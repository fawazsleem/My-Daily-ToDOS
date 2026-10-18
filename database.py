import sqlite3 as lite
import datetime as dt

datebase = lite.connect('todo.db')
cursur = datebase.cursor()
cursur.execute("""CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    complete_time TEXT,
                    task_entrytime TEXT,
                    completed INTEGER DEFAULT 0
                )""")


def task_entry(task_name,task_time):
    entry_time = dt.datetime.now()
    task = (task_name ,task_time ,entry_time)
    cursur.execute("INSERT INTO tasks (task,complete_time,task_entrytime) VALUES (?,?,?)",task)

    datebase.commit()

def delete_task(task_id):
    cursur.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )
    datebase.commit()
    
def update_task(task_id,completed):

    cursur.execute("UPDATE tasks SET completed=? WHERE ID=?",(completed,task_id))
    datebase.commit()

def get_task():
    tasks = []
    cursur.execute("SELECT * FROM tasks")
    for id,taskname,completetime,tasktime,completed in cursur.fetchall():
        task = {"ID":id,
                "task name":taskname,
                "entry time":tasktime,
                "task complete time":completetime,
                "completed":bool(completed)}
        tasks.append(task)
    
    return tasks


 
