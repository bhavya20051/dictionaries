#Function that assigns default value to key if key is not in dictionary, also uses.get method of finding keys in dictionary
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id=user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id=user_ids.get("superStackSmash", 100000)
print(stack_id)