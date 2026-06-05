from dotenv import load_dotenv
import os
from mistralai.client import Mistral

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
model = "ministral-3b-2512"

client = Mistral(api_key = api_key)
query = input()

chat_response = client.chat.complete(
        model = model,
        messages = [
            {
                "role" : "user",
                "content" : query,
            }
        ]
    )

print(chat_response)
print(chat_response.choices[0].message.content)


'''
Sample Conversation and Structure of chat_response

query = "who won IPL 2026?"

chat_response = 

id='5a217e42017742f29980b3a434efd1f0'
object='chat.completion' 
model='ministral-3b-2512' 
usage=UsageInfo(prompt_tokens=13, completion_tokens=110, total_tokens=123, prompt_audio_seconds=Unset(), prompt_tokens_details={'cached_tokens': 0}) 
created=1780683081 
choices=
[
	ChatCompletionChoice(
			index=0, 
			finish_reason='stop', 
			message=AssistantMessage(
				role='assistant', 
				content='As of now (June 2024), the **IPL 2026** season has not yet been played. 
						The **Indian Premier League (IPL)** is scheduled to begin on **March 22, 2026**, 
						with the **Royal Challengers Bangalore (RCB)** as the defending champions (who won IPL 2025).\n\n
						Would you like details on the **IPL 2026 schedule, teams, or predictions**? Let me know! 🏏', 
				tool_calls=None, 
				prefix=False
				), 
			messages=None
		)
]
'''
