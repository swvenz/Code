zzz_dict = {
    "name": ['Lycaon', 'Belle'],
    "age": [36, 25], 
    "Occupation": ["Victoria Housekeeping", "Proxy"]
    }

# Accessing values
print(zzz_dict["name"])
print(zzz_dict["name"][1])

# Adding a new value to an existing list
zzz_dict["name"].append("Wise")
print(zzz_dict["name"])


# from collections import defaultdict
# zzz_dict["name"][1] = defaultdict(list)
# zzz_dict["name"].append("Banyue")
# zzz_dict["name"].append("Zhao")
# zzz_dict["name"].append("Dialyn")
# zzz_dict["age"].append(28)
# print(zzz_dict)