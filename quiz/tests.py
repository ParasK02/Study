from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from .models import Assignment, User,Submission,Lesson,Course  # Import necessary models

class AssignmentSubmissionTest(TestCase):

    def setUp(self):
        # Set up any necessary objects like a user, assignment, etc.
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
      
        self.course = Course.objects.create(title="Test Course", description="Test", professor=self.user)
        self.lesson = Lesson.objects.create(title="Test Lesson", content="Test", course=self.course)
        self.assignment = Assignment.objects.create(title="Test Assignment", description="Test", dueDay="2021-05-05", deadline="00:00:00", lesson=self.lesson)
    def test_file_upload(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')

        # Prepare a sample file
        sample_file = SimpleUploadedFile("test_file.txt", b"file_content", content_type="text/plain")

        # Build the POST request data
        data = {
            'title': 'Test Submission',
            'content': sample_file,
            # Add other form fields if necessary
        }

        # Send POST request
        response = self.client.post(reverse('submission', args=[self.assignment.id, self.lesson.id, self.course.id]), data)

        # Check that the response is what you expect
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Submission.objects.count(), 1)  # Assuming a Submission should be created

        # Additional assertions as necessary
    def test_file_upload2(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')

        # Prepare a sample file
        sample_file = SimpleUploadedFile("test_file.txt", b"file_content", content_type="text/plain")
        sample_file2 = SimpleUploadedFile("test_file2.txt", b"file_content", content_type="text/plain")

        sample_files = [sample_file, sample_file2]
        # Build the POST request data
        data = {
            'title': 'Test Submission',
            'content': sample_files,
            # Add other form fields if necessary
        }

        # Send POST request
        response = self.client.post(reverse('submission', args=[self.assignment.id, self.lesson.id, self.course.id]), data)

        # Check that the response is what you expect
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Submission.objects.count(), 2)  # Assuming a Submission should be created

        # Additional assertions as necessary
