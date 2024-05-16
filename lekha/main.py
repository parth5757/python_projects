# import tkinter as tk
# from tkinter import ttk, messagebox, filedialog
# import sqlite3
# from PIL import Image, ImageTk

# class InventoryApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Inventory Management System")
        
#         # Create a database connection
#         self.conn = sqlite3.connect('inventory.db')
#         self.c = self.conn.cursor()
        
#         # Create tables if not exists
#         self.create_tables()
        
#         # Create the main frame
#         self.main_frame = ttk.Frame(root)
#         self.main_frame.pack(padx=20, pady=20)
        
#         # Create widgets
#         self.inventory_label = ttk.Label(self.main_frame, text="Inventory Management System", font=('Helvetica', 18))
#         self.inventory_label.grid(row=0, column=0, columnspan=4)
        
#         self.inventory_tree = ttk.Treeview(self.main_frame, columns=("ID", "Product", "Quantity", "Price"))
#         self.inventory_tree.heading("#0", text="", anchor=tk.W)
#         self.inventory_tree.heading("ID", text="ID")
#         self.inventory_tree.heading("Product", text="Product")
#         self.inventory_tree.heading("Quantity", text="Quantity")
#         self.inventory_tree.heading("Price", text="Price")
#         self.inventory_tree.grid(row=1, column=0, columnspan=4)
        
#         self.add_button = ttk.Button(self.main_frame, text="Add Product", command=self.add_product_window)
#         self.add_button.grid(row=2, column=0, padx=5, pady=5)
        
#         self.edit_button = ttk.Button(self.main_frame, text="Edit Product", command=self.edit_product_window)
#         self.edit_button.grid(row=2, column=1, padx=5, pady=5)
        
#         self.sell_button = ttk.Button(self.main_frame, text="Sell Product", command=self.sell_product_window)
#         self.sell_button.grid(row=2, column=2, padx=5, pady=5)
        
#         self.report_button = ttk.Button(self.main_frame, text="Generate Report", command=self.generate_report)
#         self.report_button.grid(row=2, column=3, padx=5, pady=5)
        
#         # Load inventory data
#         self.load_inventory()
    
#     def create_tables(self):
#         # Create inventory table if not exists
#         self.c.execute('''CREATE TABLE IF NOT EXISTS inventory
#                           (id INTEGER PRIMARY KEY, product TEXT, quantity INTEGER, price REAL)''')
        
#         # Create purchase table if not exists
#         self.c.execute('''CREATE TABLE IF NOT EXISTS purchases
#                           (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, total_price REAL)''')
        
#         # Create sales table if not exists
#         self.c.execute('''CREATE TABLE IF NOT EXISTS sales
#                           (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, total_price REAL)''')
    
#     def load_inventory(self):
#         # Clear existing data
#         for row in self.inventory_tree.get_children():
#             self.inventory_tree.delete(row)
        
#         # Fetch inventory data from the database
#         self.c.execute("SELECT * FROM inventory")
#         rows = self.c.fetchall()
        
#         # Populate the Treeview with inventory data
#         for row in rows:
#             self.inventory_tree.insert("", "end", values=row)
    
#     def add_product_window(self):
#         # Create a new window for adding a product
#         self.add_product_window = tk.Toplevel(self.root)
#         self.add_product_window.title("Add Product")
        
#         # Create labels and entry fields
#         ttk.Label(self.add_product_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
#         self.product_name_entry = ttk.Entry(self.add_product_window)
#         self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
#         ttk.Label(self.add_product_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
#         self.quantity_entry = ttk.Entry(self.add_product_window)
#         self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
#         ttk.Label(self.add_product_window, text="Price:").grid(row=2, column=0, padx=5, pady=5)
#         self.price_entry = ttk.Entry(self.add_product_window)
#         self.price_entry.grid(row=2, column=1, padx=5, pady=5)
        
#         ttk.Label(self.add_product_window, text="Image:").grid(row=3, column=0, padx=5, pady=5)
#         self.image_entry = ttk.Entry(self.add_product_window, state='readonly')
#         self.image_entry.grid(row=3, column=1, padx=5, pady=5)
#         ttk.Button(self.add_product_window, text="Browse", command=self.browse_image).grid(row=3, column=2, padx=5, pady=5)
        
#         ttk.Button(self.add_product_window, text="Add", command=self.add_product).grid(row=4, column=0, columnspan=3, padx=5, pady=5)
    
#     def browse_image(self):
#         filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
#         self.image_entry.configure(state='normal')
#         self.image_entry.delete(0, tk.END)
#         self.image_entry.insert(0, filename)
#         self.image_entry.configure(state='readonly')
    
#     def add_product(self):
#         # Get product details from entry fields
#         product_name = self.product_name_entry.get()
#         quantity = self.quantity_entry.get()
#         price = self.price_entry.get()
#         image_path = self.image_entry.get()
        
#         try:
#             # Insert product into database
#             self.c.execute("INSERT INTO inventory (product, quantity, price, image_path) VALUES (?, ?, ?, ?)",
#                            (product_name, quantity, price, image_path))
#             self.conn.commit()
            
#             # Close add product window
#             self.add_product_window.destroy()
            
#             # Refresh inventory list
#             self.load_inventory()
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to add product: {str(e)}")
    
#     def edit_product_window(self):
#         # Check if a product is selected
#         selected_item = self.inventory_tree.selection()
#         if not selected_item:
#             messagebox.showerror("Error", "Please select a product to edit")
#             return
        
#         # Get product details
#         product_id = self.inventory_tree.item(selected_item, 'values')[0]
#         product_name = self.inventory_tree.item(selected_item, 'values')[1]
#         quantity = self.inventory_tree.item(selected_item, 'values')[2]
#         price = self.inventory_tree.item(selected_item, 'values')[3]
        
#         # Create a new window for editing a product
#         self.edit_product_window = tk.Toplevel(self.root)
#         self.edit_product_window.title("Edit Product")
        
#         # Create labels and entry fields
#         ttk.Label(self.edit_product_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
#         self.product_name_entry = ttk.Entry(self.edit_product_window)
#         self.product_name_entry.insert(0, product_name)
#         self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
#         ttk.Label(self.edit_product_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
#         self.quantity_entry = ttk.Entry(self.edit_product_window)
#         self.quantity_entry.insert(0, quantity)
#         self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
#         ttk.Label(self.edit_product_window, text="Price:").grid(row=2, column=0, padx=5, pady=5)
#         self.price_entry = ttk.Entry(self.edit_product_window)
#         self.price_entry.insert(0, price)
#         self.price_entry.grid(row=2, column=1, padx=5, pady=5)
        
#         ttk.Button(self.edit_product_window, text="Update", command=lambda: self.update_product(product_id)).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
#     def update_product(self, product_id):
#         # Get updated product details from entry fields
#         product_name = self.product_name_entry.get()
#         quantity = self.quantity_entry.get()
#         price = self.price_entry.get()
        
#         try:
#             # Update product in database
#             self.c.execute("UPDATE inventory SET product=?, quantity=?, price=? WHERE id=?",
#                            (product_name, quantity, price, product_id))
#             self.conn.commit()
            
#             # Close edit product window
#             self.edit_product_window.destroy()
            
#             # Refresh inventory list
#             self.load_inventory()
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to update product: {str(e)}")
    
#     def sell_product_window(self):
#         # Create a new window for selling a product
#         self.sell_product_window = tk.Toplevel(self.root)
#         self.sell_product_window.title("Sell Product")
        
#         # Create labels and entry fields
#         ttk.Label(self.sell_product_window, text="Product ID:").grid(row=0, column=0, padx=5, pady=5)
#         self.product_id_entry = ttk.Entry(self.sell_product_window)
#         self.product_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
#         ttk.Label(self.sell_product_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
#         self.sell_quantity_entry = ttk.Entry(self.sell_product_window)
#         self.sell_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
#         ttk.Button(self.sell_product_window, text="Sell", command=self.sell_product).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
#     def sell_product(self):
#         # Get product details from entry fields
#         product_id = self.product_id_entry.get()
#         sell_quantity = self.sell_quantity_entry.get()
        
#         try:
#             # Fetch product details from the database
#             self.c.execute("SELECT * FROM inventory WHERE id=?", (product_id,))
#             product = self.c.fetchone()
            
#             if product:
#                 product_name = product[1]
#                 current_quantity = product[2]
#                 price = product[3]
                
#                 # Check if sufficient quantity is available
#                 if int(sell_quantity) <= current_quantity:
#                     # Calculate total price
#                     total_price = int(sell_quantity) * price
                    
#                     # Update inventory quantity
#                     new_quantity = current_quantity - int(sell_quantity)
#                     self.c.execute("UPDATE inventory SET quantity=? WHERE id=?", (new_quantity, product_id))
#                     self.conn.commit()
                    
#                     # Record sale in sales table
#                     self.c.execute("INSERT INTO sales (product_id, quantity, total_price) VALUES (?, ?, ?)",
#                                    (product_id, sell_quantity, total_price))
#                     self.conn.commit()
                    
#                     # Show success message
#                     messagebox.showinfo("Success", f"{sell_quantity} {product_name} sold for ${total_price}")
                    
#                     # Refresh inventory list
#                     self.load_inventory()
#                 else:
#                     messagebox.showerror("Error", "Insufficient quantity available")
#             else:
#                 messagebox.showerror("Error", "Product not found")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to sell product: {str(e)}")
            
#     def generate_report(self):
#         # Create a new window for generating report
#         self.report_window = tk.Toplevel(self.root)
#         self.report_window.title("Inventory Report")
        
#         # Create Treeview to display report
#         report_tree = ttk.Treeview(self.report_window, columns=("Product", "Quantity Sold", "Total Sales"))
#         report_tree.heading("#0", text="", anchor=tk.W)
#         report_tree.heading("Product", text="Product")
#         report_tree.heading("Quantity Sold", text="Quantity Sold")
#         report_tree.heading("Total Sales", text="Total Sales")
#         report_tree.grid(row=0, column=0)
        
#         # Fetch data from sales table
#         self.c.execute("SELECT product_id, SUM(quantity), SUM(total_price) FROM sales GROUP BY product_id")
#         sales_data = self.c.fetchall()
        
#         # Populate the Treeview with report data
#         for sale in sales_data:
#             product_id = sale[0]
#             quantity_sold = sale[1]
#             total_sales = sale[2]
            
#             # Fetch product name from inventory table
#             self.c.execute("SELECT product FROM inventory WHERE id=?", (product_id,))
#             product_name = self.c.fetchone()[0]
            
#             report_tree.insert("", "end", values=(product_name, quantity_sold, total_sales))
            
#         # Calculate total sales
#         total_sales = sum(sale[2] for sale in sales_data)
#         ttk.Label(self.report_window, text=f"Total Sales: ${total_sales}", font=('Helvetica', 12)).grid(row=1, column=0, padx=5, pady=5)

# # Create the main application window
# root = tk.Tk()
# app = InventoryApp(root)
# root.mainloop()






























import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io
import base64

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        
        # Create a database connection
        self.conn = sqlite3.connect('inventory.db')
        self.c = self.conn.cursor()
        
        # Create tables if not exists
        self.create_tables()
        
        # Create the main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=20, pady=20)
        
        # Create widgets
        self.inventory_label = ttk.Label(self.main_frame, text="Inventory Management System", font=('Helvetica', 18))
        self.inventory_label.grid(row=0, column=0, columnspan=4)
        
        self.inventory_tree = ttk.Treeview(self.main_frame, columns=("ID", "Product", "Quantity", "Price"))
        self.inventory_tree.heading("#0", text="", anchor=tk.W)
        self.inventory_tree.heading("ID", text="ID")
        self.inventory_tree.heading("Product", text="Product")
        self.inventory_tree.heading("Quantity", text="Quantity")
        self.inventory_tree.heading("Price", text="Price")
        self.inventory_tree.grid(row=1, column=0, columnspan=4)
        
        self.add_button = ttk.Button(self.main_frame, text="Add Product", command=self.add_product_window)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.edit_button = ttk.Button(self.main_frame, text="Edit Product", command=self.edit_product_window)
        self.edit_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.sell_button = ttk.Button(self.main_frame, text="Sell Product", command=self.sell_product_window)
        self.sell_button.grid(row=2, column=2, padx=5, pady=5)
        
        self.report_button = ttk.Button(self.main_frame, text="Generate Report", command=self.generate_report)
        self.report_button.grid(row=2, column=3, padx=5, pady=5)
        
        # Load inventory data
        self.load_inventory()
    
    def create_tables(self):
        # Create inventory table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS inventory
                          (id INTEGER PRIMARY KEY, product TEXT, quantity INTEGER, price REAL)''')
        
        # Create purchase table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS purchases
                          (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, total_price REAL)''')
        
        # Create sales table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS sales
                          (id INTEGER PRIMARY KEY, product_id INTEGER, quantity INTEGER, total_price REAL)''')
    
    def load_inventory(self):
        # Clear existing data
        for row in self.inventory_tree.get_children():
            self.inventory_tree.delete(row)
        
        # Fetch inventory data from the database
        self.c.execute("SELECT * FROM inventory")
        rows = self.c.fetchall()
        
        # Populate the Treeview with inventory data
        for row in rows:
            self.inventory_tree.insert("", "end", values=row)
    
    def add_product_window(self):
        # Create a new window for adding a product
        self.add_product_window = tk.Toplevel(self.root)
        self.add_product_window.title("Add Product")
        
        # Create labels and entry fields
        ttk.Label(self.add_product_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name_entry = ttk.Entry(self.add_product_window)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.add_product_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.add_product_window)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.add_product_window, text="Price:").grid(row=2, column=0, padx=5, pady=5)
        self.price_entry = ttk.Entry(self.add_product_window)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Label(self.add_product_window, text="Image:").grid(row=3, column=0, padx=5, pady=5)
        self.image_entry = ttk.Entry(self.add_product_window, state='readonly')
        self.image_entry.grid(row=3, column=1, padx=5, pady=5)
        ttk.Button(self.add_product_window, text="Browse", command=self.browse_image).grid(row=3, column=2, padx=5, pady=5)
        
        ttk.Button(self.add_product_window, text="Add", command=self.add_product).grid(row=4, column=0, columnspan=3, padx=5, pady=5)
    
    def browse_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        self.image_entry.configure(state='normal')
        self.image_entry.delete(0, tk.END)
        self.image_entry.insert(0, filename)
        self.image_entry.configure(state='readonly')
    
    def add_product(self):
        # Get product details from entry fields
        product_name = self.product_name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        image_path = self.image_entry.get()
        
        try:
            # Insert product into database
            self.c.execute("INSERT INTO inventory (product, quantity, price, image_path) VALUES (?, ?, ?, ?)",
                           (product_name, quantity, price, image_path))
            self.conn.commit()
            
            # Close add product window
            self.add_product_window.destroy()
            
            # Refresh inventory list
            self.load_inventory()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add product: {str(e)}")
    
    def edit_product_window(self):
        # Check if a product is selected
        selected_item = self.inventory_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a product to edit")
            return
        
        # Get product details
        product_id = self.inventory_tree.item(selected_item, 'values')[0]
        product_name = self.inventory_tree.item(selected_item, 'values')[1]
        quantity = self.inventory_tree.item(selected_item, 'values')[2]
        price = self.inventory_tree.item(selected_item, 'values')[3]
        
        # Create a new window for editing a product
        self.edit_product_window = tk.Toplevel(self.root)
        self.edit_product_window.title("Edit Product")
        
        # Create labels and entry fields
        ttk.Label(self.edit_product_window, text="Product Name:").grid(row=0, column=0, padx=5, pady=5)
        self.product_name_entry = ttk.Entry(self.edit_product_window)
        self.product_name_entry.insert(0, product_name)
        self.product_name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.edit_product_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.quantity_entry = ttk.Entry(self.edit_product_window)
        self.quantity_entry.insert(0, quantity)
        self.quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(self.edit_product_window, text="Price:").grid(row=2, column=0, padx=5, pady=5)
        self.price_entry = ttk.Entry(self.edit_product_window)
        self.price_entry.insert(0, price)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(self.edit_product_window, text="Update", command=lambda: self.update_product(product_id)).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    
    def update_product(self, product_id):
        # Get updated product details from entry fields
        product_name = self.product_name_entry.get()
        quantity = self.quantity_entry.get()
        price = self.price_entry.get()
        
        try:
            # Update product in database
            self.c.execute("UPDATE inventory SET product=?, quantity=?, price=? WHERE id=?",
                           (product_name, quantity, price, product_id))
            self.conn.commit()
            
            # Close edit product window
            self.edit_product_window.destroy()
            
            # Refresh inventory list
            self.load_inventory()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update product: {str(e)}")
    
    def sell_product_window(self):
        # Create a new window for selling a product
        self.sell_product_window = tk.Toplevel(self.root)
        self.sell_product_window.title("Sell Product")
        
        # Create labels and entry fields
        ttk.Label(self.sell_product_window, text="Product ID:").grid(row=0, column=0, padx=5, pady=5)
        self.product_id_entry = ttk.Entry(self.sell_product_window)
        self.product_id_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.sell_product_window, text="Quantity:").grid(row=1, column=0, padx=5, pady=5)
        self.sell_quantity_entry = ttk.Entry(self.sell_product_window)
        self.sell_quantity_entry.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Button(self.sell_product_window, text="Sell", command=self.sell_product).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    
    def sell_product(self):
        # Get product details from entry fields
        product_id = self.product_id_entry.get()
        sell_quantity = self.sell_quantity_entry.get()
        
        try:
            # Fetch product details from the database
            self.c.execute("SELECT * FROM inventory WHERE id=?", (product_id,))
            product = self.c.fetchone()
            
            if product:
                product_name = product[1]
                current_quantity = product[2]
                price = product[3]
                
                # Check if sufficient quantity is available
                if int(sell_quantity) <= current_quantity:
                    # Calculate total price
                    total_price = int(sell_quantity) * price
                    
                    # Update inventory quantity
                    new_quantity = current_quantity - int(sell_quantity)
                    self.c.execute("UPDATE inventory SET quantity=? WHERE id=?", (new_quantity, product_id))
                    self.conn.commit()
                    
                    # Record sale in sales table
                    self.c.execute("INSERT INTO sales (product_id, quantity, total_price) VALUES (?, ?, ?)",
                                   (product_id, sell_quantity, total_price))
                    self.conn.commit()
                    
                    # Show success message
                    messagebox.showinfo("Success", f"{sell_quantity} {product_name} sold for ${total_price}")
                    
                    # Refresh inventory list
                    self.load_inventory()
                else:
                    messagebox.showerror("Error", "Insufficient quantity available")
            else:
                messagebox.showerror("Error", "Product not found")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to sell product: {str(e)}")
            
    def generate_report(self):
        # Create a new window for generating report
        self.report_window = tk.Toplevel(self.root)
        self.report_window.title("Inventory Report")
        
        # Create Treeview to display report
        self.report_tree = ttk.Treeview(self.report_window, columns=("ID", "Product", "Quantity", "Total Price"), show="headings")
        self.report_tree.heading("ID", text="ID")
        self.report_tree.heading("Product", text="Product")
        self.report_tree.heading("Quantity", text="Quantity")
        self.report_tree.heading("Total Price", text="Total Price")
        self.report_tree.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Fetch sales data from the database
        self.c.execute("SELECT * FROM sales")
        sales_data = self.c.fetchall()
        
        # Populate the Treeview with sales data
        for sale in sales_data:
            self.report_tree.insert("", "end", values=sale)
        
        # Prepare to generate a chart
        products = []
        quantities_sold = []
        total_sales = []

        for sale in sales_data:
            product_id = sale[0]
            quantity_sold = sale[1]
            total_sales.append(sale[2])

            # Fetch product name from inventory table
            self.c.execute("SELECT product FROM inventory WHERE id=?", (product_id,))
            product_name = self.c.fetchone()[0]

            products.append(product_name)
            quantities_sold.append(quantity_sold)

        # Generate a bar chart using Matplotlib
        fig, ax = plt.subplots()
        ax.bar(products, quantities_sold)
        ax.set_ylabel('Quantity Sold')
        ax.set_title('Sales Report')

        # Convert the plot to PNG
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img = Image.open(buf)
        img = img.convert('RGB')
        photo = ImageTk.PhotoImage(img)

        # Display the chart in a Toplevel window
        self.chart_window = tk.Toplevel(self.report_window)
        self.chart_window.title("Sales Chart")

        chart_label = ttk.Label(self.chart_window, image=photo)
        chart_label.image = photo  # Keep a reference to avoid garbage collection
        chart_label.pack()

        # Optionally, close the chart window after a delay
        self.chart_window.after(5000, lambda: self.chart_window.destroy())


# Create the main application window
root = tk.Tk()
app = InventoryApp(root)
root.mainloop()
