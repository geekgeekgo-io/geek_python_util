from src.geek_wordpress_util import WordPressUtil
# Example usage
if __name__ == "__main__":
    wp_util = WordPressUtil("https://www.geekgeekgo.io", "nat", "your_password")
    media_info = wp_util.upload_media("/path/to/your/file.pdf")

    if media_info:
        post = wp_util.create_post(
            title="My New Post",
            content="This is the content of my new post.",
            status="publish",
            media_ids=[media_info["id"]]  # Use the uploaded media ID
        )

