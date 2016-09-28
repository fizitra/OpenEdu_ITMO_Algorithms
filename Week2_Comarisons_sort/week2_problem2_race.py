with open('race.in', 'r', encoding='utf-8') as race:
    dict_race = {}
    for line in race:
        l = line.strip().split()
        if len(l) > 1:
            dict_race.setdefault(l[0],[]).append(l[1])
f = open('race.out','a')

for country in sorted(list(dict_race)):
    print("=== "+country+" ===", file=f)
    for man in dict_race[country]:
        print(man, file=f)
f.close()