import re

#if __name__ == "__main__":
s = input()
print(bool(re.match(r'^[1-9][\d]{5}$', s) and len(re.findall(r'(\d)(?=\d\1)',s)) < 2))
print(bool(re.match(r'^[1-9][\d]{5}$', s) and len(re.findall(r'(\d)(?=\d\1)',s)) < 2))