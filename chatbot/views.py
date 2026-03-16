from django.shortcuts import render
from django.http import JsonResponse
from .nlp_model import get_bot_response

def chatbot_view(request):
    if request.method == "POST":
        user_message = request.POST.get("message")
        response = get_bot_response(user_message)
        return JsonResponse({"reply": response})

    return render(request, "chat.html")