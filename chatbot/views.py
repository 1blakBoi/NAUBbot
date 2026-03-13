from django.shortcuts import render
from .bot import UniversityChatbot

bot = UniversityChatbot()

def chatbot_view(request):

    response = None

    if request.method == 'POST':
        question = request.POST.get('question')
        response = bot.get_response(question)
    return render(request, 'chatbot/index.html', {'response': response})

