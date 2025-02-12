# 1.
user = {
    "first_name":  "Marcin"
}

data = {
    "country": "PL"
}

full_data = user | data

print(full_data)

# 2. - in place
"""
Also possible by operator `|=`
"""
user.update(full_data)
print(user)

# merging with **

second_user = {
    "first_name":  "Marcin"
}

meta_data = {
    "country": "PL"
}

updated_user = {**second_user, **meta_data}

print(updated_user)
