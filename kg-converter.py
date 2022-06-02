from tkinter import *

window = Tk()

# Title
window.title('Convert Kg')

# Convert Functions
def kg_converter():
    # print("Success:", kg_input.get())
    # kg to grams (1kg == 1000 grams)
    grams = float(kg_input.get()) * 1000
    grams_results.insert(END, grams)
    # kg to pounds (1kg == 2.20462 pounds)
    pounds = float(kg_input.get()) * 2.20462
    pounds_results.insert(END, pounds)
    # kg to ounces (1kg == 35.274 ounces)
    ounces = float(kg_input.get()) * 35.274
    ounces_results.insert(END, ounces)


# Add Label for Kg
Label(window, text='Kg', height=1, width=20).grid(row=0, column=0)

# Add entry for Kg input
kg_input = StringVar()
# We store the entry value in a variable using the textvariable attribute
kg_entry = Entry(window, textvariable=kg_input).grid(row=0, column=1)


# Add convert Button
convert_btn = Button(window, text='Convert', command=kg_converter).grid(row=0, column=2)

# Conversion Results
grams_results = Text(window, height=1, width=18)
grams_results.grid(row=1, column=0)
pounds_results = Text(window, height=1, width=20)
pounds_results.grid(row=1, column=1)
ounces_results = Text(window, height=1, width=20)
ounces_results.grid(row=1, column=2)

window.mainloop()