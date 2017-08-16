from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model details
    """
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name', 'last_name',
                  'user_type')
        read_only_fields = ('email',)