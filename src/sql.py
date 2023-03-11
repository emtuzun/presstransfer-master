import sqlite3

try:
    con = sqlite3.connect("data.db")
    cur = con.cursor()
except:
    print("Database Connection Failed!")

def create_part(part_name):
    try:
        cur.execute(f'create table {part_name} (robot, position, x_axis, y_axis, z_axis, a_axis, b_axis, c_axis, p_axis, q_axis)')
        return True
    except:
        return False
def delete_part(part_name):
    try:
        cur.execute(f'drop table {part_name}')
        return True
    except:
        return False
def edit_part(part_name, coordinates:list):
    cur.execute(f'insert into {part_name} values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', coordinates)
def list_part_names():
    cur.execute("select name from sqlite_master where type='table'")
    names = cur.fetchall()
    names = [names[i][0] for i in range(len(names))]
    return names
def list_part(part_name, robot):
    cur.execute(f'select * from {part_name} where robot={robot}')