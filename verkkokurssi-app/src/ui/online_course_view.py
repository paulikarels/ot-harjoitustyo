from tkinter import ttk, StringVar, constants
from services.app_service import app_service
from tkinter import Text


class OnlineCourseView:
    def __init__(self, root):
        self._root = root
        self._frame = ttk.Frame(master=self._root)  
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        course_list_label = ttk.Label(master=self._frame, text="Courses:")
        self._course_listbox = ttk.Treeview(master=self._frame)
        
        course_name_label = ttk.Label(master=self._frame, text="Course Name:")
        self._course_name_text = Text(master=self._frame, height=1, width=15)

        add_course_button = ttk.Button(master=self._frame, text="Add Course", command=self._add_course)
        delete_course_button = ttk.Button(master=self._frame, text="Delete Course", command=self._delete_course)
        
        course_list_label.grid(row=0, column=0, sticky=constants.W, padx=8, pady=8)
        self._course_listbox.grid(row=1, column=0, rowspan=4, sticky=(constants.N, constants.S, constants.E, constants.W), padx=8, pady=8)

        course_name_label.grid(row=1, column=1, sticky=constants.W, padx=1, pady=2)
        self._course_name_text.grid(row=2, column=1, sticky=(constants.W, constants.E), padx=1, pady=2)
        add_course_button.grid(row=3, column=1, sticky=(constants.W, constants.E), padx=8, pady=8)
        delete_course_button.grid(row=4, column=1, sticky=(constants.W, constants.E), padx=8, pady=8)
        
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)

    def _add_course(self):
        course_name = self._course_name_text.get("1.0", "end-1c")
        
        if course_name:
            self._course_listbox.insert("", "end", text=course_name)
            self._course_name_text.delete("1.0", "end")
        else:
            print("Course name cannot be empty.")

    def _delete_course(self):
        selected_item = self._course_listbox.selection()
        if selected_item:
            self._course_listbox.delete(selected_item)