# 形参**user_info中的两个星号让Python创建一个名为user_info的空字典
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert','einstein',location='princeton',field = 'physics')

print(user_profile)

