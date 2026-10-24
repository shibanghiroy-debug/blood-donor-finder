import csv
can_recieve_from={
    "A+": ["A+","A-","O+","O-"],
    "A-": ["A-","O-"],
    "B+": ["B+","B-","O+","O-"],
    "B-": ["B-","O-"],
    "AB+": ["A+","A-","B+","B-","O+","O-","AB+","AB-",],
    "AB-": ["A-","B-","AB-","O-"],
    "O+": ["O+","O-"],
    "O-": ["O-"]}
def check_eligibility(age,weight,recent_donation):
    reasons=[]
    if not(18<=age<=65):
        reasons.append("Age must be between 18 and 65")
    if weight<50:
        reasons.append("Weight must be atleast 50 kg")
    if recent_donation.lower()=="yes":
        reasons.append("Cannot donate if donated in last 3 months")
    return reasons
def donate_blood():
    print("\n---Donor Registration---")
    name=str(input("Name: "))
    blood_group=str(input("Blood Group: ")).strip().upper()
    try:
        age=int(input("Age: "))
        weight=float(input("Weight(Kg): "))
    except ValueError:
        print("Invalid number entered")
        return
    location=str(input("Location: "))
    contact=input("Contact number: ")
    if len(contact)!= 10:
        print("Invalid Entry")
    recent=input("Donated in last 3 months?(yes/no): ")
    reasons=check_eligibility(age,weight,recent)
    if reasons:
        print("Rejected:",",".join(reasons))
    else:
        with open("donors.csv","a") as f:
            csv.writer(f).writerow([name,blood_group,location,contact])
        print("Successfully registered as a donor!")
def need_blood():
    print("\n---Request Donation---")
    name=str(input("Name: "))
    blood_group=str(input("Blood Group: ")).strip().upper()
    try:
        age=int(input("Age: "))
    except ValueError:
        print("Invalid number entered")
    location=str(input("Location: "))
    contact=input("Contact number: ")
    if len(contact)!=10:
        print("Invalid Entry")
        contact=input("Enter again")
    if blood_group in can_recieve_from[blood_group]:
        matches=can_recieve_from[blood_group]
        print("Required blood groups are: ",can_recieve_from[blood_group])
        flag=0
        with open("donors.csv","r",newline="") as f:
            for r in csv.reader(f):
              if len(r)>1 and r[1] in matches:
               flag=1
               if r[2]==location:
                   print("Matches in same city: ",{r})
               else:
                    print("Showing matches from different cities:")
                    print("Match= ",{r[0]},"Contact= ",{r[3]})
        if flag==0:
          print("No match found yet")
while True:
    print("\n---Blood Donor System---")
    print("1. Need Blood")
    print("2. Donate Blood")
    print("3. Exit")
    choice=int(input("Enter Choice(1-3): "))
    if choice==1:
        need_blood()
    elif choice==2:
        donate_blood()
    elif choice==3:
        print("Exiting Program")
        break
    else:
        print("Invalid input")
    
