#Depth First Search using Stack and Set data structures
adc_List = {0:[1,2],1:[2],2:[0,3],3:[3]}
visited_set = set()
check_stack = [0]

while len(check_stack)!=0:
  this_item = check_stack.pop()
  print this_item
  visited_set.add(this_item)
  listItems = adc_List[this_item]
  for item in listItems:
    if item not in visited_set:
      check_stack.append(item)



