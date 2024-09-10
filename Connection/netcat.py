import sys
import socket
import getopt
import threading
import subprocess


listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0



def main():
    global listen,command,upload, execute, tagret, upload_destination, port
    
    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[:1], "hle:t:p:cu", ["help","listen","execute","target","port","command","upload"])

    except getopt.GetoptError as err:
        print("Error")

    for o,a in opts:
        if o in("-h","--help"):
            usage()

        elif o in("-l","--listen"):
            listen = True

        elif o in("-c", "--commandshell"):
            command = True

        elif o in("u","--upload"):
            upload_destination = a

        elif o in("t", "--target"):
            target = a

        elif o in("-p", "--port"):
            port = int(a)

        else:
            assert False, "Unhandled Option"

        if not listen and len(target) and port > ):
            buffer = sys.stdin.read()

            client_sender(buffer)

        if listen:
            server_loop()



def usage():
    print("{TEXT}")
    sys.exit(0)


main()
