from geek_rabbitmq_util import RabbitMqUtil

r = RabbitMqUtil()
r.publish_topic_messsage("home.natcheung.com",
                         "admin",
                         "QazxsW123",
                         "5672",
                         "geekgeekgo.news.summary",
                         "abc")