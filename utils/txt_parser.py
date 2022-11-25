def openFile( file ):
    try:
        f = open( file, 'r' )
    except IOError:
        print("Error: file '%s' not found." % file)
        return None
    return f
