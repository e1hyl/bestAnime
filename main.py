import mem
import fav

new_dict_fav = {}
new_dict_mem = {}

new_dict_mem = mem.dict_mem
new_dict_fav = fav.dict_fav

ratio_list = [0] * 50
names_list = [0] * 50
index = 0

for key in new_dict_fav:
    name_found = new_dict_mem.get(key, None)
    if name_found:
        names_list[index] = key
        ratio_list[index] = (int(new_dict_fav[key].replace(",", "")) / int(new_dict_mem[key].replace(",", "")))
        index = index + 1
        
for x in range(17):
    names_list.pop()
    ratio_list.pop()
 
dict_ratio = dict(zip(names_list, ratio_list))

sd = {k: v for k, v in sorted(dict_ratio.items(), key=lambda item: item[1], reverse=True)}

pos = 1
print("   ANIME --- FAVORITES/MEMBERS")
for key, value in sd.items():
    print(pos,") ", key, " ==> ","%.5f" % (value * 100), "%", sep = "")
    pos = pos + 1
    