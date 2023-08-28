import jwt
from managementSystem.settings import SECRET_KEY
import datetime

expiration_date = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
print(expiration_date)
# # expiry_timestamp = int(expiry_date.timestamp() * 1000)
# print(expiration_date)
# payload = {
#     'id':1,
#     'exp': expiration_date,
# }
# token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm="HS256")
# print(token)
# token2 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZXhwIjoxNjkxMTIyODU2fQ.KJcane7JcVWajme4ivSv-Gjtm5hJjfIxHt-kgdngAKE'
#
#
# jtoken = jwt.decode(token2,SECRET_KEY,algorithms='HS256')
# print(jtoken)


# 状态：使用， 库存， 损耗，出库

materiel = {
    '类别':'ftf',
    '添加时间':'2023-8-7 7:12:23',
    '入库数量':'12',
    '使用数量':'3',
    '出库数量':'4',
    '损耗数量':'3',
    '仓库库存':'2',
    '添加者':'刘',
    '货物':[
        {'id':1, '添加时间': '2023-8-7 7:12:23', '状态':'使用', '备注':'',},
        {'id':2, '添加时间': '2023-8-7 7:12:23', '状态':'使用', '备注':'',}
    ]
}
