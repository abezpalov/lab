s100 = set(range(100))
print(s100)

all_sets = set([])
print(all_sets)

for i in range(100):
    for s in all_sets:
        print(s)
        if len(s) < 3:
            s = set(s)
            s.add(i)
            all_sets.add(frozenset(s))
    print(f'{i}: {len(all_sets)}')

