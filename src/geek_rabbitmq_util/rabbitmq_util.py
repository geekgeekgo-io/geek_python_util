import pika

class RabbitMqUtil:

    def create_telegram_json(self, chat_id, message, base64, chat_group):
        data = {
            "chat_id": chat_id,
            "message": message,
            "base64": base64,
            "chat_group": chat_group
        }
        return data

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