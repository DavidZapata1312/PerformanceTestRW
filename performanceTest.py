#initialize list with 5 product predefine
products=[{'name':'Rice','price':1000,'quantity':20},{'name':'Meat','price':8000,'quantity':20},{'name':'Eegs','price':1000,'quantity':20},{'name':'Tomatoes','price':1000,'quantity':20},{'name':'Potatoes','price':1000,'quantity':20}]

#Function to valide if the name exist
def name_exists(name, products):
    for product in products:
        if product["name"].lower() == name.lower():
            return True
    return False

#Add new products to the list "products"
def add_products(name,price,quantity):
    #if the name is in the list, don't add it and return a message
    if name_exists(name, products):
        print(f"A product with the name '{name}' already exists.")
        return
    #If don't exist, create a dictionary whit the information and add it 
    else:
        new_product = {
            "name": name,
            "price": price,
            "quantity": quantity
            }

        products.append(new_product)
        print(f"Product '{name}' added successfully.")

#requests a name and compares it with the "name" keys in the products list
def search_product(name_search,products):
        i=0
        lenght=len(products)
        while i < lenght:
            for product in products:
                if product['name'].lower()==name_search:
                    print(product)
                    break
                else:
                    i+=1
   

def update_price(name_update, new_price):
        #Search for the product and actualize his price
            for product in products:
                if product["name"].lower() == name_update:
                    product["price"] = new_price
                print(f"Price of product '{name_update}' updated to {new_price}.")
                print(product)
                return

def delete_product(product_delete):
        #Search for a product, if it exist delete
        for product in products:
            if product['name'].lower()==product_delete:
                products.remove(product)
                print(products)
                break
            else:
                print(f"There are no products with the name:{product_delete}")
                break

def calculate_total_value():
    #It goes through the list of products, multiplying prices by quantities and adding the results.
    return sum(map(lambda product: product.get("quantity", 0) * product.get("price", 0), products))


def menu():
    #Displays an interactive menu with the available functions
    while True:
        print("\n--- Options Menu ---")
        print("1. Add new product")
        print("2. Search")
        print("3. Delete")
        print("4. Check total value inventory")
        print("5. Update product price")
        print("6. Exit")

        option = input("Select an option (1/2/3/4/5/6): ").strip()

        if option == "1":
            print("\n--- Add new product ---")
            name = input("Product name: ").strip()
            try:
                price = float(input("Product price: "))
                quantity = int(input("Product quantity: "))
            except ValueError:
                print("Invalid price or quantity. Try again.")
                
            if not name:
                print("The name cannot be empty.")
                if price < 0:
                        print("The price cannot be negative.")
                if quantity < 0:
                        print("The quantity cannot be negative.")
            add_products(name, price, quantity)

        elif option == "2":
            print("\n--- Search product ---")
            name_search=input("Product to search: ").strip().lower()
            search_product(name_search, products)
   

        elif option == "3":
            print("\n--- Delete ---")
            product_delete=input("Product to delete: ").strip().lower()
            delete_product(product_delete)

        elif option == "4":
            total=calculate_total_value()
            print(f"total inventory value: {total}")
            

        elif option == "5":
            print("--- Update product price ---")
            name_update=input("Product to change price: ").strip().lower()
            try:
                new_price = float(input("Product price: "))
    
            except ValueError:
                print("Invalid price. Try again.")
                

            if new_price < 0:
                        print("The price cannot be negative.")
            update_price(name_update, new_price)

        elif option == "6":
            print("Goodbye! Inventory updated.")
            break
        
        else:
            print("Invalid option. Try again.")

menu()      





