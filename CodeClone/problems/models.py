from django.db import models
from django.contrib.auth import get_user_model

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    example_input = models.TextField()
    example_output = models.TextField()
    difficulty = models.CharField(choices=[('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard')], max_length=10)

    def __str__(self):
        return self.title

class Submission(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    result = models.CharField(max_length=100)  # Store results such as "Accepted" or "Failed"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} - {self.result}"
