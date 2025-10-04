import numpy as np

gen = np.random.default_rng(seed=None)

print(gen)

result = gen.normal(loc=4.5, scale=2.0, size=(1,5))

print(result)
rounded = [round(r, 2) for r in result[0]]
print(rounded)

print(np.mean(rounded))
