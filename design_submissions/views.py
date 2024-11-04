from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserDesignSubmission
from .forms import UserDesignSubmissionForm


@login_required
def submit_design(request):
    """
    View to submit designs to be featured on a graphic apparel product
    """
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


@login_required
def delete_submission(request, submission_id):
    """
    View to delete user uploaded submissions
    """
    submission = get_object_or_404(
        UserDesignSubmission, id=submission_id, user=request.user)
    submission.delete()
    return redirect('submit_design')


@login_required
def edit_submission(request, submission_id):
    submission = get_object_or_404(
        UserDesignSubmission, id=submission_id, user=request.user)
    if request.method == 'POST':
        form = UserDesignSubmissionForm(
            request.POST, request.FILES, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('submit_design')
    else:
        form = UserDesignSubmissionForm(instance=submission)
    return render(
        request, 'design_submissions/edit_submission.html',
        {'form': form, 'submission': submission})
