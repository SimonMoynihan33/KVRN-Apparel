from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserDesignSubmission
from .forms import UserDesignSubmissionForm


@login_required
def submit_design(request):
    form = UserDesignSubmissionForm()
    user_submissions = UserDesignSubmission.objects.filter(user=request.user)

    if request.method == 'POST':
        form = UserDesignSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.save()
            return redirect('submit_design')

    return render(request, 'design_submissions/submit_design.html', {
        'form': form,
        'user_submissions': user_submissions,
    })
