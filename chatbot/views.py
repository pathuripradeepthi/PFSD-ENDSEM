import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Load your OpenAI API key
openai.api_key = 'your-openai-api-key'

@csrf_exempt
def chat_with_gpt(request):
    if request.method == 'POST':
        # Get the user message from the request body
        data = json.loads(request.body)
        user_message = data.get('message', '')

        try:
            # Send the message to OpenAI's GPT model
            response = openai.Completion.create(
                engine="text-davinci-003",  # or use gpt-4 if available
                prompt=user_message,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )

            # Get the reply from GPT
            gpt_response = response.choices[0].text.strip()

            # Return the response as JSON
            return JsonResponse({'response': gpt_response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
