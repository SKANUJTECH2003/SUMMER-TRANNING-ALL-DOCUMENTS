import json
import os
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox, ttk


class Product(ABC):
    def __init__(self, product_id, name, price, stock, category):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__category = category

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def get_category(self):
        return self.__category

    def set_price(self, price):
        self.__price = price

    def set_stock(self, stock):
        self.__stock = stock

    def reduce_stock(self, qty):
        if qty <= self.__stock:
            self.__stock -= qty
            return True
        return False

    @abstractmethod
    def calculate_discounted_price(self):
        pass

    def to_dict(self):
        return {
            "product_id": self.get_product_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "stock": self.get_stock(),
            "category": self.get_category(),
            "type": self.__class__.__name__,
        }


class Electronics(Product):
    def __init__(self, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock, "Electronics")

    def calculate_discounted_price(self):
        return self.get_price() * 0.90


class Clothing(Product):
    def __init__(self, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock, "Clothing")

    def calculate_discounted_price(self):
        return self.get_price() * 0.80


class Grocery(Product):
    def __init__(self, product_id, name, price, stock):
        super().__init__(product_id, name, price, stock, "Grocery")

    def calculate_discounted_price(self):
        return self.get_price() * 0.95


class ShoppingApp:
    def __init__(self):
        self.users_file = "users.json"
        self.products_file = "products.json"
        self.orders_file = "orders.json"
        self.users = []
        self.products = []
        self.orders = []
        self.current_user = None
        self.cart = []
        self.load_data()

        self.root = tk.Tk()
        self.root.title("Online Shopping Management")
        self.root.geometry("800x550")
        self.root.resizable(False, False)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        self.show_login_screen()
        self.root.mainloop()

    def load_data(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, "r") as f:
                self.users = json.load(f)
        else:
            self.users = []

        if os.path.exists(self.products_file):
            with open(self.products_file, "r") as f:
                self.products = json.load(f)
        else:
            self.products = []

        if os.path.exists(self.orders_file):
            with open(self.orders_file, "r") as f:
                self.orders = json.load(f)
        else:
            self.orders = []

        self.ensure_default_data()

    def save_data(self):
        with open(self.users_file, "w") as f:
            json.dump(self.users, f, indent=2)
        with open(self.products_file, "w") as f:
            json.dump(self.products, f, indent=2)
        with open(self.orders_file, "w") as f:
            json.dump(self.orders, f, indent=2)

    def ensure_default_data(self):
        if not any(user["email"] == "admin@example.com" for user in self.users):
            self.users.append({
                "name": "Admin",
                "email": "admin@example.com",
                "password": "admin123",
                "role": "admin",
            })

        if not self.products:
            self.products.extend([
                {"product_id": "E101", "name": "Laptop", "price": 50000, "stock": 10, "category": "Electronics", "type": "Electronics"},
                {"product_id": "C201", "name": "T-Shirt", "price": 1200, "stock": 20, "category": "Clothing", "type": "Clothing"},
                {"product_id": "G301", "name": "Rice", "price": 800, "stock": 30, "category": "Grocery", "type": "Grocery"},
            ])
            self.save_data()

    def find_user(self, email):
        return next((user for user in self.users if user["email"] == email), None)

    def find_product(self, product_id):
        return next((product for product in self.products if product["product_id"] == product_id), None)

    def make_product_obj(self, data):
        if data["type"] == "Electronics":
            return Electronics(data["product_id"], data["name"], data["price"], data["stock"])
        if data["type"] == "Clothing":
            return Clothing(data["product_id"], data["name"], data["price"], data["stock"])
        return Grocery(data["product_id"], data["name"], data["price"], data["stock"])

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_login_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Online Shopping System", font=("Arial", 20, "bold")).pack(pady=20)

        form = tk.Frame(self.main_frame)
        form.pack(pady=10)

        tk.Label(form, text="Email:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.email_entry = tk.Entry(form, width=35)
        self.email_entry.grid(row=0, column=1, pady=5)

        tk.Label(form, text="Password:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.password_entry = tk.Entry(form, show="*", width=35)
        self.password_entry.grid(row=1, column=1, pady=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Login", width=15, command=self.handle_login).grid(row=0, column=0, padx=8)
        tk.Button(button_frame, text="Sign Up", width=15, command=self.show_signup_screen).grid(row=0, column=1, padx=8)

    def show_signup_screen(self):
        self.clear_frame()
        tk.Label(self.main_frame, text="Create New Account", font=("Arial", 18, "bold")).pack(pady=20)

        form = tk.Frame(self.main_frame)
        form.pack(pady=10)

        tk.Label(form, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.signup_name = tk.Entry(form, width=35)
        self.signup_name.grid(row=0, column=1, pady=5)

        tk.Label(form, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.signup_email = tk.Entry(form, width=35)
        self.signup_email.grid(row=1, column=1, pady=5)

        tk.Label(form, text="Password:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.signup_password = tk.Entry(form, show="*", width=35)
        self.signup_password.grid(row=2, column=1, pady=5)

        tk.Label(form, text="Confirm Password:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.signup_confirm = tk.Entry(form, show="*", width=35)
        self.signup_confirm.grid(row=3, column=1, pady=5)

        button_frame = tk.Frame(self.main_frame)
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Register", width=15, command=self.handle_signup).grid(row=0, column=0, padx=8)
        tk.Button(button_frame, text="Back to Login", width=15, command=self.show_login_screen).grid(row=0, column=1, padx=8)

    def handle_signup(self):
        name = self.signup_name.get().strip()
        email = self.signup_email.get().strip()
        password = self.signup_password.get()
        confirm_password = self.signup_confirm.get()

        if not name or not email or not password:
            messagebox.showwarning("Validation Error", "Please fill all fields.")
            return
        if password != confirm_password:
            messagebox.showwarning("Validation Error", "Passwords do not match.")
            return
        if self.find_user(email):
            messagebox.showwarning("Validation Error", "Email already registered.")
            return

        self.users.append({"name": name, "email": email, "password": password, "role": "customer"})
        self.save_data()
        messagebox.showinfo("Success", "Account created. Please login.")
        self.show_login_screen()

    def handle_login(self):
        email = self.email_entry.get().strip()
        password = self.password_entry.get()
        user = self.find_user(email)

        if not user or user["password"] != password:
            messagebox.showerror("Login Failed", "Invalid email or password.")
            return

        self.current_user = user
        self.cart = []
        if user["role"] == "admin":
            self.show_admin_dashboard()
        else:
            self.show_customer_dashboard()

    def show_admin_dashboard(self):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"Admin Dashboard - {self.current_user['name']}", font=("Arial", 18, "bold")).pack(pady=10)

        frame = tk.Frame(self.main_frame)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        left = tk.Frame(frame)
        left.pack(side="left", fill="both", expand=True, padx=(0, 5))

        tk.Label(left, text="Products", font=("Arial", 14, "bold")).pack(anchor="w")
        self.product_tree = ttk.Treeview(left, columns=("ID", "Name", "Category", "Price", "Stock", "Discount"), show="headings", height=10)
        for col in ("ID", "Name", "Category", "Price", "Stock", "Discount"):
            self.product_tree.heading(col, text=col)
            self.product_tree.column(col, width=100)
        self.product_tree.pack(fill="both", expand=True)
        self.product_tree.bind("<ButtonRelease-1>", self.populate_product_fields)

        right = tk.Frame(frame)
        right.pack(side="right", fill="y", padx=(5, 0))

        tk.Label(right, text="Product Details", font=("Arial", 14, "bold")).pack(anchor="w")
        form = tk.Frame(right)
        form.pack(pady=5)

        tk.Label(form, text="ID:").grid(row=0, column=0, sticky="e", padx=5, pady=4)
        self.product_id_entry = tk.Entry(form, width=25)
        self.product_id_entry.grid(row=0, column=1)

        tk.Label(form, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=4)
        self.product_name_entry = tk.Entry(form, width=25)
        self.product_name_entry.grid(row=1, column=1)

        tk.Label(form, text="Category:").grid(row=2, column=0, sticky="e", padx=5, pady=4)
        self.product_category = ttk.Combobox(form, values=["Electronics", "Clothing", "Grocery"], state="readonly", width=22)
        self.product_category.grid(row=2, column=1)
        self.product_category.current(0)

        tk.Label(form, text="Price:").grid(row=3, column=0, sticky="e", padx=5, pady=4)
        self.product_price_entry = tk.Entry(form, width=25)
        self.product_price_entry.grid(row=3, column=1)

        tk.Label(form, text="Stock:").grid(row=4, column=0, sticky="e", padx=5, pady=4)
        self.product_stock_entry = tk.Entry(form, width=25)
        self.product_stock_entry.grid(row=4, column=1)

        button_frame = tk.Frame(right)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Add Product", width=15, command=self.add_product).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Update Product", width=15, command=self.update_product).grid(row=0, column=1, padx=5)

        bottom_frame = tk.Frame(self.main_frame)
        bottom_frame.pack(fill="x", padx=10, pady=5)
        tk.Button(bottom_frame, text="View Orders", width=15, command=self.show_orders_window).pack(side="left")
        tk.Button(bottom_frame, text="Logout", width=15, command=self.logout).pack(side="right")

        self.refresh_products()

    def populate_product_fields(self, event):
        selected = self.product_tree.focus()
        if not selected:
            return
        values = self.product_tree.item(selected, "values")
        if not values:
            return
        product = self.find_product(values[0])
        if product:
            self.product_id_entry.delete(0, tk.END)
            self.product_id_entry.insert(0, product["product_id"])
            self.product_name_entry.delete(0, tk.END)
            self.product_name_entry.insert(0, product["name"])
            self.product_category.set(product["category"])
            self.product_price_entry.delete(0, tk.END)
            self.product_price_entry.insert(0, product["price"])
            self.product_stock_entry.delete(0, tk.END)
            self.product_stock_entry.insert(0, product["stock"])

    def refresh_products(self):
        for row in self.product_tree.get_children():
            self.product_tree.delete(row)
        for product in self.products:
            item = self.make_product_obj(product)
            discount = f"{item.calculate_discounted_price():.2f}"
            self.product_tree.insert("", tk.END, values=(product["product_id"], product["name"], product["category"], product["price"], product["stock"], discount))

    def add_product(self):
        product_id = self.product_id_entry.get().strip()
        name = self.product_name_entry.get().strip()
        category = self.product_category.get()
        try:
            price = float(self.product_price_entry.get())
            stock = int(self.product_stock_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Price must be a number and stock must be an integer.")
            return

        if not product_id or not name:
            messagebox.showwarning("Invalid Input", "Please fill all product fields.")
            return
        if self.find_product(product_id):
            messagebox.showwarning("Duplicate Product", "A product with this ID already exists.")
            return

        self.products.append({"product_id": product_id, "name": name, "price": price, "stock": stock, "category": category, "type": category})
        self.save_data()
        self.refresh_products()
        messagebox.showinfo("Success", "Product added successfully.")

    def update_product(self):
        product_id = self.product_id_entry.get().strip()
        product = self.find_product(product_id)
        if not product:
            messagebox.showwarning("Not Found", "Please select a valid product.")
            return

        try:
            price = float(self.product_price_entry.get())
            stock = int(self.product_stock_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Price must be a number and stock must be an integer.")
            return

        product["name"] = self.product_name_entry.get().strip()
        product["category"] = self.product_category.get()
        product["price"] = price
        product["stock"] = stock
        product["type"] = product["category"]
        self.save_data()
        self.refresh_products()
        messagebox.showinfo("Success", "Product updated successfully.")

    def show_orders_window(self):
        orders_win = tk.Toplevel(self.root)
        orders_win.title("Orders")
        orders_win.geometry("650x400")

        tk.Label(orders_win, text="Order History", font=("Arial", 16, "bold")).pack(pady=10)
        tree = ttk.Treeview(orders_win, columns=("Customer", "Email", "Items", "Total"), show="headings")
        for col in ("Customer", "Email", "Items", "Total"):
            tree.heading(col, text=col)
            tree.column(col, width=150)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        for order in self.orders:
            items = ", ".join([f"{item['name']} x{item['qty']}" for item in order["items"]])
            tree.insert("", tk.END, values=(order["customer"], order["email"], items, f"{order['total']:.2f}"))

    def show_customer_dashboard(self):
        self.clear_frame()
        tk.Label(self.main_frame, text=f"Customer Dashboard - {self.current_user['name']}", font=("Arial", 18, "bold")).pack(pady=10)

        frame = tk.Frame(self.main_frame)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        product_frame = tk.Frame(frame)
        product_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
        tk.Label(product_frame, text="Products", font=("Arial", 14, "bold")).pack(anchor="w")
        self.customer_product_tree = ttk.Treeview(product_frame, columns=("ID", "Name", "Category", "Price", "Stock"), show="headings", height=8)
        for col in ("ID", "Name", "Category", "Price", "Stock"):
            self.customer_product_tree.heading(col, text=col)
            self.customer_product_tree.column(col, width=100)
        self.customer_product_tree.pack(fill="both", expand=True)
        self.customer_product_tree.bind("<ButtonRelease-1>", self.select_customer_product)

        cart_frame = tk.Frame(frame)
        cart_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))
        tk.Label(cart_frame, text="Cart", font=("Arial", 14, "bold")).pack(anchor="w")
        self.cart_tree = ttk.Treeview(cart_frame, columns=("ID", "Name", "Qty", "Price", "Total"), show="headings", height=8)
        for col in ("ID", "Name", "Qty", "Price", "Total"):
            self.cart_tree.heading(col, text=col)
            self.cart_tree.column(col, width=100)
        self.cart_tree.pack(fill="both", expand=True)

        controls = tk.Frame(self.main_frame)
        controls.pack(fill="x", padx=10, pady=5)

        tk.Label(controls, text="Selected Product ID:").grid(row=0, column=0, padx=5, pady=4, sticky="e")
        self.selected_product_id = tk.Entry(controls, width=15, state="readonly")
        self.selected_product_id.grid(row=0, column=1, padx=5)

        tk.Label(controls, text="Quantity:").grid(row=0, column=2, padx=5, sticky="e")
        self.cart_qty = tk.Entry(controls, width=10)
        self.cart_qty.grid(row=0, column=3, padx=5)

        tk.Button(controls, text="Add to Cart", width=12, command=self.add_to_cart).grid(row=0, column=4, padx=5)
        tk.Button(controls, text="Remove Selected", width=13, command=self.remove_from_cart).grid(row=0, column=5, padx=5)
        tk.Button(controls, text="Checkout", width=12, command=self.checkout).grid(row=0, column=6, padx=5)

        footer = tk.Frame(self.main_frame)
        footer.pack(fill="x", padx=10, pady=5)
        tk.Button(footer, text="Logout", width=12, command=self.logout).pack(side="right")

        self.refresh_customer_products()
        self.refresh_cart()

    def select_customer_product(self, event):
        selected = self.customer_product_tree.focus()
        if selected:
            values = self.customer_product_tree.item(selected, "values")
            self.selected_product_id.config(state="normal")
            self.selected_product_id.delete(0, tk.END)
            self.selected_product_id.insert(0, values[0])
            self.selected_product_id.config(state="readonly")

    def refresh_customer_products(self):
        for row in self.customer_product_tree.get_children():
            self.customer_product_tree.delete(row)
        for product in self.products:
            self.customer_product_tree.insert("", tk.END, values=(product["product_id"], product["name"], product["category"], product["price"], product["stock"]))

    def refresh_cart(self):
        for row in self.cart_tree.get_children():
            self.cart_tree.delete(row)
        for item in self.cart:
            total = item["price"] * item["qty"]
            self.cart_tree.insert("", tk.END, values=(item["product_id"], item["name"], item["qty"], item["price"], f"{total:.2f}"))

    def add_to_cart(self):
        product_id = self.selected_product_id.get().strip()
        if not product_id:
            messagebox.showwarning("Cart Error", "Please select a product first.")
            return
        try:
            qty = int(self.cart_qty.get())
        except ValueError:
            messagebox.showwarning("Cart Error", "Please enter a valid quantity.")
            return
        if qty <= 0:
            messagebox.showwarning("Cart Error", "Quantity must be greater than zero.")
            return

        product = self.find_product(product_id)
        if not product or product["stock"] < qty:
            messagebox.showwarning("Stock Error", "Not enough stock for selected product.")
            return

        existing = next((item for item in self.cart if item["product_id"] == product_id), None)
        if existing:
            if product["stock"] < existing["qty"] + qty:
                messagebox.showwarning("Stock Error", "Not enough stock to add more of this product.")
                return
            existing["qty"] += qty
        else:
            self.cart.append({"product_id": product_id, "name": product["name"], "price": product["price"], "qty": qty})

        self.refresh_cart()
        messagebox.showinfo("Cart", "Product added to cart.")

    def remove_from_cart(self):
        selected = self.cart_tree.focus()
        if not selected:
            messagebox.showwarning("Cart Error", "Select an item in the cart to remove.")
            return
        values = self.cart_tree.item(selected, "values")
        self.cart = [item for item in self.cart if item["product_id"] != values[0]]
        self.refresh_cart()
        messagebox.showinfo("Cart", "Item removed from cart.")

    def checkout(self):
        if not self.cart:
            messagebox.showwarning("Checkout", "Your cart is empty.")
            return

        total = 0
        for item in self.cart:
            product = self.find_product(item["product_id"])
            if not product or product["stock"] < item["qty"]:
                messagebox.showwarning("Checkout", f"Not enough stock for {item['name']}.")
                return
            total += item["price"] * item["qty"]

        for item in self.cart:
            product = self.find_product(item["product_id"])
            product["stock"] -= item["qty"]

        self.orders.append({
            "customer": self.current_user["name"],
            "email": self.current_user["email"],
            "items": [item.copy() for item in self.cart],
            "total": total,
        })
        self.save_data()
        self.cart = []
        self.refresh_customer_products()
        self.refresh_cart()
        messagebox.showinfo("Checkout", f"Purchase successful! Total bill: {total:.2f}")

    def logout(self):
        self.current_user = None
        self.cart = []
        self.show_login_screen()


if __name__ == "__main__":
    ShoppingApp()
