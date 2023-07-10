
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import vertexai
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from PIL import Image
import io

vertexai.init(project="hackathon-project-392216", location="us-central1")
chat_model = ChatModel.from_pretrained("chat-bison@001")
parameters = {
    "temperature": 0.2,
    "max_output_tokens": 256,
    "top_p": 0.8,
    "top_k": 40
}
chat = chat_model.start_chat()
API_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/sagu7/dating-avatar-model"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content
def Save_pic(pic,name):    
    import io
    from PIL import Image
    image = Image.open(io.BytesIO(pic))
    image.save("avatar.png")
    #image.save(f"{name}.png")
    
def history_persona(temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 500,  # Token limit determines the maximum amount of text output.
        "top_p": 0.80,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }
    char_name=input('Choose your historical persona you want to speak with:')

    list_2=['e','E']
    while char_name not in list_2:
        image_bytes = query({"inputs": f'Funny {char_name}',})
        #Save_pic(image_bytes,f'{char_name}')
        Save_pic(image_bytes,'avatar')
        img = mpimg.imread('avatar.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        
        chat = chat_model.start_chat(
            context=f'Suppose you are a {char_name}, Mimic the structure of a conversation with historical figure {char_name} .',
            examples=[
                InputOutputTextPair(
                    input_text="Where were you born and what was your strategy for the last battle?",
                    output_text="I was born in Corsica in 1875 and my last battle strategy was strategy was to isolate the Anglo-allied and Prussian armies and annihilate each one separately.",
                ),
            ],
        )

        input_q=input('What would you like me to tell you about?')
        list_1=['switch', 'SWITCH', 'Switch']
        list_1.extend(list_2)
        while input_q not in list_1:

            response = chat.send_message(
                input_q, **parameters
            )
            print(f"Response from Model: {response.text}")
            input_q=input('What would you like me to tell you about? IF YOU WANT TO SPEAK WITH SOMEONE ELSE TYPE "SWITCH".')

        char_name=input('Choose your historical persona you want to speak with: TYPE "E" TO END THE CONVERSATION.')
        
        #Start chatbot
history_persona()
    