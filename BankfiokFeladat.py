class Bank:
    def __init__(self):
        self.bankname = []
        self.bankoffices = []
        
    def add_new_bank(self, name, headquarters):
        self.bankname.append([name, headquarters])
        self.bankoffices.append([name, []])
        print(f"Új bank hozzáadva: {name}")

                
    def add_bankoffices(self, bank_name, office_name):
        for bank in self.bankoffices:
            if bank[0] == bank_name:
                bank[1].append(office_name)
                print(f"Új bankfiók hozzáadva a(z) {bank_name} bankhoz: {office_name}\n")
                return  
            
        print(f"A(z) {bank_name} bank nem található.\n")
  
                 
    def del_bankoffices(self, bank_name, office_name):
        for bank in self.bankoffices:
            if bank[0] == bank_name:
                if office_name in bank[1]:
                    bank[1].remove(office_name)
                    print(f"A(z) {office_name} bankfiók törölve a(z) {bank_name} bankból.\n")
                    return     

        print(f"A(z) {office_name} bankfiók nem található a(z) {bank_name} bankban.\n")


    def list_bankoffices(self, bank_name):
        for bank in self.bankoffices:
            if bank[0] == bank_name:
                print(f"{bank_name} bankfiókjai: {bank[1]}")
                return

        print(f"A(z) {bank_name} bank nem található.\n")


class Customer:
    def __init__(self):
        self.customers = []

    def last_cust_id(self):
        if len(self.customers) == 0:
            return 1 
        else:
            last_customer = self.customers[-1]
            return last_customer.get("id", 1) + 1
        
    print(f"\n")

    def add_customer(self, name, email):
        new_customer = {"id": self.last_cust_id(), "name": name, "email": email}
        self.customers.append(new_customer)
        print(f"Új felhasználó hozzáadva: {name}, {email}\n")

    
    def list_customer(self):
        if len(self.customers) == 0:
            print(f"Nincsenek még felhasználók.\n")
        else:
            print(f"Felhasználók listája:\n")
            for customer in self.customers:
                print(f"Azonosító: {customer['id']}, Név: {customer['name']}, Email: {customer['email']}\n")

    
    def delete_customer(self, customer_id):
        for customer in self.customers:
            if customer['id'] == customer_id:
                self.customers.remove(customer)
                print(f"Az ügyfél azonosítóval {customer_id} törölve.\n")
                return

        print(f"Nem található ügyfél azonosítóval {customer_id}.\n")
 

def main():
    customer = Customer()
    bank = Bank()

def main():
    customer = Customer()
    bank = Bank()

    print(f"\n")
    while True:
        print("Válassz a következő lehetőségek közül:")
        print("1 - Új bank felvétele")
        print("2 - Új bankfiók felvétele")
        print("3 - Bankfiókok listázása")
        print("4 - Bankfiók törlése")
        print("5 - Ügyfél felvétele")
        print("6 - Ügyfél listázása")
        print("7 - Ügyfél törlése")
        print("e - Kilépés")

        choice = input("Add meg a kívánt művelet betűjelét: \n")

        
        if choice == "1":
            print("Új bank felvétele \n")
            name = input("Add meg az új bank nevét: ")
            headquarters = input("Add meg a bank székhelyét: \n")
            bank.add_new_bank(name, headquarters)
            print

        elif choice == "2":
            print("Új bankfiók felvétele \n")
            bank_name = input("Add meg a bank nevét: ")
            office_name = input("Add meg az új bankfiók nevét: \n")
            bank.add_bankoffices(bank_name, office_name)
            print
            
        elif choice == "3":
            print("Bankfiókok listázása\n")
            bank_name = input("Add meg a bank nevét: \n")
            bank.list_bankoffices(bank_name)
            print
            
        elif choice == "4":
            print("Bankfiók törlése\n")
            bank_name = input("Add meg a bank nevét: ")
            office_name = input("Add meg a bankfiók nevét: \n")
            bank.del_bankoffices(bank_name, office_name)
            print
            
        elif choice == "5":
            print("Ügyfél felvétele\n")
            name = input("Add meg az új felhasználó nevét: ")
            email = input("Add meg az új felhasználó email címét: \n")
            customer.add_customer(name, email)
            print
            
            
        elif choice == "6":
            print("Ügyfél listázása\n")
            customer.list_customer()
            print
            
        elif choice == "7":
            print("Ügyfél törlése")
            customer_id = int(input(f"Add meg az ügyfél azonosítóját, amit törölni szeretnél: \n"))
            customer.delete_customer(customer_id)
            print
            
        elif choice == "e":
            print("Kilépés a főmenübe...\n")
            print
            break
        
        
        else:
            print(f"Nem megfelelő választás, kérlek válassz a menüpontok közül!\n")

if __name__ == "__main__":
    main()




 





