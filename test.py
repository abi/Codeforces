str1 = str(raw_input())
str2 = str(raw_input())
str3 = str(raw_input())
import itertools

# str1 = "abcd"
# str2 = "bc"
# str3 = "dd"
strings = [str1, str2, str3]

def largest_start_seq(x, y):
  i = 0
  y = y[::-1]
  while i < len(x) and i < len(y):
    if x[i] != y[i]:
      break
    i += 1
    #print i
  return  y[i:][::-1] + x
  
def find_best_substr(a, b):
  if a in b:
    return b
  if b in a:
    return a
  
  front = largest_start_seq(a, b)
  back = largest_start_seq(b, a)
    
  if len(front) > len(back):
    return back
  else:
    return front
  
lengths = []

def find_bestbest(strings):
  best = find_best_substr(strings[0], strings[1])
  bestbest = find_best_substr(best, strings[2])
  #print bestbest
  return len(bestbest)
  
for i in itertools.permutations(strings):
  lengths.append(find_bestbest(i))
  
#print lengths
#print bestbest
print min(lengths)