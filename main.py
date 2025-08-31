# import json
# import os
# import tkinter as tk
# from tkinter import ttk, messagebox, simpledialog


# class LibraryManager:
#     DATA_FILE = "library_data.json"

#     def __init__(self):
#         self.books = []
#         self.issued_books = {}
#         self.load_data()

#     def show_books(self):
#         """Show numbered list of books in a popup."""
#         if not self.books:
#             messagebox.showinfo("Available Books", "No books available.")
#             return
        
#         # Number the books
#         book_list = "\n".join([f"{i+1}. {book}" for i, book in enumerate(self.books)])
#         messagebox.showinfo("Available Books", book_list)

#     def load_data(self):
#         """Load data from JSON file or initialize defaults."""
#         if os.path.exists(self.DATA_FILE):
#             with open(self.DATA_FILE, "r") as f:
#                 data = json.load(f)
#                 self.books = data.get("books", [])
#                 self.issued_books = data.get("issued_books", {})
#         else:
#             self.books = [
#                 "Vistas", "Invention", "Rich & Poor", "Indian",
#                 "Macroeconomics", "Microeconomics", "Horror Story",
#                 "Justice", "Murder Mystery", "God & Devil",
#                 "Social Awareness", "Society", "Evolution of the Mankind",
#                 "48 Laws of Power", "Business Development", "Relationships"
#             ]
#             self.issued_books = {}
#             self.save_data()

#     def save_data(self):
#         """Save current data to JSON file."""
#         with open(self.DATA_FILE, "w") as f:
#             json.dump({"books": self.books, "issued_books": self.issued_books}, f, indent=4)

#     def borrow_book(self, name, book):
#         """Borrow a book for a user."""
#         if book in self.books:
#             self.books.remove(book)
#             self.issued_books.setdefault(name, []).append(book)
#             self.save_data()
#             return True
#         return False

#     def return_book(self, name, book):
#         """Return a borrowed book."""
#         if name in self.issued_books and book in self.issued_books[name]:
#             self.issued_books[name].remove(book)
#             if not self.issued_books[name]:
#                 del self.issued_books[name]
#             self.books.append(book)
#             self.save_data()
#             return True
#         return False

#     def donate_book(self, book):
#         """Donate a new book."""
#         if book and book not in self.books:
#             self.books.append(book)
#             self.save_data()
#             return True
#         return False


# class LibraryGUI:
#     def __init__(self, root, manager):
#         self.manager = manager
#         self.root = root
#         self.root.title("📚 Indore Library System")
#         self.root.geometry("700x500")

#         # Search Bar
#         self.search_var = tk.StringVar()
#         tk.Label(root, text="Search Book:", font=("Arial", 12)).pack(pady=5)
#         search_entry = tk.Entry(root, textvariable=self.search_var, width=40)
#         search_entry.pack()
#         search_entry.bind("<KeyRelease>", self.update_book_list)

#         # Book List
#         self.tree = ttk.Treeview(root, columns=("Book"), show="headings", height=15)
#         self.tree.heading("Book", text="Available Books")
#         self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
#         self.update_book_list()

#         # Buttons
#         btn_frame = tk.Frame(root)
#         btn_frame.pack(pady=10)

#         ttk.Button(btn_frame, text="Borrow Book", command=self.borrow_book).grid(row=0, column=0, padx=5)
#         ttk.Button(btn_frame, text="Return Book", command=self.return_book).grid(row=0, column=1, padx=5)
#         ttk.Button(btn_frame, text="Donate Book", command=self.donate_book).grid(row=0, column=2, padx=5)
#         ttk.Button(btn_frame, text="Track Books", command=self.track_books).grid(row=0, column=3, padx=5)
#         ttk.Button(btn_frame, text="Show Books", command=self.manager.show_books).grid(row=0, column=4, padx=5)

#         ttk.Button(root, text="Exit", command=root.quit).pack(pady=10)

#     def update_book_list(self, event=None):
#         """Update book list in the Treeview based on search."""
#         for row in self.tree.get_children():
#             self.tree.delete(row)
#         keyword = self.search_var.get().lower()
#         for book in self.manager.books:
#             if keyword in book.lower():
#                 self.tree.insert("", tk.END, values=(book,))

#     def borrow_book(self):
#         selected = self.tree.selection()
#         if not selected:
#             messagebox.showwarning("Warning", "Select a book to borrow.")
#             return
#         book = self.tree.item(selected[0])["values"][0]
#         name = self.prompt("Enter your name:")
#         if name:
#             if self.manager.borrow_book(name, book):
#                 messagebox.showinfo("Success", f"'{book}' issued to {name}")
#                 self.update_book_list()
#             else:
#                 messagebox.showerror("Error", "Book is not available.")

#     def return_book(self):
#         name = self.prompt("Enter your name:")
#         book = self.prompt("Enter book name to return:")
#         if name and book:
#             if self.manager.return_book(name, book):
#                 messagebox.showinfo("Success", f"'{book}' returned by {name}")
#                 self.update_book_list()
#             else:
#                 messagebox.showerror("Error", "Book not found under your name.")

#     def donate_book(self):
#         book = self.prompt("Enter book name to donate:")
#         if book:
#             if self.manager.donate_book(book):
#                 messagebox.showinfo("Thank You", f"'{book}' added to library!")
#                 self.update_book_list()
#             else:
#                 messagebox.showwarning("Warning", "Book already exists or invalid.")

#     def track_books(self):
#         if not self.manager.issued_books:
#             messagebox.showinfo("Track Books", "No books are issued.")
#         else:
#             data = "\n".join([f"{user}: {', '.join(books)}" for user, books in self.manager.issued_books.items()])
#             messagebox.showinfo("Issued Books", data)

#     def prompt(self, text):
#         return simpledialog.askstring("Input", text)


# if __name__ == "__main__":
#     root = tk.Tk()
#     manager = LibraryManager()
#     app = LibraryGUI(root, manager)
#     root.mainloop()













import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime


class LibraryManager:
    DATA_FILE = "library_data.json"

    def __init__(self):
        self.books = []
        self.issued_books = {}
        self.transactions = []
        self.load_data()

    def log_transaction(self, action, user, book):
        """Log each borrow/return/donate activity with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append({
            "action": action,
            "user": user,
            "book": book,
            "timestamp": timestamp
        })
        self.save_data()

    def show_books(self):
        """Show numbered list of books."""
        if not self.books:
            messagebox.showinfo("Available Books", "No books available.")
            return
        book_list = "\n".join([f"{i+1}. {book}" for i, book in enumerate(self.books)])
        messagebox.showinfo("Available Books", book_list)

    def load_data(self):
        """Load data from JSON file or initialize defaults."""
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "r") as f:
                data = json.load(f)
                self.books = data.get("books", [])
                self.issued_books = data.get("issued_books", {})
                self.transactions = data.get("transactions", [])
        else:
            self.books = [
                "Vistas", "Invention", "Rich & Poor", "Indian",
                "Macroeconomics", "Microeconomics", "Horror Story",
                "Justice", "Murder Mystery", "God & Devil",
                "Social Awareness", "Society", "Evolution of the Mankind",
                "48 Laws of Power", "Business Development", "Relationships"
            ]
            self.issued_books = {}
            self.transactions = []
            self.save_data()

    def save_data(self):
        """Save current data to JSON file."""
        with open(self.DATA_FILE, "w") as f:
            json.dump({
                "books": self.books,
                "issued_books": self.issued_books,
                "transactions": self.transactions
            }, f, indent=4)

    def borrow_book(self, name, book):
        """Borrow a book for a user."""
        if book in self.books:
            self.books.remove(book)
            self.issued_books.setdefault(name, []).append(book)
            self.log_transaction("borrowed", name, book)
            return True
        return False

    def return_book(self, name, book):
        """Return a borrowed book."""
        if name in self.issued_books and book in self.issued_books[name]:
            self.issued_books[name].remove(book)
            if not self.issued_books[name]:
                del self.issued_books[name]
            self.books.append(book)
            self.log_transaction("returned", name, book)
            return True
        return False

    def donate_book(self, book, name="Anonymous"):
        """Donate a new book."""
        if book and book not in self.books:
            self.books.append(book)
            self.log_transaction("donated", name, book)
            return True
        return False


class LibraryGUI:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("📚 Indore Library System")
        self.root.geometry("750x500")

        # Search Bar
        self.search_var = tk.StringVar()
        tk.Label(root, text="Search Book:", font=("Arial", 12)).pack(pady=5)
        search_entry = tk.Entry(root, textvariable=self.search_var, width=40)
        search_entry.pack()
        search_entry.bind("<KeyRelease>", self.update_book_list)

        # Book List
        self.tree = ttk.Treeview(root, columns=("Book"), show="headings", height=15)
        self.tree.heading("Book", text="Available Books")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)
        self.update_book_list()

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Borrow Book", command=self.borrow_book).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Return Book", command=self.return_book).grid(row=0, column=1, padx=5)
        ttk.Button(btn_frame, text="Donate Book", command=self.donate_book).grid(row=0, column=2, padx=5)
        ttk.Button(btn_frame, text="Track Books", command=self.track_books).grid(row=0, column=3, padx=5)
        ttk.Button(btn_frame, text="Activity Log", command=self.view_activity_log).grid(row=0, column=4, padx=5)

        ttk.Button(root, text="Exit", command=root.quit).pack(pady=10)

    def update_book_list(self, event=None):
        """Update book list in the Treeview based on search."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        keyword = self.search_var.get().lower()
        for book in self.manager.books:
            if keyword in book.lower():
                self.tree.insert("", tk.END, values=(book,))

    def borrow_book(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a book to borrow.")
            return
        book = self.tree.item(selected[0])["values"][0]
        name = self.prompt("Enter your name:")
        if name:
            if self.manager.borrow_book(name, book):
                messagebox.showinfo("Success", f"'{book}' issued to {name}")
                self.update_book_list()
            else:
                messagebox.showerror("Error", "Book is not available.")

    def return_book(self):
        name = self.prompt("Enter your name:")
        book = self.prompt("Enter book name to return:")
        if name and book:
            if self.manager.return_book(name, book):
                messagebox.showinfo("Success", f"'{book}' returned by {name}")
                self.update_book_list()
            else:
                messagebox.showerror("Error", "Book not found under your name.")

    def donate_book(self):
        book = self.prompt("Enter book name to donate:")
        name = self.prompt("Enter your name (leave blank for Anonymous):") or "Anonymous"
        if book:
            if self.manager.donate_book(book, name):
                messagebox.showinfo("Thank You", f"'{book}' added to library!")
                self.update_book_list()
            else:
                messagebox.showwarning("Warning", "Book already exists or invalid.")

    def track_books(self):
        if not self.manager.issued_books:
            messagebox.showinfo("Track Books", "No books are issued.")
        else:
            data = "\n".join([f"{user}: {', '.join(books)}" for user, books in self.manager.issued_books.items()])
            messagebox.showinfo("Issued Books", data)

    def view_activity_log(self):
        if not self.manager.transactions:
            messagebox.showinfo("Activity Log", "No activity recorded yet.")
        else:
            log = "\n".join([
                f"{t['timestamp']}: {t['user']} {t['action']} '{t['book']}'"
                for t in self.manager.transactions
            ])
            messagebox.showinfo("Activity Log", log)

    def prompt(self, text):
        return simpledialog.askstring("Input", text)


if __name__ == "__main__":
    root = tk.Tk()
    manager = LibraryManager()
    app = LibraryGUI(root, manager)
    root.mainloop()
