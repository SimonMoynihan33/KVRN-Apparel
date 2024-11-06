from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserDesignSubmission
from .forms import UserDesignSubmissionForm


@login_required
def submit_design(request):
    """
    View to submit designs to be featured on a graphic apparel product
    """
    submission_id = request.POST.get('submission_id')
    if request.method == 'POST':
        if submission_id:
            # Attempt to edit an existing submission
            submission = get_object_or_404(
                UserDesignSubmission, id=submission_id, user=request.user)

            # Check if the submission is processing or finalized
            if submission.status in ['processing', 'finalized']:
                messages.error(
                    request,
                    "This submission is already being processed or finalized \
                        and cannot be edited."
                )

                return redirect('submit_design')

            form = UserDesignSubmissionForm(
                request.POST, request.FILES, instance=submission)
        else:
            # Create a new submission if no ID provided
            form = UserDesignSubmissionForm(request.POST, request.FILES)

        if form.is_valid():
            new_submission = form.save(commit=False)
            new_submission.user = request.user
            new_submission.save()
            return redirect('submit_design')
    else:
        # Show an empty form for a new submission
        form = UserDesignSubmissionForm()

    # Display all submissions by the user
    user_submissions = UserDesignSubmission.objects.filter(user=request.user)
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
