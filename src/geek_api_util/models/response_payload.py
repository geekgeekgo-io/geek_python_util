class ResponsePayload:
    def __init__(self, message: str, status: str):
        self.status = status
        self.data = {
            "message": message
        }

    def to_dict(self):
        return {
            "status": self.status,
            "data": self.data
        }
