import gradio as gr
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
import datetime
import mimetypes
import os
import traceback
from typing import List, Union
import re
import time
import requests
# from transformers import BlipProcessor, BlipForConditionalGeneration
from transformers import pipeline
import datetime
import json
import mimetypes
import os
import sys
from functools import reduce
import warnings


import webbrowser
from modules.shared import opts, cmd_opts


generator = pipeline('text-generation', model = 'gpt2')

def generate_text(txt):
    clean_results = []
    for result in generator(txt, max_length = 100, num_return_sequences=1):
        clean_text = re.sub(r'[^a-zA-Z\s]', '', result['generated_text']).strip()  # Loại bỏ ký tự không phải chữ
        clean_results.append(clean_text)
        time.sleep(0.1)
    clean_results = clean_results[0].replace("\n\n", ". ")
    # print(clean_results)

    return clean_results


def open_train_lora():
    url = "http://0.0.0.0:7860/"
    webbrowser.open(url)

   

def img2text(input_textbox):
    model = "nlpconnect/vit-gpt2-image-captioning"
    max_length = 16
    num_beams = 4
    gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
    model = VisionEncoderDecoderModel.from_pretrained(model)
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    # images = await load_image_from_request(filename, device=device)
    pixel_values = feature_extractor(images=input_textbox, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds