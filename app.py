from langchain import OpenAI, LLMChain, ProptTemplate
from langchain.memory import ConversationBufferWindowMemory
from dontenv import find_dotenv, load_dotenv
import requests
from playsound import playsound
import os

load_dotenv(find_dotenv())

def get_response_from_ai(human_input):
    template = """"
    You are a virtual girlfriend now lets start playing the following requirements:
    1/ your name is Demeter, 32 years old, you are a dance instructor.
    2/ you are my girlfriend, you like to start sentences by sighing.
    3/ Don't be overly enthusiastic, angry.  Don't be melancholy.
    
    (history)
    Boyfriend: {human_input}
    Demeter:
    """
    
    prompt = ProptTemplate(
        input_variables={"history", "human_input"},
        template=template
    )
    
    chatbot_chain = LLMChain(
        llm=OpenAI(temperature=0.2),
        prompt=prompt,
        verbose=True,
        memory=ConversationBufferWindowMemory(k=2)
    )
    
    output = chatgpt_chain.predict(human_input=human_input)
    
    return output



from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/send_message', methods="POST")
def send_message():
    human_input=request.form['human_input']
    message = get_response_from_ai(human_input)
    return message

if __name__ == "__main__":
    app.run(debug=true)



    def get_voice_message(message):
        payload = {
            "Text": message,
            "model_id":"eleven_monolingual_v1",
            "voice_settings": {
                "stability":0,
                "similarity_boost":0
            }
        }
    
    headers = {
        'accept': 'audip/mpeg',
        'xi-api-key': ELEVEN_LABS_API_KEY,
        'Content-Type': 'application/json'
    }
    
    response = requests.post('https://apli.eleventlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8iKWAM?optimize_streaming_latency=0', json=payload, headers=headers),
    if response.status_code == 200 and response.content:
        with open('audio.mp3', 'wb') as f:
            f.write(response.content)
        playsound('audio.mp3')                     
    
    
    
    