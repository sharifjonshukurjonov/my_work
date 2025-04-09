from webob import Request, Response



class FrameWorkApp:
    def __init__(self):
        self.routes = dict()

    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self, request):
        res = Response()
        path = request.path
        matched = False

        for route_path, handler in self.routes.items():
            lst = path.strip("/").split("/")

            if route_path == "/admin/login" and len(lst) >= 3 and "/".join(lst[:2]) == "admin/login":
                handler(request, res, lst[2])
                matched = True
                break


            elif route_path == "/u/id" and len(lst) >= 3 and "/".join(lst[:2]) == "u/id":
                handler(request, res, lst[2])
                matched = True
                break

            elif route_path == path:
                handler(request, res)
                matched = True
                break

        if not matched:
            self.default_response(res)

        return res

    def default_response(self,response):
        response.status_code = 404
        response.text = "URL xatolik bor , topilmadi!"

    def route(self, path):
        def wrapper(handler):
            self.routes[path] = handler
            return handler

        return wrapper
