from rest_framework import serializers
from .models import Materiel


# required 必须传
class Materiel_serializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, required=False)
    add_name = serializers.CharField(max_length=200)
    cargo_name = serializers.CharField(max_length=30)
    cargo_info = serializers.JSONField(default=list)
    add_time = serializers.DateTimeField(allow_null=True)
    # 进货对象
    merchant = serializers.CharField(max_length=50, allow_blank=True)
    # 入库数量
    quantity_in_storage = serializers.IntegerField(default=0)
    # 使用数量
    quantity_used = serializers.IntegerField(default=0)
    # 出库数量
    outbound_quantity = serializers.IntegerField(default=0)
    # 损耗数量
    loss_quantity = serializers.IntegerField(default=0)
    # 库存数量
    available_quantity = serializers.IntegerField(default=0)
    # 备注
    remark = serializers.CharField(max_length=200, allow_blank=True, required=False)

    def validate(self, attrs):
        print('验证字段', attrs)
        return attrs

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance,key,value)
        instance.save()
        return instance

    def create(self, validated_data):
        # 调用save方法会自动调用create方法
        print('保存')
        # 字典的key要更函数参数名保持一致才可以传参 如**validated_data
        diary = Materiel.objects.create(**validated_data)
        return diary