from django.shortcuts import render

# Create your views here.
def all_my(reqest):
  return render(reqest,'My/all_My.html')