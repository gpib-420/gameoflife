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
    rmid = int(roomIdFromName(room_name))
    print('looking for room %s'%room_name+' with ID %d'%rmid)
    database = 0
    print('do mysql things with that database and get all comments for room %s' % room_name)
    print('if no comments for %s, create that room' % room_name)
    print('if found comments for %s, open room and populate with comments' % room_name)
    newRoom = room(name=room_name)
    return room

def connect_to_database():
    # test mysql module for the database
    import mysql.connector

    print('searching for sinners.')

    try:
        mydb = mysql.connector.connect(user='rstx', password="basedbase666", host="http://loser.church", database="sinners")

        # Printing the connection object
        print(mydb)

        return(mydb)

    except:
        print('can''t connect to db on loser.church')
        return(-1)

# define class room
class room(object):
    id=0
    name='000'
    html_page = None
    def __init__(self,name=None):
        if name:
            self.id = int(roomIdFromName(name))
            try:
                db = connect_to_database() # connect to db, get db to do stuff
            except:
                print('cant access db on loser.church')

            print('room being created. Id %d'%self.id)
            loserPageTemplate = '''
                    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
                    <html>
                    <head>
                        <meta content="text/html; charset=ISO-8859-1"
                        http-equiv="content-type">
                        <title>{room}</title>
                    </head>
                    <body>
                    room {room}
                    <hr>
                    <div>
                        <input id="comment" maxlength="64" class="input" type="text" placeholder="sin">
                        <button id="post-comment-btn" class="py-button" type="submit" py-click="post_comment()">
                        enter
                        </button>
                    </div>
                    <hr>
                    sys: id {id}
                    </body>
                    </html>'''  # NEW note '{person}' two lines up

            self.html_page = loserPageTemplate.format(room=self.name, id=self.id)

