import re

text = input()

patern = r"\b_[a-zA-Z0-9]+\b"
id = re.findall(patern, text)
vid = []

for valid_id in id:
    v_id = valid_id[1:]
    vid.append(v_id)

v_i_d = ",".join(vid)

print(v_i_d)