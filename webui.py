print("Importing libraries...")

import time
from transformers import pipeline, Conversation, GPT2LMHeadModel, AutoTokenizer
import gradio as gr
import torch

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

print(config.get("PROPERTIES", "model_name"))

print("Done!")
time.sleep(1)

print("Downloading AI...")

model = GPT2LMHeadModel.from_pretrained(config["model_name"])
tokenizer = AutoTokenizer.from_pretrained(config["model_name"])

device = torch.device("cuda")
model.to(device)

chatbot = pipeline(task="conversational", model = model, tokenizer = tokenizer)

print("Done!")
time.sleep(1)

print("Generating gradio interface...")

past_user_inputs = []
generated_responses = []

def chocolate_ai(message, history):
    conversation = Conversation(message, past_user_inputs = past_user_inputs, generated_responses = generated_responses)
    conversation = chatbot(conversation)

    past_user_inputs.append(message)
    generated_responses.append(conversation.generated_responses[-1])

    return conversation.generated_responses[-1]

gradio_interface = gr.ChatInterface(chocolate_ai, title="Chocolate AI", description="Type to start a conversation.")

print("Done!")

gradio_interface.launch()