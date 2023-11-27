import datetime
from io import TextIOWrapper

def has_the_program_run_today()-> bool:
    try:
        file:TextIOWrapper = open("text.txt", "r+", encoding="utf-8")
        datestr = file.read()
        if datestr != "" and datetime.date.today()!=datetime.date.fromisoformat(datestr):
            return True
        file.write(datetime.date.today().isoformat())
        return False
    except OSError:
        file:TextIOWrapper = open("text.txt", "w", encoding="utf-8")
        file.write(datetime.date.today().isoformat())
        return False

# has_the_program_run_today()
