from django.http import JsonResponse

def api_key(func):
    def wrapper(self,request,*args,**kwargs):
        if not request.headers.get('api-key'):
            return JsonResponse({"response":"You must add 'api-key' to your headers"})
        elif request.headers.get('api-key') != 'b150db6374bc12fefd6e3c705127bf95b6b4937b721799598c':
            return JsonResponse({"response":"invalid 'api-key'"})
        else:
            return func(self,request,*args,**kwargs)
    return wrapper