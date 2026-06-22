from django.shortcuts import render, redirect, get_object_or_404
from .models import Resume
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def resume_form(request):

    if request.method == "POST":

        data = Resume.objects.create(

            user=request.user,

            name=request.POST['name'],
            title=request.POST['title'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            address=request.POST['address'],
            summary=request.POST['summary'],
            education=request.POST['education'],
            experience=request.POST['experience'],
            skills=request.POST['skills'],
            template=request.POST['template']
        )

        if data.template == "template1":
            return render(
                request,
                'template1.html',
                {'resume': data}
            )

        return render(
            request,
            'template2.html',
            {'resume': data}
        )

    return render(request, 'form.html')


@login_required
def my_resumes(request):

    resumes = Resume.objects.filter(
        user=request.user
    )

    return render(
        request,
        'my_resumes.html',
        {'resumes': resumes}
    )


@login_required
def delete_resume(request, id):

    resume = get_object_or_404(
        Resume,
        id=id,
        user=request.user
    )

    resume.delete()

    return redirect('my_resumes')


@login_required
def view_resume(request, id):

    resume = get_object_or_404(
        Resume,
        id=id,
        user=request.user
    )

    if resume.template == "template1":
        return render(
            request,
            'template1.html',
            {'resume': resume}
        )

    return render(
        request,
        'template2.html',
        {'resume': resume}
    )