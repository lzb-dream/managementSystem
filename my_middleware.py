import jwt
from django.conf import settings
from django.http import JsonResponse
import json
import re
from django.utils.deprecation import MiddlewareMixin


class Myware(MiddlewareMixin):
    # 请求到达路由之前
    def process_request(self, request):
        if request.path == '/login':
            return None
        else:
            token = request.META.get('HTTP_AUTHORIZATION')
            print('token', token)
            try:
                parse_token = jwt.decode(token,settings.SECRET_KEY,['HS256'])
                print('parse_token', parse_token)
            except:
                print('令牌错误')
                return JsonResponse({'message': '令牌错误'})
            if request.method != 'GET':
                body = json.loads(request.body)
                body['account_number'] = parse_token.get('account_number')
                new_body = json.dumps(body).encode('utf-8')
                request._body = new_body
                return None
            else:
                account_number = parse_token.get('account_number')
                # 使用 querydict对象的copy()方法, 获取一个可修改的querydict
                GET_data = request.GET.copy()
                GET_data['account_number'] = account_number
                request.GET = GET_data
                return None


    # 请求达到视图之前
    def process_view(self, request, callback, callback_args, callback_kwargs):
        # print('请求达到路由之前')
        pass

    # 返回响应
    def process_response(self, request, response):
        print('发返回视图')
        return response
