from collections import Counter
with open("open-the-file-where-the-paragrapher-exist.txt","r") as file:
    reading = file.read().split() #split() use to separately count words in a given string
new = Counter(reading)
new_sorted_list = sorted(new.items(), key= lambda x:x[1],reverse=True)
rule = []
save = 0
for w,c in new_sorted_list:
        if save < 20:
             rule.append((w,c))
             save += 1
with open("Enter-your-file-name.txt","w") as new_file:
      new_file_ = new_file.write(str(rule))