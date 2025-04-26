#Script to find the factorial of a number straightforward and with a recursive function.
import tkinter as tk #Import tkinter to have a GUI window for the user to interact with.
#Define the Solution class and the two functions.
class Solution(object):
    def findFactorial(self, n): #This is the straightforward function to find a factorial. 
        result = 1
        for i in range (1,n+1): #We iterate over the numbers up to the input one, multiplying them all and updating the result variable.
            result = result*i
        return result

    def findFactorialRecursively(self, n):
        if n == 1: #Condition to finish the recursion. The factorial of 1 is 1.
            return 1
        else:
            return n * self.findFactorialRecursively(n-1) # factorial(n) = n*factorial(n-1) until we reach n==1.
        
#Ask user for an input integer number that they want to find the factorial of.
#We ask this using a Graphic User Interface (GUI) through the tkinter library.

def get_input():
    global n #To make the variable global so we can use it outside the function.
    n = entry.get()
    #Validate that the input is valid.
    try:
        n = int(n) #Take the user input and convert it to an integer.
    except ValueError:
        result_label1.config(text=f"Input is invalid, please enter a valid integer.", fg="red") #If the input format cannot be converted to an integer (e.g. it is a string or a float) then we raise an exception and ask the user to provide a valid integer.
        return

    #Confirm the input number.
    result_label1.config(text=f"The input number you provided is {n}", fg = "green")
    #To be able to output the factorial, we want to check what category the input falls into:
    if n < 0: #Factorial of a negative number is not defined.
        result_label2.config(text="Input number is negative. Factorial of a negative number is not defined.", fg = "red")
    elif n == 0: #Factorial of 0 is 1.
        result_label2.config(text="Factorial of 0 is 1", fg = "blue")
    else: #If input number is positive, we execute the two functions.
        solution = Solution()
        fact1 = solution.findFactorial(n)
        fact2 = solution.findFactorialRecursively(n)
        result_label2.config(text=f"Straightforward: {fact1} | Recursive: {fact2}", fg = "blue")
        #Lastly, we want to check if the two solution methods output the same result.
        if fact1 == fact2:
            result_label3.config(text="The two methods match!", fg = "green")
        else:
            result_label3.config(text="The two methods don't match.", fg = "red")

def open_window(): #Specify the tkinter window as a function so we can call it whenever needed.
    global window, entry, result_label1, result_label2, result_label3
    window = tk.Tk() #Initializes the window.
    window.title("Factorial Calculator")
    window.configure(bg="#f0f8ff")  # Light background
    label = tk.Label(text="Enter a valid integer to find factorial", font=("Helvetica", 14, "bold"), bg="#f0f8ff", fg="#333")
    entry = tk.Entry(font=("Helvetica", 12), width=20)
    button = tk.Button(text="Submit", command=get_input, bg="#4CAF50", fg="white", font=("Helvetica", 12), width=10)
    exit_button = tk.Button(text="Exit", command=window.destroy, bg="#f44336", fg="white", font=("Helvetica", 12), width=10)
    result_label1 = tk.Label(text="", bg="#f0f8ff", font=("Helvetica", 12))
    result_label2 = tk.Label(text="", bg="#f0f8ff", font=("Helvetica", 12))
    result_label3 = tk.Label(text="", bg="#f0f8ff", font=("Helvetica", 12))

    label.pack(pady=10)
    entry.pack(pady=5)
    button.pack(pady=5)
    exit_button.pack(pady=5)
    result_label1.pack(pady=5)
    result_label2.pack(pady=5)
    result_label3.pack(pady=5)

    window.mainloop()

#Start GUI.
open_window()