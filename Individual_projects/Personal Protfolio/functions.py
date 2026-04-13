#RC 1st, personal protfolio
import tkinter as tk
from tkinter import messagebox
# Project Descriptions (Display BEFORE running the code)
project_descriptions = {
    "Project 1": {
        "description": "A calculator app that performs basic arithmetic operations.",
        "learned": ["Built GUI with Tkinter", "Implemented event handling"],
        "challenge": "Handling division by zero gracefully."
    },
    "Project 2": {
        "description": "A to-do list application with save/load functionality.",
        "learned": ["File handling", "Managing list states"],
        "challenge": "Persisting data between sessions."
    },
    "Project 3": {
        "description": "A simple game like Tic-Tac-Toe.",
        "learned": ["Game logic implementation", "Using grids"],
        "challenge": "Detecting game win conditions."
    },
    "Project 4": {
        "description": "A basic drawing app with canvas.",
        "learned": ["Drawing on canvas", "Mouse event handling"],
        "challenge": "Implementing smooth drawing."
    }
}

# Define project functions
def run_project_1():
    messagebox.showinfo("Project 1", "Running Calculator App...")


def run_project_2():
    messagebox.showinfo("Project 2", "Running To-Do List App...")


def run_project_3():
    messagebox.showinfo("Project 3", "Running Tic-Tac-Toe Game...")


def run_project_4():
    messagebox.showinfo("Project 4", "Running Drawing App...")


# Main Application 
class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Portfolio")
        self.create_widgets()

    def create_widgets(self):
        # Introduction Section
        intro_frame = tk.Frame(self.root, padx=10, pady=10)
        intro_frame.pack(fill='both', expand=True)

        intro_label = tk.Label(intro_frame, text="Welcome to My Portfolio!\n\n"
                                                 "This portfolio showcases some of my favorite projects "
                                                 "from this class and more!\n"
                                                 "Use the buttons below to view and run each project.",
                               justify='left')
        intro_label.pack()

        # Projects Buttons
        button_frame = tk.Frame(self.root, padx=10, pady=10)
        button_frame.pack()

        projects = ["Project 1", "Project 2", "Project 3", "Project 4"]
        run_functions = [run_project_1, run_project_2, run_project_3, run_project_4]

        for proj, func in zip(projects, run_functions):
            btn = tk.Button(button_frame, text=proj, width=20,
                            command=lambda f=func, p=proj: self.show_project_info(p, f))
            btn.pack(pady=5)

    def show_project_info(self, project_name, run_function):
        info = project_descriptions[project_name]
        desc_text = f"{project_name}:\n\n" \
                    f"Description: {info['description']}\n" \
                    f"Learned:\n- {info['learned'][0]}\n- {info['learned'][1]}\n" \
                    f"Challenge:\n- {info['challenge']}\n\n" \
                    f"Click OK to run the project."
        messagebox.showinfo(project_name, desc_text)
        # Run the project
        run_function()
