from django.shortcuts import render
from .bot import UniversityChatbot

bot = UniversityChatbot()

def chatbot_view(request):

    # chat history
    if 'chat_history' not in request.session:
        request.session['chat_history'] = []
    chat_history = request.session['chat_history']

    if request.GET.get('clear'):
        request.session['chat_history'] = []

    #response = None

    if request.method == 'POST':
        question = request.POST.get('question')
        response = bot.get_response(question)

        chat_history.append({
            'question': question,
            'answer': response,
        })

        request.session['chat_history'] = chat_history

    return render(request, 'chatbot/index.html', {'chat_history': chat_history})

