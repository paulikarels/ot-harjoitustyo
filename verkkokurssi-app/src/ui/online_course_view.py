from tkinter import ttk, StringVar, constants, messagebox
from tkinter import Text
from ui.exercise_view import ExerciseView
import plotly.graph_objs as go

class OnlineCourseView:
    def __init__(self, root, handle_course, get_courses, show_login_view, course_repository, exercise_repository, show_online_course_view, current_user):
        self._root = root
        self._handle_course = handle_course
        self._get_courses = get_courses
        self._show_login_view = show_login_view
        self._show_online_course_view = show_online_course_view 
        self._current_course = None
        self._course_repository = course_repository
        self._exercise_repository = exercise_repository
        self._current_course_id = None
        self._current_user = current_user
        self._frame = ttk.Frame(master=self._root)  
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        course_list_label = ttk.Label(master=self._frame, text="Courses:")
        self._course_listbox = ttk.Treeview(master=self._frame, columns=("Credits"))

        self._course_listbox.heading("#0", text="Course Name")
        self._course_listbox.heading("Credits", text="Credits")
        
        course_name_label = ttk.Label(master=self._frame, text="Course Name:")
        self._course_name_text = Text(master=self._frame, height=1, width=15)

        add_course_button = ttk.Button(master=self._frame, text="Add Course", command=self._add_course)
        credits_label = ttk.Label(master=self._frame, text="Credits:")
        self._credits_entry = ttk.Entry(master=self._frame, width=5)
        delete_course_button = ttk.Button(master=self._frame, text="Delete Course", command=self._delete_course)
        time_series_button = ttk.Button(master=self._frame, text="Show Progress Chart", command=self._show_time_series_chart)    

        self._back_to_login_button = ttk.Button(master=self._frame, text="Back to Login", command=self._show_login_view)
        self._back_to_login_button.grid(row=7, column=0, sticky=(constants.W, constants.E), padx=8, pady=8)

        course_list_label.grid(row=0, column=0, sticky=constants.W, padx=8, pady=8)
        self._course_listbox.grid(row=1, column=0, rowspan=4, sticky=(constants.N, constants.S, constants.E, constants.W), padx=8, pady=8)

        course_name_label.grid(row=1, column=1, sticky=constants.W, padx=1, pady=2)
        self._course_name_text.grid(row=2, column=1, sticky=(constants.W, constants.E), padx=1, pady=2)
        
        credits_label.grid(row=3, column=1, sticky=constants.W, padx=1, pady=2)
        self._credits_entry.grid(row=4, column=1, sticky=constants.W, padx=1, pady=2)

        add_course_button.grid(row=5, column=1, sticky=(constants.W, constants.E), padx=8, pady=8)
        delete_course_button.grid(row=6, column=1, sticky=(constants.W, constants.E), padx=8, pady=8)
        
        time_series_button.grid(row=7, column=1, columnspan=2, sticky=(constants.W, constants.E), padx=8, pady=8)

        time_series_button = ttk.Button(master=self._frame, text="Show Time Series Chart", command=self._show_time_series_chart)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)

        self._load_courses()

    def _load_courses(self):
        for item in self._course_listbox.get_children():
            self._course_listbox.delete(item)

        courses = self._get_courses()
        
        for course in courses:
            self._course_listbox.insert("", "end", text=course.title, values=(course.credits))

        for item in self._course_listbox.get_children():
            self._course_listbox.bind("<Button-1>", self._handle_course_click)



    def _add_course(self):
        course_name = self._course_name_text.get("1.0", "end-1c")
        creditss = self._credits_entry.get()

        if course_name and creditss.isdigit() and int(creditss) >= 0:
            self._handle_course(course_name, int(creditss))
            self._load_courses()
            self._course_name_text.delete("1.0", "end")
            self._credits_entry.delete(0, 'end')
        else:
            messagebox.showerror('Error', 'Course name cannot be empty, and credits should be a positive integer!')
            print("Course name cannot be empty, and credits should be a positive integer.")

    def _delete_course(self):
        selected_item = self._course_listbox.selection()
        if selected_item:
            course_title = self._course_listbox.item(selected_item, "text")
            course_id = self._course_repository.get_course_with_title(course_title)[0].id
            self._course_repository.delete_course_with_course_id(course_id)
            self._load_courses()

    def _handle_course_click(self, event):
        item = self._course_listbox.selection()
        if item:
            self._current_course = self._course_listbox.item(item, "text")
            course_title = self._course_listbox.item(item, "text")
            current_course_id = self._course_repository.get_course_with_title(course_title)[0].id
            self.destroy()

            exercise_view = ExerciseView(
                self._root,
                self._show_online_course_view,
                self._exercise_repository,
                self._course_repository,
                current_course_id,  
                course_title,
                self._get_exercises_for_course 
            )

            exercise_view.pack()

    def _get_exercises_for_course(self, course_title):
        course = self._course_repository.get_course_with_title(course_title)
        if course:
            exercises = self._exercise_repository.get_exercises_for_course(course[0].id)
            exercise_data = [(exercise.description, "Done" if exercise.done else "Not Done") for exercise in exercises]
            return exercise_data
        else:
            return []
            


    def _show_time_series_chart(self):
        course_data = self._get_courses()

        course_timestamps = [course.created_at for course in course_data]
        course_titles = [course.title for course in course_data]

        completed_exercises = {course.title: 0 for course in course_data}

        exercise_data = self._exercise_repository.get_exercises_for_user(self._current_user.id)

        exercise_timestamps = []
        exercise_courses = []

        for exercise in exercise_data:
            for course in course_data:
                if exercise.course == course.id:
                    if exercise.done:
                        completed_exercises[course.title] += 1
                        exercise_timestamps.append(exercise.marked_done_at)
                        exercise_courses.append(course.title)

        course_trace = go.Scatter(x=course_timestamps, y=course_titles, mode='markers+text', name='Kursi luoto', text=course_titles, textposition="bottom center")
        exercise_trace = go.Scatter(x=exercise_timestamps, y=exercise_courses, mode='markers', name='Tehdyt tehtävät', marker=dict(symbol='circle', size=10))

        layout = go.Layout(title='Kurssi ja tehtävä taulu', xaxis=dict(title='Timestamp'), yaxis=dict(title='Kurssi'))

        fig = go.Figure(data=[course_trace, exercise_trace], layout=layout)

        fig.show()