document.addEventListener("DOMContentLoaded", function () {
    document.getElementById('openModalBtn').addEventListener('click', function () {
        document.getElementById('createCourseModal').style.display = 'block';
        console.log("Pressed Button")
    });

    document.getElementsByClassName('close')[0].addEventListener('click', function () {
        document.getElementById('createCourseModal').style.display = 'none';
    });

    window.addEventListener('click', function (event) {
        if (event.target == document.getElementById('createCourseModal')) {
            document.getElementById('createCourseModal').style.display = 'none';
        }
    });

    
});

function submitForm(formId, successCallback) {
    $.ajax({
        url: $(`#${formId}`).attr('action'),
        type: 'POST',
        data: $(`#${formId}`).serialize(),
        success: function (response) {
            if (response.success) {
                alert('Operation successful!');
                successCallback(response);
            } else {
                alert(`Error: ${response.error}`);
            }
        },
        error: function (xhr, errmsg, err) {
            alert(`Ajax Error: ${errmsg}`);
        },
    });
}

// Lesson form submission
$('#createCourseForm').submit(function (event) {
    event.preventDefault();
    submitForm('createCourseForm', function (response) {
        // Handle success, e.g., close the modal or show a success message
        $('#createCourseModal').hide();
        // Parse the serialized lesson data
        var lesson = JSON.parse(response.lesson)[0];
        // Append the new lesson to the list dynamically
        var lessonList = $('#lessonList');
        lessonList.append('<div>' +
            `<h3>${lesson.fields.title}</h3>` +
            '<button class="openAssignmentModalBtn" data-lesson-id="' + lesson.pk + '">Add Assignment</button>' +
            // ... Other lesson details
            '</div>');
    });
});

