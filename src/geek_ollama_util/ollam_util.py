
import json
import os
import requests
from geek_common_util import CommonUtil
c = CommonUtil()
class OllamaAPI:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.generate_url = f"{self.base_url}/api/generate"
        self.context = None

    def generate(self, model, prompt, system="", format="", options=None, use_context=True):
        """
        Generate a completion using the specified model and prompt.

        :param model: The name of the model to use
        :param prompt: The prompt to generate from
        :param system: System message to send to the model (optional)
        :param format: The format to return the response in (optional)
        :param options: Additional options for the generation (optional)
        :param use_context: Whether to use and update the stored context (default: True)
        :return: The generated text
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "system": system,
            "format": format,
        }

        if options:
            payload.update(options)

        if use_context and self.context:
            payload["context"] = self.context

        try:
            response = requests.post(self.generate_url, json=payload)
            response.raise_for_status()

            full_response = ""
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line)
                    if 'response' in json_response:
                        full_response += json_response['response']

                    if json_response.get('done', False):
                        if use_context:
                            self.context = json_response.get('context')
                        break

            return full_response.strip()

        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def list_models(self):
        """
        List all available models.

        :return: A list of available model names
        """
        list_url = f"{self.base_url}/api/tags"
        try:
            response = requests.get(list_url)
            response.raise_for_status()
            models = response.json()['models']
            return [model['name'] for model in models]
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def clear_context(self):
        """
        Clear the stored context.
        """
        self.context = None

    def export_context(self, filename):
        """
        Export the current context to a file.

        :param filename: The name of the file to save the context
        """
        if self.context is not None:
            with open(filename, 'w') as f:
                json.dump(self.context, f)
            print(f"Context exported to {filename}.")

    def import_context(self, filename):
        """
        Import context from a file.

        :param filename: The name of the file to load the context from
        """
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                self.context = json.load(f)
            print(f"Context imported from {filename}.")
        else:
            print(f"File {filename} does not exist.")



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
        ollama.export_context(ollama_context_file)

        return response
