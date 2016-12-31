
fruit =['apple','pears','mango','kiwi','apple','pears','grape','mango']

def analyse_fruit(l):
  counts = {}
  for item in l:
    if item in counts:
      counts[item] = counts[item]+1
    else:
      counts[item]=1
  return counts

counts1 = analyse_fruit(fruit)

print counts1

