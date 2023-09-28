""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    get_shutdown_events returns log entries were shutdown was initiated
    """
    with open(logfile,'r') as f:
        events = []
        for event in f:
            if 'Shutdown initiated' in event:
                events.append(event)
        return events
        


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
