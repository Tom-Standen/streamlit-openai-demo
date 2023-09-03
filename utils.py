import os
from typing import Dict
import openai
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)  # for exponential backoff
from models import ModelParameters, PromptParameters

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def openai_create_messages_dict(system_message_template: str, user_input_template: str, variables: Dict):
    
    # Start with the system message
    system_message = {
        "role": "system",
        "content": system_message_template.format(**variables)
    }

    # Create the user message
    user_message = {
        "role": "user",
        "content": user_input_template.format(**variables)
    }

    # Return a list of the messages in the order they should be processed
    return [system_message, user_message]

@retry(wait=wait_random_exponential(min=1, max=3), stop=stop_after_attempt(3))
async def openai_chat_completion(model_name: str, temperature: str, max_tokens:str, messages: Dict, stream=False):
    """
    Wrapper to make a chat completion to OpenAI API with a timeout.
    """
    return await openai.ChatCompletion.acreate(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.5,
            stream=stream
        )

def handleSend(model_params: ModelParameters, prompt_params: PromptParameters):
    translate_prompt_template = open_file(filepath=os.path.join("prompts", "chat", "translate.txt"))
    user_input_template = open_file(filepath=os.path.join("prompts", "chat", "user_input.txt"))

    # Create the messages dict
    messages = openai_create_messages_dict(translate_prompt_template, user_input_template, prompt_params.dict())
    return openai_chat_completion(model_params.model_name, model_params.temperature, model_params.max_len, messages, stream=False)

