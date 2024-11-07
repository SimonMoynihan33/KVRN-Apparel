from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact


def about(request):
    """View to handle About Us section and process Contact Form submission"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your message has been sent successfully!")
            return redirect("about")
    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, "info/about.html", context)


@login_required
def contact_messages_view(request):
    """View for superusers to view contact messages in read-only format."""
    if not request.user.is_superuser:
        messages.error(
            request, "You do not have permission to view this page.")
        return redirect("home")  # Redirect non-superusers to home

    # Retrieve contact messages if the user is a superuser
    contact_messages = Contact.objects.all().order_by("-submitted_at")
    return render(
        request, "info/messages_list.html",
        {"contact_messages": contact_messages}
    )


def faq_page(request):
    """Render the FAQ page."""
    return render(request, "info/faq.html")
