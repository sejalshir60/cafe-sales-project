menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 80
}

orders = {}

n = int(input("Enter number of orders: "))

for i in range(n):
    item = input("Enter item name: ")
    qty = int(input("Enter quantity: "))

    if item in menu:
        orders[item] = orders.get(item, 0) + qty
    else:
        print("Item not available")

with open("report.html", "w") as file:
    file.write("""
    <html>
    <head>
        <title>Cafe Sales Report</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Cafe Sales Report</h1>
        <table border="1" cellpadding="5">
            <tr>
                <th>Item</th>
                <th>Quantity</th>
                <th>Total Price</th>
            </tr>
    """)

    for item, qty in orders.items():
        file.write(f"""
            <tr>
                <td>{item}</td>
                <td>{qty}</td>
                <td>{qty * menu[item]}</td>
            </tr>
        """)

    file.write("""
        </table>
    </body>
    </html>
    """)

print("✅ Report generated successfully")
