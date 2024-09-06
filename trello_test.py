from src.geek_trello_util import TrelloUtil

# Replace these with your actual Trello API key, token, and list ID
API_KEY = ""
TOKEN = ""
LIST_ID = ""

# FINDING LIST_ID (add .json to the end of trello link to find the board ID, and then inside find the name of the list name and then find the "id:" again
# https://docs.pixiebrix.com/integrations/trello/find-board-and-list-ids-in-trello
# Example usage
card_name = "New Task"
card_description = "This is a new task added via the API"
t = TrelloUtil()
result = t.add_card_to_trello(API_KEY, TOKEN, LIST_ID, card_name, card_description)

if result:
    print(f"Card ID: {result['id']}")
    print(f"Card URL: {result['url']}")
