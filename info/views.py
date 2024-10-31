from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


def about(request):
    """ View to handle About Us section and process Contact Form submission """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your message has been sent successfully!")
            return redirect('about')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'info/about.html', context)
