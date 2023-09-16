rcds = {}

while True:
    choice = input('Enter "1" to Add Data, "2" to Delete Data or "3" to End: ')
    
    if choice == "1":
        key = input("Enter Key: ")
        val = input("Enter Value: ")
        
        rcds[key] = val 
        
        print(f"Added: {key}: {val}")
        
    elif choice == "2":
        key = input("Enter Key to Delete: ")
        
        if key in rcds:
            del rcds[key]
            
            print(f"Deleted: {key}")
        else:
            print("Key is not found in records")
            
    elif choice == "3":
        break
    else:
        print('Invalid choice, Please enter "1", "2", or "3" only')

print()
print("Final Records: ", rcds)
print()
print("THANK YOU!")