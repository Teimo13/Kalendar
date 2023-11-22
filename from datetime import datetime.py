import tkinter as tk
from datetime import datetime
from tkinter import messagebox

class AppointmentManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Manager")

        self.appointments = {}

        # Labels and Entry widgets for date and description
        tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
        self.date_entry = tk.Entry(root)
        self.date_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Description:").grid(row=1, column=0, padx=10, pady=5)
        self.description_entry = tk.Entry(root)
        self.description_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons for adding and listing appointments
        tk.Button(root, text="Add Appointment", command=self.add_appointment).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(root, text="List Appointments", command=self.list_appointments).grid(row=3, column=0, columnspan=2, pady=10)

    def add_appointment(self):
        date = self.date_entry.get()
        description = self.description_entry.get()

        if date and description:
            if date in self.appointments:
                self.appointments[date].append(description)
            else:
                self.appointments[date] = [description]

            tk.messagebox.showinfo("Success", "Appointment added successfully!")

            # Clear entry fields after adding an appointment
            self.date_entry.delete(0, tk.END)
            self.description_entry.delete(0, tk.END)
        else:
            tk.messagebox.showwarning("Warning", "Please enter both date and description.")

    def list_appointments(self):
        if self.appointments:
            sorted_appointments = sorted(self.appointments.items(), key=lambda x: datetime.strptime(x[0], '%Y-%m-%d'))
            appointment_text = ""
            for date, descriptions in sorted_appointments:
                appointment_text += f"{date}: {', '.join(descriptions)}\n"

            tk.messagebox.showinfo("Appointments", appointment_text)
        else:
            tk.messagebox.showinfo("Appointments", "No appointments available.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentManager(root)
    root.mainloop()