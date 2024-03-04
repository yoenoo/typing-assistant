import requests
from string import Template

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
OLLAMA_CONFIG = {
  "model": "mistral:7b-instruct-v0.2-q4_K_S",
  "keep_alive": "5m",
  "stream": False,
}
PROMPT_TEMPLATE = Template(
"""Fix all misspelling, typos and casing and punctutation in the text provided below, but preserve all new line characters. Return only the corrected text, don't inclue a preamble.

$text
"""
)

def text_correct(txt: str):
  prompt = PROMPT_TEMPLATE.safe_substitute({"text": txt})
  r = requests.post(OLLAMA_ENDPOINT, 
                    json={"prompt": prompt, **OLLAMA_CONFIG},
                    headers={"Content-Type": "application/json"}, 
                    timeout=10)

  if r.status_code != 200:
    raise ValueError(f"invalid response")

  return r.json().get("response").strip()

def text_generate(txt: str):
	pass

def text_summarize(txt: str):
	pass


if __name__ == "__main__":
  p = "Thiss isa tyypong testt withh manyy typos\nPyytthonn iss sooo cooll"
  print(p)
  p = PROMPT_TEMPLATE.substitute(text=p)
  out = text_correct(p)
  print(out)
