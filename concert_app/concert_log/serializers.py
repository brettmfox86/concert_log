from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from concert_app.concert_log.models import Profile, UserConcert
from rest_framework import serializers


# **************************************** USER SERIALIZERS ****************************************#
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_photo', 'birth_date', 'location')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'profile')

    def create(self, validated_data):
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )

        profile = Profile(
            profile_photo=validated_data['profile']['profile_photo'],
            birth_date=validated_data['profile']['birth_date'],
            location=validated_data['profile']['location']
        )

        user.save()
        profile.user = user
        profile.save()
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.username = validated_data['username']
        instance.email = validated_data['email']

        try:
            profile = Profile.objects.get(user=instance)
        except ObjectDoesNotExist:
            profile = Profile.objects.create(user=instance)

        profile.profile_photo = validated_data['profile']['profile_photo']
        profile.birth_date = validated_data['profile']['birth_date']
        profile.location = validated_data['profile']['location']

        profile.save()
        instance.save()
        return instance


# **************************************** USER CONCERT SERIALIZERS ****************************************#
class UserConcertSerializer(serializers.ModelSerializer):
    username = serializers.StringRelatedField(source='user.username', read_only=True)
    first_name = serializers.StringRelatedField(source='user.first_name', read_only=True)
    last_name = serializers.StringRelatedField(source='user.last_name', read_only=True)
    email = serializers.StringRelatedField(source='user.email', read_only=True)

    class Meta:
        model = UserConcert
        fields = ('concert_id', 'user', 'username', 'first_name', 'last_name', 'email')
