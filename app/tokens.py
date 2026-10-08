from rest_framework_simplejwt.tokens import RefreshToken

class MyToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)        # 1. build the normal token
        token['username'] = user.username     # 2. add your own data
        token['email'] = user.email
        token['first_name'] = user.first_name
        return token