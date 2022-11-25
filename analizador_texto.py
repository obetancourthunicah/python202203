from utils.txt_parser import openFile

def main():
  f = openFile( './data/meeting_saved_chat.txt' )
  if f is None:
    return
  for line in f:
    print(line)

main()
