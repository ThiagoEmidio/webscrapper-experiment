import win32com.client

def create_scheduled_task():
    scheduler:win32com.client.CDispatch = win32com.client.Dispatch("Schedule.Service")
    scheduler.Connect()

    root_folder = scheduler.GetFolder("\\")
    task_definition = scheduler.NewTask(0)

    with open("task.xml", "r", encoding="UTF-16") as xml_file:
        xml_content = xml_file.read()

    task_definition.XmlText = xml_content
    root_folder.RegisterTaskDefinition('Task', task_definition, 6, '','',0)


