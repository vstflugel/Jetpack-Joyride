from alarmexception import AlarmException
from getch import _getChUnix as getChar
import signal

def take_input():
    def alarmhandler(signum, frame):
        raise AlarmException
    
    def user_input(timeout=0.05):
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
        
    char = user_input()

    return char