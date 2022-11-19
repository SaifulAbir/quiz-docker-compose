from rest_framework import permissions, status, views,viewsets
from utils.response_wrapper import ResponseWrapper
class CustomRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        
        msg = None
        if data:
            try:
                if isinstance(data, list):
                    data = data[0]
                msg = data["msg"]
                del data["msg"]
            except Exception:
                msg = None
        
        custom_msg = None
        if response.status_code > 299 or response.status_code < 200:
            custom_msg = "Failed"
        else:
            custom_msg = "Success"

        response_dict = {
            "status": {"code": response.status_code, "text": response.status_text},
            "data": data,
            "msg": msg if msg else custom_msg,
        }

        return super().render(response_dict, accepted_media_type, renderer_context)