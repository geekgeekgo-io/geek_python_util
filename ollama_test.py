from src.geek_ollama_util import OllamaUtil

o = OllamaUtil()
OLLAMA_API_URL = "https://alienollama.geekgeekgo.io"
OLLAMA_API_PATH = "/api/generate"
OLLAMA_API = OLLAMA_API_URL + OLLAMA_API_PATH
MODEL = "llama3.1"

print(o.generate(OLLAMA_API_URL, MODEL, "tell me a funny story", "/Users/nat"))


