# Read about the Tower of Hanoi algorithm. Write a program to implement it

def Tower_Of_Hanoi(n, from_rod, to_rod, aux_rod):
	if n == 0:
		return
	Tower_Of_Hanoi(n-1, from_rod, aux_rod, to_rod)
	print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
	Tower_Of_Hanoi(n-1, aux_rod, to_rod, from_rod)
N = 3
Tower_Of_Hanoi(N, 'A', 'C', 'B')
