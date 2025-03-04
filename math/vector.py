from typing import List

Vektor = List[float]

def add(v: Vektor, w: Vektor) -> Vektor:
	assert len(v) == len(w)
	return [v1 + w1 for v1, w1 in zip(v,w)]

def subtract(v: Vektor, w: Vektor) -> Vektor:
	assert len(v) == len(w)
	return [v1 - w1 for v1, w1 in zip(v,w)] 

def vector_sum(vectors: List[Vektor]) -> Vektor:
	assert vectors
	num_elements = len(vectors[0])
	assert all(len(v) == num_elements for v in vectors), "different sizes!"
	return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

def scalar_multiply(x: float, v:Vektor) -> Vektor:
	return [x*v1 for v1 in v]	

def vector_mean(vectors: List[Vektor]) -> Vektor:
	n = len(vectors)
	return scalar_multiply(1/n, vector_sum(vectors))

def dot(v: Vektor, w: Vektor) -> float:
	return [sum(v1*w1 for v1, w1 in zip(v,w))]

v = [1,2,3]
w = [4,5,6]
x = [5,2,2]
y = [1,0,2]


print("Vektoraddition",add(v,w))
print("Vektorsubtraktion",subtract(v,w))
print("Vektorsumme", vector_sum([v,w,x,y]))
print("Skalare Multiplikation",scalar_multiply(5,v))
print("Durchschnitt",vector_mean([v,w,x,y]))
print("Skalarprodukt", dot(v,w))
