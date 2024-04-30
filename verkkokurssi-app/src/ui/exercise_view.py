import secrets
from tkinter import ttk, constants
from entities.exercise import Exercise

class ExerciseView:
    def __init__(self, root, show_course_view, exercise_repository, course_repository,  current_course_id, current_course_title, get_exercises_for_course):
        self._root = root
        self._show_course_view = show_course_view
        self._course_repository = course_repository
        self._exercise_repository = exercise_repository
        self.current_course_title = current_course_title
        self._current_course_id = current_course_id
        self._get_exercises_for_course = get_exercises_for_course
        self._frame = ttk.Frame(master=self._root)
        self._initialize()
        self._reload_exercises()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._exercise_label = ttk.Label(master=self._frame, text="Exercises:")
        self._exercise_label.grid(row=0, column=0, padx=8, pady=8)

        self._exercise_listbox = ttk.Treeview(master=self._frame, columns=("Status"))
        self._exercise_listbox.grid(row=1, column=0, sticky=(constants.N, constants.S, constants.E, constants.W), padx=8, pady=8)

        self._exercise_listbox.heading("#0", text="Exercise")
        self._exercise_listbox.heading("Status", text="Status")

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

        for exercise, status in exercises:
            self._exercise_listbox.insert("", "end", text=exercise, values=(status))

    def _create_exercise(self):
        question = self._exercise_question_entry.get()
        if question:
            existing_exercises = self._exercise_repository.get_exercises_for_course(self._current_course_id)
            if any(exercise.description == question for exercise in existing_exercises):
                print("An exercise with the same description already exists for this course.")
            else:
                new_exercise = Exercise(self.generate_random_id(), description=question, done=False, course=self._current_course_id)
                self._exercise_repository.create(new_exercise)
                self._reload_exercises()
                self._exercise_question_entry.delete(0, constants.END)
        else:
            print("Please enter a question for the exercise.")

    def _mark_done(self):
        selected_item = self._exercise_listbox.focus()
        if selected_item:
            exercise_name = self._exercise_listbox.item(selected_item, "text")
            self._exercise_repository.mark_exercise_as_done(exercise_name)
            self._reload_exercises()
        else:
            print("Please select an exercise to mark as done.")

    def _reload_exercises(self):
        exercises = self._get_exercises_for_course(self.current_course_title)
        self.display_exercises(exercises)

    def close(self):
        self.destroy()

    def _back_button_clicked(self):
        self._show_course_view(self._current_course_id)
        self.close()

    def generate_random_id(self, length=10):
        return ''.join(
                secrets.choice("123456789")
                for _ in range(length)
            )
