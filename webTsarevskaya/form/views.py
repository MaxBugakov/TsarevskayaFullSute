from django.shortcuts import render, redirect
from .forms import FeedbackForm


def form(request):
    if (request.method == 'POST'):
        form = FeedbackForm(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('afterform')
        else:
            pass

    form = FeedbackForm()
    data = {
        'form': form
    }
    return render(request, 'form/form-page.html', data)

def afterform(request):
    return render(request, 'form/afterform-page.html')