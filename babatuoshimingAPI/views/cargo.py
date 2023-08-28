from rest_framework.views import Response, APIView
import json
import re
import datetime
from ..models import Users
from ..serializersSet import Materiel_serializers, Materiel


class MaterielManage(APIView):
    def get(self, request):
        account_number = request.GET.get('account_number')
        user = Users.objects.filter(account_number=account_number).first()
        if user:
            status = user.status
            # 超级管理员身份 需要的数据
            if int(status) == 3:
                materiel_model = Materiel.objects.all().order_by('-id')
                materiel = Materiel_serializers(instance=materiel_model, many=True).data
                for i in materiel:
                    i['add_time'] = i['add_time'].replace('T',' ')
                    i['add_name'] = json.loads(i['add_name'])['name']
                return Response({'data': materiel, 'status': 200})

    # 添加货物类名
    def post(self, request):
        data = json.loads(request.body)
        add_time = data.get('add_time')
        # 前端已经格式化时间
        # # 13位转成10位
        # timestamp = int(int(add_time) / 1000)
        # # 时间戳转成datetime对象
        # dt = datetime.datetime.fromtimestamp(timestamp)
        # add_time = dt.strftime("%Y-%m-%d %H:%M:%S")

        cargo_name = data.get('cargo_name')
        remark = data.get('remark')
        merchant = data.get('merchant')
        add_name = data.get('add_name')
        account_number = data.get('account_number')
        data = {
            'add_name': json.dumps({'account_number': account_number, 'name': add_name}),
            'add_time': add_time,
            'cargo_name': cargo_name,
            'cargo_info': [],
            'merchant': merchant,
            'remark': remark
        }
        materiel = Materiel.objects.filter(cargo_name=cargo_name).first()
        if not materiel:
            materiel_serializers = Materiel_serializers(data=data)
            if materiel_serializers.is_valid():
                materiel_serializers.save()
                return Response({'message': 'ok', 'status': 200})
            else:
                print('错误信息', materiel.errors)
                return Response({'message': '错误'}, status=400)
        else:
            return Response({'message': '类名已经存在'}, status=400)

    def put(self, request):
        print(request.body)
        return Response({'message': '成功'})


materiel = {
    '类别': 'ftf',
    '添加时间': '2023-8-7 7:12:23',
    '入库数量': '12',
    '使用数量': '3',
    '出库数量': '4',
    '损耗数量': '3',
    '仓库库存': '2',
    '添加者': '刘',
    '货物': [
        {'id': 1, '添加时间': '2023-8-7 7:12:23', '状态': '使用', '备注': '', '添加者':'' },
        {'id': 2, '添加时间': '2023-8-7 7:12:23', '状态': '使用', '备注': '', }
    ]
}
