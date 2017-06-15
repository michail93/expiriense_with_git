if __name__=="__main__":

    import sys

    print(sys.platform, sys.version, sep="\n")
    for x in sys.path:
        print(x)
