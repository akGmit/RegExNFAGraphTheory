"""Regex module contains functions for command line interface"""
import argparse
import match

def main():
  parser = argparse.ArgumentParser(description='Matching string against regular expression.')
  parser.add_argument('regex', type=str, help='A regular expression')
  parser.add_argument('filename', type=str, help='A file name containing strings')

  args = parser.parse_args()
  exec(args.regex, args.filename)

def exec(regex, filename):
  """Function to read reg ex from file and strings to match from file.
  Each line in files repressents regex or string.
  Output result to screen.
  """
  r = open(regex, "r")
  f = open(filename, "r")
  regexs = []
  strs = []
  for reg in r:
    regexs.append(reg.rstrip('\n'))
  for string in f:
    strs.append(string.rstrip('\n'))

  r.close()
  f.close()
  
  for reg in regexs:
    print('RegEx - ' + reg)
    for string in strs:
      print('{:<15} .... {}'.format(string, match.match(reg, string)))
    print()
if __name__ == '__main__':
    main()