from rest_framework.views import Response, APIView
import json
import re
from ..models import Users
from managementSystem.settings import SECRET_KEY
import datetime
import jwt


class UserManagement(APIView):

    def get(self, request):

        pass

    def post(self, request):
        # data = bytes.decode(request.body)
        # json 可以直接转换bytes类型数据
        data = json.loads(request.body)
        usernameSign = data.get('usernameSign')
        account_numberSign = data.get('account_numberSign')
        passwordSign = data.get('passwordSign')
        account_numberLogin = data.get('account_numberLogin')
        passwordLogin = data.get('passwordLogin')

        print(data)
        # 注册请求
        if data.get('type') == 'SignIn':
            if not usernameSign or not account_numberSign or not passwordSign:
                print('无效请求体')
                return Response({'message': '无效个人信息，请重新注册'}, status=500)
            verify = Users.objects.filter(account_number=account_numberSign).first()
            if verify:
                print(verify)
                return Response({'message': '账号已经存在'})
            pattern = r'[^0-9A-Za-z]'
            for i in [account_numberSign, passwordSign]:
                content = re.findall(pattern, i)
                if len(content) > 0:
                    return Response({'message': '注册内容不符合规则'})
            Users.objects.create(username=usernameSign, account_number=account_numberSign, password=passwordSign).save()
            return Response({'status': 200, 'message': '账号注册成功，请等待后台审核通过后方可登录'})
        # 登录请求
        else:
            user = Users.objects.filter(account_number=account_numberLogin,password=passwordLogin).first()
            if user:
                time = 30
                expiration_date = datetime.datetime.utcnow() + datetime.timedelta(minutes=time)
                expiration_timep = datetime.datetime.now()+datetime.timedelta(minutes=time)
                expiration_timep = int(expiration_timep.timestamp()*1000)
                payload = {
                    'account_number': account_numberLogin,
                    'exp': expiration_date,
                }
                token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm="HS256")
                user.__dict__.pop('_state')
                user.__dict__.pop('account_number')
                user.__dict__.pop('password')
                user.__dict__.pop('id')
                return Response({'status': 200, 'token': token, 'expiration_timep':expiration_timep, 'userInfo': user.__dict__})
            else:
                return Response({'message': '账号不存在或者为禁用状态'},status=400)





