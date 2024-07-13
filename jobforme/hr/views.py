from django.shortcuts import render

# Create your views here.
def hrHome_view(request):
    return render(request,'hr/hrHome.html')

def post_job_view(request):
    return render(request,'hr/post_job.html')

def candidate_view(request):
    return render(request,'hr/candidate.html')