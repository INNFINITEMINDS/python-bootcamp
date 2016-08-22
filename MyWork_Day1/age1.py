
import sys
import datetime as dt

def days_from_now(ndays):
    #stuff

def days_since(year, month, day):
    #stuff
    
if __name__ == "__main__":
    """
    Executed only if run from the command line.
      to list the days since that date, call with
      age1.py <year> <month> <day>
      
    or

      to list the dat in some number of days, use
      age1.py <days>
    """
    argstot = len(sys.argv)
    cmdargs = str(sys.argv)

    print("The total numbers of argumentss passed to the script: %d " % argstot)
    print ("Arguments list: %s " % cmdargs)

    if argstot == 2:
        result = days_from_now(int(sys.argv[1]))
    elif argstot == 4:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        day = int(sys.argv[3])
        result = days_since(year, month, day)
    else:
        print("This program takes only 1 or 3 arguments; you have supplied:" argstot)
        break