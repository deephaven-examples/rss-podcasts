"""
run_script.py

A Python script that runs a secondary Python script in Deephaven.

@copyright Deephaven Data Labs
"""
from pydeephaven import Session, DHError

import sys
import time

def main(script_paths: list, host: str, max_retries: int):
    """
    Main method for the script. Simply runs the Python scripts in the given paths
    on the Deephaven server.

    Parameters:
        script_path (list[str]): A list of paths to the Python scripts to run
        host (str): The host name of the Deephaven instance
        max_retries (int): The maximum attempts to retry connecting to Deephaven

    Returns:
        None
    """
    print("Attempting to connect to host at")
    print(host)
    session = None

    #Simple retry loop in case the server tries to launch before Deephaven is ready
    count = 0
    while (count < max_retries):
        try:
            session = Session(host=host)
            print("Connected to Deephaven")
            break
        except DHError as e:
            print("Failed to connect to Deephaven... Waiting to try again")
            print(e)
            time.sleep(5)
            count += 1
        except Exception as e:
            print("Unknown error when connecting to Deephaven... Waiting to try again")
            print(e)
            time.sleep(5)
            count += 1
    if session is None:
        sys.exit(f"Failed to connect to Deephaven after {max_retries} attempts")

    for script_path in script_paths:
        with open(script_path) as f:
            print(f"Running script at {script_path}")
            script_string = f.read()
            try:
                session.run_script(script_string)
            except DHError as e:
                print(e)
                sys.exit(f"Deephaven error when trying to run the script at {script_path}")
            except Exception as e:
                print(e)
                sys.exit(f"Unexpected error when trying to run the script at {script_path}")

usage = """
usage: python run_script.py script-paths host max-retries
"""

if __name__ == '__main__':
    if len(sys.argv) > 4:
        sys.exit(usage)

    try:
        script_paths = sys.argv[1].split(",")
        host = sys.argv[2]
        max_retries = int(sys.argv[3])
    except:
        sys.exit(usage)

    main(script_paths, host, max_retries)
