# A set:
#   1. unordered
#   2. mutable
#   3. unique values only
#   4. it uses hash tables for very fast lookupsand insertions.


categories = ["electronics","electronics","furniture","furniture","clothing","electronics"]

categories_set = set(categories)

categories_set.add("toys")
categories_set.add("electronics")
print("sports" in categories_set)
print("electronics" in categories_set)
print(categories_set)



# uses
# 1. remove duplicates
# 2. fast searching
# 3. tags/categories