import sys
import logging

def main(command:str):

    logging.info(command)

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)

    if len(sys.argv) < 2:
        command = 'none'
    else:
        command = sys.argv[1]

    main(command=command)