from geek_rabbitmq_util import RabbitMqUtil

r = RabbitMqUtil()
topics_content= "this is from crew mq array"
j = r.create_telegram_json(["1363054391"], topics_content, "image_path", "geekgeekgo_news")
r.publish_topic_messsage("home.natcheung.com",
                         "admin",
                         "QazxsW123",
                         "5672",
                         "geekgeekgo_news",
                         j)