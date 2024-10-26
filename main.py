import tkinter as tk
from tkinter import ttk, scrolledtext, font
import pyttsx3
import threading

class AirtelIVRGUI:
    def __init__(self, master):
        self.master = master
        master.title("jagruti digitel services System")
        master.geometry("400x700")
        master.configure(bg='#f0f0f0')

        self.engine = pyttsx3.init()
        voices=self.engine.getProperty('voices')
        self.engine.setProperty('voice',voices[0].id)         #this line for voice of program 0=man,1=woman
        self.engine.setProperty('rate', 150)

        self.create_widgets()
        self.current_menu = self.main_menu
        self.show_menu()

    def create_widgets(self):
        # Create and pack the output text area
        self.output_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, width=40, height=10, bg='#ffffff', fg='#000000')
        self.output_area.pack(padx=10, pady=10)

        # Create the dial pad
        dial_pad_frame = tk.Frame(self.master, bg='#f0f0f0')
        dial_pad_frame.pack(padx=10, pady=5)

        buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '*', '0', '#'
        ]

        button_font = font.Font(family="jagruti", size=16, weight="bold")

        row, col = 0, 0
        for button in buttons:
            tk.Button(dial_pad_frame, text=button, width=5, height=2, 
                      bg='#ffffff', fg='#000000', activebackground='#e0e0e0',
                      relief=tk.RAISED, bd=1,
                      font=button_font,
                      command=lambda x=button: self.dial_button_click(x)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

        # Create special buttons
        special_buttons_frame = tk.Frame(self.master, bg='#f0f0f0')
        special_buttons_frame.pack(padx=10, pady=5)

        call_button = tk.Button(special_buttons_frame, text="Call", width=10, height=2,
                                bg='#4CAF50', fg='#ffffff', activebackground='#45a049',
                                relief=tk.RAISED, bd=1,
                                font=button_font,
                                command=lambda: self.dial_button_click('call'))
        call_button.grid(row=0, column=0, padx=5, pady=5)

        end_call_button = tk.Button(special_buttons_frame, text="End Call", width=10, height=2,
                                    bg='#f44336', fg='#ffffff', activebackground='#d32f2f',
                                    relief=tk.RAISED, bd=1,
                                    font=button_font,
                                    command=self.end_call)
        end_call_button.grid(row=0, column=1, padx=5, pady=5)

        self.current_input = ''
        self.input_display = tk.Label(self.master, text='', font=("Arial", 24), bg='#f0f0f0')
        self.input_display.pack(pady=10)

    def dial_button_click(self, button):
        if button == 'call':
            self.process_input(self.current_input)
            self.current_input = ''
        else:
            self.current_input += button
            self.input_display.config(text=self.current_input) #main code ->
          

    def end_call(self):
        self.speak("Thank you for using jagruti digitel services. Goodbye!")
        self.master.quit()

    def show_menu(self):
        self.output_area.delete(1.0, tk.END)
        menu_text = self.current_menu()
        self.output_area.insert(tk.END, menu_text)
        self.speak(menu_text)
        self.current_input = ''
        self.input_display.config(text='')

    def process_input(self, user_input):
        if user_input in ['1', '2', '3', '4', '5']:
            self.handle_menu_choice(user_input)
        elif user_input == '6':
            self.show_menu()
        elif user_input == '8':
            self.current_menu = self.main_menu
            self.show_menu()
        else:
            self.output_area.insert(tk.END, "\nInvalid input. Please try again.\n")
            self.speak("Invalid input. Please try again.")

    def handle_menu_choice(self, choice):
        menu_functions = {
            '1': self.postpaid_menu,
            '2': self.prepaid_menu,
            '3': self.new_connection_menu,
            '4': self.tv_menu,
            '5': self.wifi_menu
        }
        self.current_menu = menu_functions.get(choice, self.main_menu)
        self.show_menu()

    def speak(self, text):
        threading.Thread(target=self.engine.say, args=(text,)).start()
        self.engine.runAndWait()

    def main_menu(self):
        return """Welcome to jagruti digitel services. Scam protection is live on jagruti digitel services.
 For postpaid query press 1
 For prepaid query press 2
 For new connection or new service press 3
 For digital TV service press 4
 For WiFi fiber query press 5
 To repeat previous menu press 6
 For main menu press 8
Enter your choice and press Call: """

    def postpaid_menu(self):
        return """
 your Query about internet not working press 2
 your Query about no communication during call press 3
 Register a complaint about jagruti digitel services postpaid services press 4
 Connect to the customer care service specialist press 5
 To repeat previous menu press 6
 For main menu press 8
Enter your choice and press Call: """

    def prepaid_menu(self):
        return """
 your Query about internet not working press 2
 your Query about no communication during call press 3
 Register a complaint about jagruti digitel service prepaid services press 4
 Connect to customer care service specialist press 5
 To repeat previous menu press 6
 For main menu press 8
Enter your choice and press Call: """

    def new_connection_menu(self):
        return """
 Buy a new SIM press 1
 Buy a new WiFi service press 2
 Buy a new TV service press 3
 Buy a new internet service press 4
 Know about premium plans press 5
 To repeat previous menu press 6
 For main menu press 8
Enter your choice and press Call: """

    def tv_menu(self):
        return """
 Know your digital TV plan press 1
 Modify channels on your digital TV press 2
 Top up your set-top box plan press 3
 Report no signal on your TV press 4
 Connect to the customer care service specialist prees 5
 To repeat previous menu prees 6
 For main menu prees 8
Enter your choice and press Call: """

    def wifi_menu(self):
        return """
 Know your fiber WiFi plan press 1
 Modify your fiber plan WiFi press 2
 Report no internet or data speed issues press 3
 Connect to your technician service specialist press 4
 Connect to the customer care service specialist press 5
 To repeat previous menu press 6
 For main menu press 8
Enter your choice and press Call: """

if __name__ == "__main__":
    root = tk.Tk()
    app = AirtelIVRGUI(root)
    root.mainloop()
