#Author: Karthik Madhav Jain kmj5614@psu.edu
#Section: 003R
#Collaborators & Breakout Room: I was unable to access my public repl and thus was not able to write the breakout room# and collaborators' information. The same is available in my lab10 repl as I had pushed this information on it.

def remove_duplicate_sorted(t):
  ordered = list(set(t))
  return (sorted(ordered))

def list_to_dictionary(t):
  dictionary = {}
  for i in t:
    n = len(i)
    if n not in dictionary:
      dictionary[n]=[i]
    else:
      dictionary[n].append(i)
  return dictionary

def run():
  t = []
  inputted = input("Enter a string:")
  while(inputted != "done"):
    t.append(inputted)
    inputted = input("Enter a string:")
  print("List: ",t)
  print("Sorted List: ",remove_duplicate_sorted(t))
  print("Dictionary: ",list_to_dictionary(t))

if __name__ == "__main__":
  run()



