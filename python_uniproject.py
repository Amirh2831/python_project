import tkinter as tk
from tkinter import messagebox

products = ['پاکن','خودکار','کتاب', 'مداد', 'دفتر']  # محصولات موجود
cart = {}  # سبد خرید به شکل دیکشنری {محصول: تعداد}

def add_to_cart():
    item = entry.get().strip()
    if item == '':
        messagebox.showwarning("هشدار", "لطفاً نام محصول را وارد کنید!")
        return
    if item in products:
        if item in cart:
            cart[item] += 1
        else:
            cart[item] = 1
        update_cart_display()
        entry.delete(0, tk.END)
    else:
        messagebox.showerror("خطا", f"محصول '{item}' موجود نیست.")

def remove_from_cart():
    selected = cart_listbox.curselection()
    if not selected:
        messagebox.showwarning("هشدار", "لطفاً یک محصول برای حذف انتخاب کنید.")
        return
    item_text = cart_listbox.get(selected[0])
    # متن به صورت "تعداد x محصول" هست، باید محصول رو جدا کنیم
    parts = item_text.split(' x ')
    product = parts[1]
    if cart[product] > 1:
        cart[product] -= 1
    else:
        del cart[product]
    update_cart_display()

def update_cart_display():
    cart_listbox.delete(0, tk.END)
    if not cart:
        cart_listbox.insert(tk.END, "سبد خرید خالی است.")
    else:
        for product, count in cart.items():
            cart_listbox.insert(tk.END, f"{count} x {product}")

root = tk.Tk()
root.title("فروشگاه ساده")

tk.Label(root, text="محصولات موجود: " + ", ".join(products), font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

add_button = tk.Button(root, text="اضافه به سبد خرید", font=("Arial", 14), command=add_to_cart)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="حذف محصول از سبد خرید", font=("Arial", 14), command=remove_from_cart)
remove_button.pack(pady=5)

cart_listbox = tk.Listbox(root, height=10, width=30, font=("Arial", 12))
cart_listbox.pack(pady=10)
update_cart_display()

root.mainloop()
