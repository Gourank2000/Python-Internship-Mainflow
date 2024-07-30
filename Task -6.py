from tkinter import *
import tkinter.messagebox as messagebox

class BillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Billing System")
        self.root.geometry("800x600")

        # Create frames
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True)

        self.title_label = Label(self.main_frame, text="Billing System", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.product_frame = Frame(self.main_frame)
        self.product_frame.pack(fill=X)

        self.customer_frame = Frame(self.main_frame)
        self.customer_frame.pack(fill=X)

        self.invoice_frame = Frame(self.main_frame)
        self.invoice_frame.pack(fill=X)

        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(fill=X)

        # Product details
        self.product_label = Label(self.product_frame, text="Product Details", font=("Arial", 18))
        self.product_label.pack(side=LEFT, padx=10)

        self.product_name_label = Label(self.product_frame, text="Product Name", font=("Arial", 14))
        self.product_name_label.pack(side=LEFT, padx=10)

        self.product_name_entry = Entry(self.product_frame, font=("Arial", 14))
        self.product_name_entry.pack(side=LEFT, padx=10)

        self.product_price_label = Label(self.product_frame, text="Product Price", font=("Arial", 14))
        self.product_price_label.pack(side=LEFT, padx=10)

        self.product_price_entry = Entry(self.product_frame, font=("Arial", 14))
        self.product_price_entry.pack(side=LEFT, padx=10)

        # Customer information
        self.customer_label = Label(self.customer_frame, text="Customer Information", font=("Arial", 18))
        self.customer_label.pack(side=LEFT, padx=10)

        self.customer_name_label = Label(self.customer_frame, text="Customer Name", font=("Arial", 14))
        self.customer_name_label.pack(side=LEFT, padx=10)

        self.customer_name_entry = Entry(self.customer_frame, font=("Arial", 14))
        self.customer_name_entry.pack(side=LEFT, padx=10)

        self.customer_address_label = Label(self.customer_frame, text="Customer Address", font=("Arial", 14))
        self.customer_address_label.pack(side=LEFT, padx=10)

        self.customer_address_entry = Entry(self.customer_frame, font=("Arial", 14))
        self.customer_address_entry.pack(side=LEFT, padx=10)

        # Invoice details
        self.invoice_label = Label(self.invoice_frame, text="Invoice Details", font=("Arial", 18))
        self.invoice_label.pack(side=LEFT, padx=10)

        self.invoice_number_label = Label(self.invoice_frame, text="Invoice Number", font=("Arial", 14))
        self.invoice_number_label.pack(side=LEFT, padx=10)

        self.invoice_number_entry = Entry(self.invoice_frame, font=("Arial", 14))
        self.invoice_number_entry.pack(side=LEFT, padx=10)

        self.invoice_date_label = Label(self.invoice_frame, text="Invoice Date", font=("Arial", 14))
        self.invoice_date_label.pack(side=LEFT, padx=10)

        self.invoice_date_entry = Entry(self.invoice_frame, font=("Arial", 14))
        self.invoice_date_entry.pack(side=LEFT, padx=10)

        # Buttons
        self.generate_invoice_button = Button(self.button_frame, text="Generate Invoice", command=self.generate_invoice, font=("Arial", 14))
        self.generate_invoice_button.pack(side=LEFT, padx=10)

        self.print_invoice_button = Button(self.button_frame, text="Print Invoice", command=self.print_invoice, font=("Arial", 14))
        self.print_invoice_button.pack(side=LEFT, padx=10)

        self.save_invoice_button = Button(self.button_frame, text="Save Invoice", command=self.save_invoice, font=("Arial", 14))
        self.save_invoice_button.pack(side=LEFT, padx=10)

    def generate_invoice(self):
        # Generate invoice logic here
        messagebox.showinfo("Invoice Generated", "Invoice has been generated successfully.")

    def print_invoice(self):
        # Print invoice logic here
        messagebox.showinfo("Invoice Printed", "Invoice has been printed successfully.")

    def save_invoice(self):
        # Save invoice logic here
        messagebox.showinfo("Invoice Saved", "Invoice has been saved successfully.")

if __name__ == "__main__":
    root = Tk()
    billing_system = BillingSystem(root)
    root.mainloop()