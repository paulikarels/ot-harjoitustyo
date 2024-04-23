from tkinter import ttk, constants

class ExerciseView:
    def __init__(self, root, show_course_view):
        self._root = root
        self._show_course_view = show_course_view
        self._frame = ttk.Frame(master=self._root)
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._exercise_label = ttk.Label(master=self._frame, text="Exercises:")
        self._exercise_label.grid(row=0, column=0, padx=8, pady=8)

        self._exercise_listbox = ttk.Treeview(master=self._frame)
        self._exercise_listbox.grid(row=1, column=0, sticky=(constants.N, constants.S, constants.E, constants.W), padx=8, pady=8)

        self._exercise_question_entry = ttk.Entry(master=self._frame, width=50)
        self._exercise_question_entry.grid(row=2, column=0, padx=8, pady=8)

        self._create_exercise_button = ttk.Button(master=self._frame, text="Create Exercise", command=self._create_exercise)
        self._create_exercise_button.grid(row=3, column=0, padx=8, pady=8)

        self._mark_done_button = ttk.Button(master=self._frame, text="Mark as Done", command=self._mark_done)
        self._mark_done_button.grid(row=4, column=0, padx=8, pady=8)

        self._back_button = ttk.Button(master=self._frame, text="Back", command=self._back_button_clicked)
        self._back_button.grid(row=5, column=0, padx=8, pady=8)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)

    def display_exercises(self, exercises):
        for item in self._exercise_listbox.get_children():
            self._exercise_listbox.delete(item)

        for exercise in exercises:
            self._exercise_listbox.insert("", "end", text=exercise)

    def _create_exercise(self):
        question = self._exercise_question_entry.get()
        if question:
            # Here you would create the exercise and add it to the list
            self._exercise_listbox.insert("", "end", text=question)
            self._exercise_question_entry.delete(0, constants.END)
        else:
            print("Please enter a question for the exercise.")

    def _mark_done(self):
        selected_item = self._exercise_listbox.focus()
        if selected_item:
            # Here you would mark the selected exercise as done
            self._exercise_listbox.item(selected_item, tags=("done",))
        else:
            print("Please select an exercise to mark as done.")

    def close(self):
        self.destroy()

    def _back_button_clicked(self):
        self._show_course_view()
        self.close()

