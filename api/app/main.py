import logging
import random
import time
import torch

from fastapi import Depends, FastAPI, HTTPException, Response, Security, status
from pydantic import BaseModel, Field, ValidationError
from transformers import GPTJForCausalLM, AutoModelForCausalLM, AutoTokenizer, pipeline


class TextData(BaseModel):
    input_text: str = Field(..., title='Input to the language model')
    temperature: float = Field(1.0, title='Temperature')
    output_length: int = Field(100, title='Length of the output')


print('Loading model...')

start = time.time()
path = '/data'

model = GPTJForCausalLM.from_pretrained(path, revision="float16", torch_dtype=torch.float16, low_cpu_mem_usage=True)
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-j-6B")

print('Time to load model:', time.time() - start)

is_gpu = torch.cuda.is_available()
print('GPU:', is_gpu)

device = torch.device('cuda' if is_gpu else 'cpu')
model.to(device)
generator = pipeline('text-generation', model=model, tokenizer=tokenizer, device=0 if is_gpu else -1)

app = FastAPI()


def generate(prompt, temperature=1.0, output_length=100):
    max_length = len(prompt.split()) + output_length
    generated_text = generator(prompt, max_length=max_length, num_return_sequences=1, temperature=temperature)[0]['generated_text']
    return generated_text


@app.get("/", include_in_schema=False)
async def _():
    return status.HTTP_200_OK


@app.get("/_health", include_in_schema=False)
async def _health():
    return status.HTTP_200_OK


@app.post("/generate_new_paragraph")
async def generate_new_paragraph(data: TextData):
    generated_text = generate(data.input_text, data.temperature, data.output_length)
    return {'generated_text': generated_text}
