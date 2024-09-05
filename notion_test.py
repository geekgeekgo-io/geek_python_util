from src.geek_notion_util import NotionUtil
CREW_DATABASE_ID = "f5d5d961bf8147adb79b075fe146effd"
RSS_DATABASE_ID = "d704dce624d3451697d9caf6654176ea"
def main():
    try:
        n = NotionUtil()
        results = n.query_crew_notion("geekgeekgo_news",
                                          "news_topic_creator",
                                          CREW_DATABASE_ID,
                                          "secret_Ylpf318nOypDkeizTxvaqMHkZwEVhW19gqsaAAP68CZ")
        processed_data = n.process_database_results(results)

        # Print processed data
        for item in processed_data:
            print(item)
            print("---")

        print(f"Total items: {len(processed_data)}")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        n = NotionUtil()
        results = n.get_all_notion(RSS_DATABASE_ID,"secret_Ylpf318nOypDkeizTxvaqMHkZwEVhW19gqsaAAP68CZ")
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