# pip install gpt4all
from gpt4all import GPT4All
import sys


def draw_cat():
    model = GPT4All(model_name='orca-mini-3b-gguf2-q4_0.gguf', allow_download=False, model_path='.')
    tokens = []
    for token in model.generate("How many overs are there is in a one day cricket match?", streaming=True):
        tokens.append(token)
        sys.stdout.write(token)

    sys.stdout.flush()


if __name__ == '__main__':
    draw_cat()
