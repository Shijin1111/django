from django.shortcuts import render, get_object_or_404
from .models import Problem, Submission
from django.contrib.auth.decorators import login_required

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problems/problem_list.html', {'problems': problems})

def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    return render(request, 'problems/problem_detail.html', {'problem': problem})

@login_required
def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)
    if request.method == 'POST':
        code = request.POST.get('code')
        # Execute code safely (requires sandboxing for security)
        result = execute_code(code, problem)  # Define this function for code execution
        submission = Submission(user=request.user, problem=problem, code=code, result=result)
        submission.save()
        return render(request, 'problems/submission_result.html', {'result': result})
    return render(request, 'problems/problem_detail.html', {'problem': problem})
