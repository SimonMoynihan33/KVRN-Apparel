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
    submission_id = request.POST.get("submission_id")
    user_submissions = UserDesignSubmission.objects.filter(user=request.user)

    if submission_id:
        submission = get_object_or_404(
            UserDesignSubmission, id=submission_id, user=request.user
        )

        # Prevent editing if the status is 'processing' or 'finalized'
        if submission.status in ["processing", "finalized"]:
            messages.warning(
                request,
                "This submission cannot be edited as it is already \
                    being processed or finalized.",
            )
            form = UserDesignSubmissionForm()
        else:
            if request.method == "POST":
                form = UserDesignSubmissionForm(
                    request.POST, request.FILES, instance=submission
                )
                form.fields.pop("email", None)

                if form.is_valid():
                    submission = form.save(commit=False)
                    submission.email = submission.email  # Keep existing email
                    submission.save()
                    messages.success(
                        request,
                        "Your design submission has been successfully\
                             updated!",
                    )
                    form = UserDesignSubmissionForm()
                else:
                    messages.error(
                        request,
                        "There was an error updating your submission.\
                             Please check the form.",
                    )
            else:
                form = UserDesignSubmissionForm(instance=submission)
                form.fields.pop("email", None)  # Exclude email field from form
    else:
        if request.method == "POST":
            form = UserDesignSubmissionForm(request.POST, request.FILES)
            if form.is_valid():
                submission = form.save(commit=False)
                submission.user = request.user
                submission.save()
                messages.success(
                    request,
                    "Your design submission has been successfully \
                        created!",
                )
                form = UserDesignSubmissionForm()
            else:
                messages.error(
                    request,
                    "There was an error with your \
                    submission. Please check the form.",
                )
        else:
            form = UserDesignSubmissionForm()

    return render(
        request,
        "design_submissions/submit_design.html",
        {"form": form, "user_submissions": user_submissions},
    )


@login_required
def delete_submission(request, submission_id):
    """
    View to delete user uploaded submissions
    """
    submission = get_object_or_404(
        UserDesignSubmission, id=submission_id, user=request.user
    )
    submission.delete()
    return redirect("submit_design")
