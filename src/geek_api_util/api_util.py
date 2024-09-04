from models.response_payload import ResponsePayload


class ApiUtil():
    def success_response(self, data:str, status_code=200):
        r = ResponsePayload(data=data, status_code=201)
        return r
