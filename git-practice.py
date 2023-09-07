toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):
   removed = "Removed", str(item)
   error = "Error"
   if toDoList.count(item) >= 1:
      toDoList.remove(item)
      return removed
   else:
      return error

active = True
while active == True:
   userAns = input("Do you want to add to your list, delete, or quit? A/D/Q ")
   if userAns == "A":
      item = input("What item do you want to add? ")
      addItem(item)
      print("Added", item)
   elif userAns == "D":
      item = input("What item do you want to delete? ")
      deleteItem(item)
      print("Deleted", item)
   elif userAns == "Q":
      active = False
      break

print(toDoList)
   # while userAns == "A":
   #    item = input("What item do you want to add? ")
   #    addItem(item)
   #    userAns = input("Do you want to add to your list or quit? A/Q ")
   # print(toDoList)


