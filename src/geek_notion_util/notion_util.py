import pika
import json
import requests

class NotionUtil:

    def query_notion_database(self, application_name: str, crew: str, notion_api: str, database_id: str, notion_api_key: str):
        headers = {
            "Authorization": f"Bearer " + notion_api_key,
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }
        filter_data = {
            "filter": {
                "and": [
                    {
                        "property": "app",  # Replace with your first field name
                        "rich_text": {
                            "equals": application_name  # Replace with the value to match
                        }
                    },
                    {
                        "property": "crew",  # Replace with your second field name
                        "rich_text": {
                            "equals": crew  # Replace with the value to match
                        }
                    }
                ]
            }

        }
        response = requests.post(notion_api, headers=headers, json=filter_data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error querying database: {response.status_code} {response.text}")

    def process_database_results(self, results):
        processed_data = []
        for page in results["results"]:
            item = {}
            properties = page["properties"]

            # Process each property (adjust according to your database structure)
            for prop_name, prop_data in properties.items():
                prop_type = prop_data["type"]
                if prop_type == "title":
                    item[prop_name] = prop_data["title"][0]["plain_text"] if prop_data["title"] else ""
                elif prop_type == "rich_text":
                    item[prop_name] = prop_data["rich_text"][0]["plain_text"] if prop_data["rich_text"] else ""
                elif prop_type == "number":
                    item[prop_name] = prop_data["number"]
                elif prop_type == "select":
                    item[prop_name] = prop_data["select"]["name"] if prop_data["select"] else ""
                elif prop_type == "multi_select":
                    item[prop_name] = [option["name"] for option in prop_data["multi_select"]]
                elif prop_type == "date":
                    item[prop_name] = prop_data["date"]["start"] if prop_data["date"] else None
                elif prop_type == "checkbox":
                    item[prop_name] = prop_data["checkbox"]
                # Add more property types as needed

            processed_data.append(item)
        return processed_data

