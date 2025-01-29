# LLM on local

### run on local computer

```bash
wget https://gpt4all.io/models/gguf/orca-mini-3b-gguf2-q4_0.gguf
python3 -m venv env
source env/bin/activate
pip install -r requirement.txt
python main.py
```

### deepseek

download the below model and use it
https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/blob/main/deepseek-coder-6.7b-instruct.Q3_K_S.gguf