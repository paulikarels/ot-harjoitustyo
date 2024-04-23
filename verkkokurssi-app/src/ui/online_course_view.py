from tkinter import ttk, StringVar, constants
from services.app_service import app_service
from tkinter import Text
from ui.exercise_view import ExerciseView

class OnlineCourseView:
    def __init__(self, root, handle_course, get_courses, exercise_view, show_login_view):
        self._root = root
        self._handle_course = handle_course
        self._get_courses = get_courses
        self._exercise_view = exercise_view
        self._show_login_view = show_login_view
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
        credits = self._credits_entry.get()

        if course_name and credits.isdigit() and int(credits) >= 0:
            self._handle_course(course_name, int(credits))
            self._load_courses()
            self._course_name_text.delete("1.0", "end")
            self._credits_entry.delete(0, 'end')
        else:
            print("Course name cannot be empty, and credits should be a positive integer.")

    def _delete_course(self):
        selected_item = self._course_listbox.selection()
        if selected_item:
            self._course_listbox.delete(selected_item)

    def _handle_course_click(self, event):
        item = self._course_listbox.selection()
        if item:
            course_title = self._course_listbox.item(item, "text")
    
            self.destroy()
            
            exercises = self._get_exercises_for_course(course_title)
            self._exercise_view.display_exercises(exercises)
            
            self._exercise_view.pack()



    def _get_exercises_for_course(self, course_title):
        return [""]
