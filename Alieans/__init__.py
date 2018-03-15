from string import Template
class MyTemplate(Template):
    delimiter = '*'

def Main():
    cart = []
    cart.append(dict(item="Coke",Prize=15,qty=2))
    cart.append(dict(item="Sprite", Prize=10, qty=1))
    cart.append(dict(item="Maza", Prize=20, qty=5))

    t = Template("$qty x $item = $Prize")
    total = 0
    print("Cart:")
    for data in cart :
        print(t.substitute(data))
        total+=data["Prize"]
    print("Total :"+str(total))

if __name__ == "__main__":
    Main()
