import pika


class Telegram:
    # Constructor to initialize the object
    def __init__(self, chat_id, message, base64, chat_group):
        self.chat_id = chat_id
        self.message = message
        self.base64 = base64
        self.chat_group = chat_group


    # Method to display dog information
    def to_dict(self):
        return {
            "chat_id": self.chat_id,
            "message": self.message,
            'base64': self.base64,
            'chat_group': self.chat_group
        }

class RabbitMqUtil:

    def create_telegram_json(self, chat_id: str, message: str, base64: str, chat_group: str):
        t = Telegram(chat_id, message.replace('"', "'"), base64, chat_group)
        t_json = t.to_dict()
        return str(t_json).replace("'", '"')

    def publish_topic_messsage(self, hostname: str, username: str, password: str, port: int, queue_name: str, message: str):
        credentials = pika.PlainCredentials(username, password)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(hostname, port=port, credentials=credentials))
        channel = connection.channel()
        queue_name = queue_name.lower()
        routing_key = queue_name
        # Declare a queue
        channel.queue_declare(queue=queue_name)

        # Publish the message
        channel.basic_publish(exchange='',
                              routing_key=routing_key,
                              body=message)
        print(f" [x] Sent '{message}'")

        # Close the connection
        connection.close()