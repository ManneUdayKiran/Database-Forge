
# 🛒 Store Manager CLI App

A command-line Python application to manage products and categories using SQLAlchemy ORM and a SQLite database.

---
## Screenshots
![image](https://github.com/user-attachments/assets/0f4f8d0e-cf72-4d0a-8c24-6839fd77faa9)
![image](https://github.com/user-attachments/assets/054becad-bef6-4540-8afa-becf36c2a090)
![image](https://github.com/user-attachments/assets/945d1d7c-b195-4914-b36f-525d06ad37c7)
![image](https://github.com/user-attachments/assets/6affda2a-6cce-4506-878b-17ef21b1e2ef)
![image](https://github.com/user-attachments/assets/8db2c504-cc09-4d74-a93d-bb578b8a1bb5)
![image](https://github.com/user-attachments/assets/0d947fb0-3685-468a-9585-696c8a8b8ceb)

---

## 📦 Features

- View all products with price and category
- Add a new product to a category
- Update product prices
- Delete products
- Auto-populates with sample categories and products if the database is empty

---

## 🛠️ Tech Stack

- Python 3.x
- SQLAlchemy (ORM)
- SQLite3 (Database)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ManneUdayKiran/Store-Manager-CLI.git
cd Store-Manager-CLI
````

### 2. Install Dependencies

```bash
pip install SQLAlchemy
```

### 3. Run the App

```bash
python store_manager.py
```

---

## 🗂 Sample Data

On first run, the app creates and inserts sample data:

### 📚 Categories

* Electronics
* Books

### 🛍️ Products

| Product Name          | Price  | Category    |
| --------------------- | ------ | ----------- |
| Laptop                | ₹75000 | Electronics |
| Smartphone            | ₹25000 | Electronics |
| Python Programming    | ₹499   | Books       |
| Data Science Handbook | ₹799   | Books       |

---

## 📂 Project Structure

```
store_manager.py
README.md
store.db (auto-created on first run)
```

---

## 👨‍💻 Author

GitHub: [ManneUdayKiran](https://github.com/ManneUdayKiran)

---

## 📋 License

This project is open source and free to use.

```
