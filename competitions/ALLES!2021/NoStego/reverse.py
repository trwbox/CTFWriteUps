ROUNDS = 32
di = 1337
dj = 42
di_values = []
dj_values = []

for k in range(ROUNDS):
    di, dj = (di * di + dj) % 512, (dj * dj + di) % 512
    di_values.append(di)
    dj_values.append(dj)

di_values.reverse()
dj_values.reverse()
print(di_values)
print(dj_values)