#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    def arguments(*argv):
        return(len(argv))
    print(arguments(),'arguments.')
    print(str(argv))

