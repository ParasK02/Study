from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from quiz.models import User, Course, Lesson, Assignment


def index(request):
    return render(request, 'quiz/index.html',{'courses':Course.objects.all()})

@login_required
def profile(request):
    # Display the user's profile
    user_profile = get_object_or_404(User, user=request.user)
    return render(request, 'profile.html', {'user_profile': user_profile})
        


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "quiz/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "quiz/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "quiz/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "quiz/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "quiz/register.html")
    
# @login_required
def createCourse(request):
    if request.method == 'POST':
        user = request.user  # Use the actual user instance
        title = request.POST['title']
        description = request.POST['description']
    
        course = Course(title=title, description=description, professor=user)
        course.save()
        course_url = reverse('viewCourse', args=[course.id])

        return HttpResponseRedirect(course_url)
    else:
        return render(request, 'quiz/index.html')

        
# View a single course and its quizzes


def viewCourse(request,courseID):
    course = get_object_or_404(Course, id=courseID)
    return render(request, "quiz/course.html",{
        'course': course,
        })

def createLesson(request):
    if request.method == 'POST':
        lessonTitle = request.POST['title']
        overview = request.POST['overview']
        courseId = request.POST['course_id']
        course = get_object_or_404(Course, id=courseId)
        lesson = Lesson(title=lessonTitle,content = overview ,course=course)
        lesson.save()
        course.lessons.add(lesson)

        # Return a JSON response indicating success
        return JsonResponse({'success': True})

    # Handle other HTTP methods or return an error response
    return JsonResponse({'success': False, 'error': 'Invalid method'})
def createAssignment(request,lessonID,courseID):
    if request.method == 'POST':
        assignmentName = request.POST['assignment']
        assignmentdesc = request.POST['assignment_description']
        dueDate = request.POST['due_date']
        deadline = request.POST['deadline']
        lesson = get_object_or_404(Lesson,id = lessonID)
        assignment = Assignment(title = assignmentName, description = assignmentdesc, dueDay = dueDate, deadline = deadline, lesson = lesson)
        assignment.save()
        lesson.assignments.add(assignment)
        course_url = reverse('viewCourse', args=[courseID])
        return HttpResponseRedirect(course_url)
    else:
        return render(request, 'quiz/assignment.html', {})
def viewAssignment(request,assignmentID,courseID,lessonID):
    assignment = get_object_or_404(Assignment,id=assignmentID)
    course = get_object_or_404(Course,id=courseID)
    return render(request,'quiz/assignmentView.html',{'assignment':assignment, 'course':course})


        
    


   