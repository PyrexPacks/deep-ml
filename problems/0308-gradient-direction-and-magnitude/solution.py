import numpy as np

def gradient_direction_magnitude(g: list) -> dict:
	g = np.asarray(g, dtype=float)
	magnitude = float(np.linalg.norm(g))
	if magnitude == 0:
		direction= np.zeros_like(g)
	else:
		direction = g/magnitude
	descent_direction = np.negative(direction)
	return {
	'magnitude' : magnitude,
	'direction' : direction, 
	'descent_direction' : descent_direction}

