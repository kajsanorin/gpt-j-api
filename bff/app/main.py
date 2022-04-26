import gradio as gr
import json
import requests
import time


# def generate(prompt, temperature, output_length):
#     max_length = len(prompt.split()) + output_length
#     generated_text = generator(prompt, max_length=max_length, num_return_sequences=1, temperature=temperature)[0]['generated_text']
#     return generated_text


def gradio_helper(prompt, temperature, output_length):
    body = json.dumps({'input_text': prompt, 'temperature': temperature, 'output_length': output_length})
    r = requests.post('http://0.0.0.0:8001/generate_new_paragraph', data=body)
    return r.json()['generated_text']
    # return r.text

iface = gr.Interface(
    fn=gradio_helper,
    inputs=[
        gr.inputs.Textbox(lines=18, placeholder="Prompt here, for example SHORT DESCRIPTION, SCENE or New newsletter"),
        gr.inputs.Slider(minimum=0.2, maximum=3.5, default=1.0),
        gr.inputs.Slider(minimum=5, maximum=2000, default=100) # length of output (in tokens),
        ],
    outputs='text',
    title='Educated Ether GPT-J',
    description='An interface to interact with the fine-tuned language model created as a collaboration between Olle Strandberg and Kajsa Norin.',
    theme="dark-huggingface",
    allow_flagging='never'
)

    



# if __name__ == "__main__":
app, local_url, share_url = iface.launch(server_port=80, server_name='0.0.0.0', share=False)
