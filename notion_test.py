from src.geek_notion_util import NotionUtil

def main():
    try:
        n = NotionUtil()

        results = n.query_notion_database("geekgeekgo_news",
                                          "news_topic_creator",
                                          "f5d5d961bf8147adb79b075fe146effd",
                                          "secret_Ylpf318nOypDkeizTxvaqMHkZwEVhW19gqsaAAP68CZ")
        processed_data = n.process_database_results(results)

        # Print processed data
        for item in processed_data:
            print(item)
            print("---")

        print(f"Total items: {len(processed_data)}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()