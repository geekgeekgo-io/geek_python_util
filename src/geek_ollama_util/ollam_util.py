import pika
import json
import requests
from .models.Ollama import OllamaAPI
import os
class OllamaUtil:

    def is_file_exist(self, file_full_path: str):
        if os.path.isfile(file_full_path):
            return True
        else:
            return False

    def generate(self, ollama_api_url, model: str, prompt: str, folder: str):
        ollama = OllamaAPI(base_url=ollama_api_url)
        ollama_context_file = folder + "context.json"
        if self.is_file_exist(ollama_context_file):
            ollama.import_context(ollama_context_file)
        else:
            ollama.clear_context()
        response = ollama.generate(model, prompt)

        return response
