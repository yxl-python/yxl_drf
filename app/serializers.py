from rest_framework import serializers
from app.models import User

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password")

        extra_kwargs = {
            "username":{
                "required":True,
                "error_messages":{
                    "required":"用户名必须提供",
                }
            },
            "password":{
                "required":True,
                "min_length":6,
                "error_messages":{
                    "required":"密码必须提供",
                    "min_length":"密码不能小于6位",
                }
            },
        }
