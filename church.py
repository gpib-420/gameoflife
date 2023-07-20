from datetime import datetime as dt


def format_date(dt_, fmt="%m/%d/%Y, %H:%M:%S"):
    return f"{dt_:{fmt}}"


def now(fmt="%m/%d/%Y, %H:%M:%S"):
    return format_date(dt.now(), fmt)


def remove_class(element, class_name):
    element.element.classList.remove(class_name)


def add_class(element, class_name):
    element.element.classList.add(class_name)

def roomIdFromName(input) {
code_1 = input[0].charCodeAt(0)*2**32
code_2 = input[1].charCodeAt(0)*2**16
code_3 = input[2].charCodeAt(0)*2**0

result = code_1+code_2+code_3

return result
}


}
def openRoom(room_name:str):
    print('YOU ARE IN ROOM %s'%room_name)
    print('checking the database...')
    print('looking for room %s'%room_name+'with ID %s'%int(roomIdFromName(room_name)))
    
