t = []

for m in range(168):
    for n in range(m):
        if m**2-n**2 == 168:
            x = n**2-100
            t.append(x)

print(t)            
