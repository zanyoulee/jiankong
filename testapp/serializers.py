from rest_framework import serializers
from testapp.models import book_zhoudu

class MeiziSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = book_zhoudu
        # 和"__all__"等价
        fields = ('id', 'name', 'author', 'fenlei', 'score','dwlink1','dwlink2','dwlink3')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     try:
    #         data['i_addr'] = instance.studentinfo.i_addr
    #     except:
    #         data['i_addr'] = ''
    #     return data