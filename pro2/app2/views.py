from django.shortcuts import render
from app2 import forms

def index(request):
    return render(request, 'app2/index.html')

def form_name_view(request):
    form = forms.Form1()

    if request.method == 'POST':
        print("Form submitted")  # Debug: Check if the form is submitted
        form = forms.Form1(request.POST)
        if form.is_valid():
            print("Validation success")  # Debug: Check if the form is valid
            print('Name:', form.cleaned_data['name'])
            print('Email:', form.cleaned_data['email'])
            print('Text:', form.cleaned_data['text'])

            # Optionally, you could redirect to a new URL or render a success template
            return render(request, 'app2/formpage.html', {'form': form, 'success': True})
        else:
            print("Form is not valid")  # Debug: Check if the form is not valid
    else:
        print("Request method is not POST")  # Debug: Check if the request method is not POST

    # If the form is not valid or it is a GET request, render the form template
    return render(request, 'app2/formpage.html', {'form': form})
