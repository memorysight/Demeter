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
    
    prompt * ProptTemplate(
        input_variables={"history", "human_input"}
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
    
    
    
    
    