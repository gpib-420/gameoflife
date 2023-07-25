from datetime import datetime as dt


def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return f"{dt_:{fmt}}"


def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)


def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(element, class_name):
    element.element.classList.add(class_name)

def roomIdFromName(input):
    code_1 = ord(input[0])*2**32
    code_2 = ord(input[1])*2**16
    code_3 = ord(input[2])*2**0

    result = code_1+code_2+code_3

    return result

def openRoom(room_name:str):
    print('YOU ARE IN ROOM %s'%room_name)
    print('checking the database...')
    print('looking for room %s'%room_name+' with ID %s'%int(roomIdFromName(room_name)))
    database = 0
    print('do mysql things with that database and get all comments for room %s' % room_name)
    print('if no comments for %s, create that room' % room_name)
    print('if found comments for %s, open room and populate with comments' % room_name)


# define class room
class room(object):
    id=0
    name='000'
    html_page = None
    def __init__(self,args=0):
        print('room created. Id %d'%self.id)





    
