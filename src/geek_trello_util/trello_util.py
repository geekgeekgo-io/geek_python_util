import requests


class TrelloUtil:
    def add_card_to_trello(self, api_key, token, list_id, card_name, card_description=""):
        url = "https://api.trello.com/1/cards"

        query = {
            'key': api_key,
            'token': token,
            'idList': list_id,
            'name': card_name,
            'desc': card_description
        }

        response = requests.post(url, params=query)

        if response.status_code == 200:
            print("Card added successfully!")
            return response.json()
        else:
            print(f"Failed to add card. Status code: {response.status_code}")
            print(response.text)
            return None
