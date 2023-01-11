class UserInfo(object):
    lv = 5
    
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account
    
    def get_account(self):
        return self.__account
    
    @classmethod
    def get_name(cls):
        return cls.lv
    
    @property
    def get_age(self):
        return self._age


class UserInfo2(UserInfo):
    pass


class UserInfo3(UserInfo):
    if __name__ == '__main__':
        userInfo2 = UserInfo2('Jack', 18, 333333)
        print(userInfo2.get_account())

