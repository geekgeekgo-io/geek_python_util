import requests
import base64
import os

class WordPressUtil:
    def __init__(self, wp_url, wp_user, wp_pass):
        self.wp_url = wp_url
        self.wp_user = wp_user
        self.wp_pass = wp_pass
        self.media_url = f"{self.wp_url}/wp-json/wp/v2/media"
        self.post_url  = f"{self.wp_url}/wp-json/wp/v2/posts"
        self.headers = self._create_auth_headers()

    def _create_auth_headers(self):
        credentials = f"{self.wp_user}:{self.wp_pass}"
        token = base64.b64encode(credentials.encode())
        return {
            "Authorization": f"Basic {token.decode('utf-8')}",
        }

    def upload_media(self, file_path):
        if not os.path.isfile(file_path):
            print("File not found:", file_path)
            return None

        file_name = os.path.basename(file_path)
        files = {
            "file": (file_name, open(file_path, "rb"), "application/pdf")
        }

        response = requests.post(self.media_url, headers=self.headers, files=files)

        if response.status_code == 201:
            print("PDF uploaded successfully!")
            print("Media ID:", response.json()["id"])
            print("Media URL:", response.json()["source_url"])
            return response.json()
        else:
            print("Failed to upload PDF")
            print("Status code:", response.status_code)
            print("Response:", response.text)
            return None

    def create_post(self, title, content, status='publish', media_ids=None):
        post_data = {
            'title': title,
            'content': content,
            'status': status,
        }

        if media_ids:
            post_data['featured_media'] = media_ids[0]  # Set the first media ID as featured

        response = requests.post(f"{self.post_url}", headers=self.headers, json=post_data)

        if response.status_code in [201, 200]:
            print("Post created successfully!")
            print("Post ID:", response.json()["id"])
            return response.json()
        else:
            print("Failed to create post")
            print("Status code:", response.status_code)
            print("Response:", response.text)
            return None