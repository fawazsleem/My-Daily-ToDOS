import flet as ft
from database import get_task,update_task,task_entry,delete_task
import datetime as dt

def main(page :ft.Page):
    page.title = "My Daily ToDoS"
    page.window.width = 500
    page.window.height = 600
    page.bgcolor = "#a14646"
    
    #================
    #switch change
    #================
    def switch_change(e):
        task_id = e.control.data
        task_completed = e.control.value
        update_task(task_id,int(task_completed))
    
    #============
    #get task
    #============
    tasks = get_task()
    title_container = ft.Container(width=480,height=50,bgcolor="#da6556",
                                   border_radius=15,padding=10,
                                   content=ft.Text("My Tasks",size=20,text_align=ft.TextAlign.CENTER))

    column = ft.Column(spacing=25,
                       scroll=ft.ScrollMode.AUTO,
                       controls=[],
                    )
    
    #==============
    #delete task
    #==============
    def delete_clicked(e):
        task_id = e.control.data

        delete_task(task_id)
        column.controls = [
            card for card in column.controls
            if card.data != task_id
        ]

        page.update()
    
    #======================
    #startup update task
    #======================
    for task in tasks:
        item = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                ft.Column([
                    ft.Text(f"{task['task name']}"),
                    ft.Text(f"due on {task['task complete time']}")
                ]),
                ft.Switch(
                          value=task["completed"],
                          data=task["ID"],
                          active_color="#EB895B",
                          active_track_color="#FDB773"  ,
                          inactive_thumb_color="#A14646",
                          inactive_track_color="#DA6556",
                          on_change=switch_change),
                ft.Button(
                        "Delete Task",
                        icon=ft.Icons.DELETE,
                        bgcolor="#DA6556",
                        color="white",
                        data=task["ID"],
                        on_click=delete_clicked
                )
            ]
        )
                
        column.controls.append(ft.Container(
            item,
            data=task["ID"],
            width=480,
            height=80,
            bgcolor="#eb895b",
            border_radius=15,
            padding=10
            ))   
    
    #========================
    # open popup
    #========================
    def open_popup(e):
        page.show_dialog(popup)
    
    #=================
    #entry new task
    #=================
    def add_task(e):
        global tasks
        task_name = task_input.value.strip()
        if task_name == "":
            task_input.error = "task name cannot be empty!"
            page.update()
            return
        
        due = selected_time.value
        if due == "No time selected":
            due = "Anytime"
        
        task_entry(task_name=task_name,task_time=due)
        
        task = get_task()
        new_task = task[-1]
        item = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        controls=[
            ft.Column([
                ft.Text(task_name),
                ft.Text(f"due on {due}")
            ]),

            ft.Switch(
                value=new_task["completed"],
                data=new_task["ID"],
                active_color="#EB895B",
                active_track_color="#FDB773",
                inactive_thumb_color="#A14646",
                inactive_track_color="#DA6556",
                on_change=switch_change
            ),
            ft.Button(
                "Delete Task",
                icon=ft.Icons.DELETE,
                bgcolor="#DA6556",
                color="white",
                data=new_task["ID"],
                on_click=delete_clicked,
            )
            ])

        column.controls.append(
        ft.Container(
            item,
            data=new_task["ID"],
            width=480,
            height=80,
            bgcolor="#EB895B",
            border_radius=15,
            padding=10
        ))
        
        task_input.value = ""
        task_input.error = None
        selected_time.value = "No time selected"
        
        page.pop_dialog()
        page.update()
        
    
    #=============
    #tast input
    #=============  
    task_input = ft.TextField(
            label="Task",
            hint_text="Type your task here...",
            color="black",
            width=400,
            bgcolor="#FDB773",
            border_color="#DA6556",
            focused_border_color="#A14646",
            cursor_color="#A14646",
    )
    
    #=======
    #time
    #=======   
    selected_time = ft.Text(
            "No time selected",
            size=30,
            weight=ft.FontWeight.BOLD,
            color="#A14646"
        )     
        
    def time_selected(e):
        if e.control.value:
            selected_time.value = e.control.value.strftime("%I:%M %p")
            page.update()
                
    time_picker = ft.TimePicker(
        on_change=time_selected
    )
    def open_time_picker(e):
        page.show_dialog(time_picker)
    
    #========
    #popup
    #========
    popup = ft.AlertDialog(modal=True,
                           
                           title="Add Task",
                           content=ft.Column([
                                ft.Text("Task"),
                                task_input,
                                
                                ft.Row(
                                    controls=ft.Button(
                                        content=ft.Text("Choose time"),
                                        on_click=open_time_picker
                                        
                                       )),
                                
                                ft.Row(
                                    controls=(ft.Button(
                                        content=ft.Text("Close"),
                                        on_click=lambda e: page.pop_dialog()),
                                    ft.Button(
                                        content=ft.Text("Add"),
                                        on_click=add_task))
                                )
                                
                            ]),
                           bgcolor="#EB895B"
                        )
    
    #=============
    #add button
    #=============      
    add_BTN = ft.Button(content=ft.Text("+",size=25,text_align=ft.TextAlign.CENTER),
                        width=50,height=50,
                        bgcolor="#FDB773",
                        color="#EB895B",
                        on_click=open_popup,
                        style=ft.ButtonStyle(
                            shape=ft.RoundedRectangleBorder(radius=15),
                            elevation=4,
                            padding=0
                        )
    )
       
    #==============
    #page update
    #==============
    page.floating_action_button = add_BTN
    page.add(title_container,ft.Container(content=column,expand=True))
    

ft.run(main)