import re


def find_date(line):
  # First and Last
  pattern = r"(\w+) (\w+)[^\.]"
  result = re.findall(pattern,line)

  # First Middle Last
  pattern=r'(\w+) (\w+) (\w+)'
  result = result + re.findall(pattern,line)

  # First M. Last
  pattern=r'(\w+) (\w+\.) (\w+)'
  result = result + re.findall(pattern,line)
  
  # Mr., Ms., Mrs., Dr.
  pattern=r'(Mr\.|Ms\.|Mrs\.|Dr\.) (\w+)'
  result = result + re.findall(pattern,line)
  return result


f = open("names.txt")
for line in f.readlines():
  #print(line)
  result = find_date(line)
  if (len(result)>0):
    print(result)