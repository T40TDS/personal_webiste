number_with_exactly_one = 0
number_not_with_exactly_one = 0

for i in range(0,100000):
  lst = []
  for k in range(0,500):
    lst = lst.append(random.randint(1, 365))
  
  true_count = 0
  for j in range(0,500):
    if lst[j] == 10:
      true_count = true_count + 1
  
  if true_count == 1:
    number_with_exactly_one = number_with_exactly_one + 1
  else:
    number_not_with_exactly_one = number_not_with_exactly_one + 1