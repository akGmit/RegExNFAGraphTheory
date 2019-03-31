import argparse
import match

def main():
  parser = argparse.ArgumentParser(description='Matching string against regular expression.')
  parser.add_argument('regex', type=str, help='A regular expression')
  parser.add_argument('filename', type=str, help='A file name containing strings')

  args = parser.parse_args()

  print(args.regex)
  print(args.filename)

if __name__ == '__main__':
    main()