def solution(area):
  squares = []
  solar_panel = []
  for i in range(2, int(area**0.5)+1):
    square = i**2
    squares.append(square)
  squares.reverse()
  squares.append(4)
  for j in range(3):
    squares.append(1)
  for k in squares:
    if k <= area:
      solar_panel.append(k)
      area -= k
    elif area == 0:
      break
  return solar_panel

print (solution(int(input("Choose a number: "))))