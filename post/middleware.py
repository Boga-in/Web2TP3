
class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"New Request: {request.method} {request.path}")
        print(f"PARAMETROS GET: {request.GET}")
        print(f"PARAMETROS POST: {request.POST}")

        response = self.get_response(request)

        return response