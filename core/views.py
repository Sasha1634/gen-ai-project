from django.http import JsonResponse
from core.services.sciwrite_service import analyze_paper

def analyze_view(request):
    file_path = "test.pdf"  # later replaced by upload logic

    result = analyze_paper(file_path)

    return JsonResponse(result)

# Create your views here.
