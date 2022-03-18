import os

# get all files with same name
files = []
for file in os.listdir("."):
    if file.startswith("dbsiga"):
        files.append(file.split(".")[0])
# sort files
file_name = "dbsiga_1.json"
if len(files):
    files.sort()
    print(files[-1])
    file_name = "dbsiga_{}.json".format(int(files[-1].split("_")[1]) + 1)
print(file_name)
os.system(
    "docker-compose run --service-ports web python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > {}".format(file_name))
