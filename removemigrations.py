import os
list_project_path_content = os.listdir()
for project_path_item in list_project_path_content:
    if not project_path_item.endswith(".py"):
        try:
            list_path_content = os.listdir(
                "{}/migrations/".format(project_path_item))
            for item in list_path_content:
                if item.endswith(".py") and not item.startswith("__"):
                    os.system(
                        "rm {}/migrations/{}".format(project_path_item, item))
                    print(project_path_item + "/" + item + " removed")
        except:
            print("No migrations found")
os.system("find . -path '*/migrations/*.pyc' -delete")
print("End")
