from rest_framework.renderers import JSONRenderer

class CustomJSONRenderer(JSONRenderer):
    """
    Custom global response format:
    {
        "status": true/false,
        "message": "text",
        "data": {... or [...] or None}
    }
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get("response", None)

        # Default structure
        response_data = {
            "status": True,
            "message": "Success",
            "data": data
        }

        # If it's an error response (4xx or 5xx)
        if response is not None and response.status_code >= 400:
            response_data["status"] = False
            response_data["message"] = "Error"
            response_data["data"] = None

            # Include detailed errors if available
            if isinstance(data, dict) and "detail" in data:
                response_data["message"] = data["detail"]
            elif isinstance(data, dict):
                response_data["errors"] = data

        return super(CustomJSONRenderer, self).render(response_data, accepted_media_type, renderer_context)
