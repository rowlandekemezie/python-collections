import anydbm
import os


def walk(som):
    for name in os.listdir(som):
        path = os.path.join(som, name)
        if os.path.isfile(path):
            print(path, name)
        else:
            walk(path)


def create_db():
    db = anydbm.open('row.db', 'c')
    db['row.png'] = 'This is rowland picture'
    print db
    for key in db:
        print key
    db.close()
# create_db()

walk(os.getcwd())
