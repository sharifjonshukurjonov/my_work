# from http.cookiejar import request_path

# from webob import Request, Response
#
# class FrameWorkApp:
#     def __init__(self):
#         self.routes = dict()
#     def __call__(self, environ, start_response):
#         req = Request(environ)
#         res = self.handle_request(req)
#         return res(environ, start_response)
#
#     def handle_request(self, request):
#         res = Response()
#         is_there = False
#
#         for path, handler in self.routes.items():
#             lst = request.path.split("/")
#             if len(lst) > 2 and lst[1] == "u":
#                 handler(request,res, lst[2])
#                 is_there= True
#             if path == request.path:
#                 handler(request, res)
#                 is_there = True
#
#         if not is_there:
#             self.default_response(res)
#
#         return res
#
#     def default_response(self, response):
#         response.status_code = 404
#         response.text = ("ERROR: 404 ... ... ...\n"
#                          "\nURLda xatolik bor, iltimos tekshiribbir ozdan so'ng urunib ko'ring!")
#
#     def route(self, path):
#         def wrapper(handler):
#             self.routes["/" + path] = handler
#             return handler
#         return wrapper



"""HOMEWORK"""

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
        is_there = False

        for path, handler in self.routes.items():
            lst = request.path.split("/")
            if len(lst) > 2 and lst[1] == "u":
                handler(request, res, lst[2], is_admin=False)
                is_there = True
            elif len(lst) > 2 and lst[1] == "admin":
                handler(request, res, lst[2], is_admin=True)
                is_there = True
            elif path == request.path:
                handler(request, res)
                is_there = True

        if not is_there:
            self.default_response(res)

        return res

    def default_response(self, response):
        response.status_code = 404
        response.text = ("ERROR: 404 ... ... ...\n"
                         "\nURLda xatolik bor, iltimos tekshirib bir ozdan so'ng urunib ko'ring!")

    def route(self, path):
        def wrapper(handler):
            self.routes["/" + path] = handler
            return handler
        return wrapper

