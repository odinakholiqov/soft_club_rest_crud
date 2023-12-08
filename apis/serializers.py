from rest_framework.serializers import ModelSerializer, Serializer, CharField, IntegerField

from .models import Post, Student


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title",)


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


# class StudentListCreateSerializer(ModelSerializer)
#     class Meta:
#         model = Student
#         fields = "__all__"

#         # fields = ("first_name",)

class StudentListCreateSerializer(Serializer):
    id = IntegerField()
    first_name = CharField()
    last_name = CharField()

    def create(self, validated_data):
        student = Student.objects.create(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"])
        
        return student
        # Student.objects.create(**validated_data)

class StudentDetailSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"