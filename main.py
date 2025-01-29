# pip install gpt4all
from gpt4all import GPT4All
import sys

# https://huggingface.co/TheBloke
# https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF
models = {
    'orca-mini':'orca-mini-3b-gguf2-q4_0.gguf',
    'deepseek-llm-small':'deepseek-llm-7b-chat.Q3_K_S.gguf', # https://huggingface.co/TheBloke/deepseek-llm-7B-chat-GGUF/blob/main/deepseek-llm-7b-chat.Q3_K_S.gguf
    'deepseek-coder-small':'deepseek-coder-6.7b-instruct.Q3_K_S.gguf',
    'deepseek-coder-medium':'deepseek-coder-6.7b-instruct.Q5_K_M.gguf',
}
    
    
    
inputs = [
    "How many overs are there is in a one day cricket match?",
    "How to calculate fibonnaci series in python?",
]

# def draw_cat():
#     model = GPT4All(model_name=models[1], allow_download=False, model_path='.')
#     tokens = []
#     for token in model.generate(inputs[1], streaming=True):
#         tokens.append(token)
#         sys.stdout.write(token)

#     sys.stdout.flush()



def example():
    model = GPT4All(model_name=models['deepseek-llm-small'], allow_download=False, model_path='.')
    with model.chat_session():
        for i in range(3):
            t = input('>> ')
            if t=='q': break
            print(model.generate(t))

if __name__ == '__main__':
    # draw_cat()
    example()
