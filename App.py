from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# ORM Setup
Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship("Category", back_populates="products")

# Database Initialization
engine = create_engine('sqlite:///store.db', echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Sample data (insert only if DB is empty)
if not session.query(Category).first():
    electronics = Category(category_name="Electronics")
    books = Category(category_name="Books")
    session.add_all([
        Product(product_name="Laptop", price=75000.0, category=electronics),
        Product(product_name="Smartphone", price=25000.0, category=electronics),
        Product(product_name="Python Programming", price=499.0, category=books),
        Product(product_name="Data Science Handbook", price=799.0, category=books),
    ])
    session.commit()

# Operations
def view_products():
    products = session.query(Product).all()
    if not products:
        print("No products found.")
    for p in products:
        print(f"{p.product_id}. {p.product_name} | ₹{p.price} | Category: {p.category.category_name}")

def update_product_price():
    view_products()
    pid = int(input("Enter Product ID to update: "))
    product = session.query(Product).get(pid)
    if product:
        new_price = float(input(f"Enter new price for {product.product_name}: ₹"))
        product.price = new_price
        session.commit()
        print("Price updated.")
    else:
        print("Product not found.")

def delete_product():
    view_products()
    pid = int(input("Enter Product ID to delete: "))
    product = session.query(Product).get(pid)
    if product:
        session.delete(product)
        session.commit()
        print("Product deleted.")
    else:
        print("Product not found.")

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: ₹"))
    print("Available categories:")
    categories = session.query(Category).all()
    for c in categories:
        print(f"{c.category_id}. {c.category_name}")
    cid = int(input("Enter category ID: "))
    category = session.query(Category).get(cid)
    if category:
        new_product = Product(product_name=name, price=price, category=category)
        session.add(new_product)
        session.commit()
        print("Product added.")
    else:
        print("Invalid category ID.")

# CLI Menu
def menu():
    while True:
        print("\n=== Store Manager ===")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product Price")
        print("4. Delete Product")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            view_products()
        elif choice == '2':
            add_product()
        elif choice == '3':
            update_product_price()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
