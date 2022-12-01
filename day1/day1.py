import os


def read_file(filepath: str):
  text_file = open(filepath, "r")
  return text_file.readlines()


def part_one(lines):
  max_count = 0
  cur_count = 0
  for line in lines: 
    if line == "\n":
      max_count = max(max_count, cur_count)
      cur_count = 0
    else:
      cur_count += int(line)
  print(max_count)


def part_two(lines):
  max_counts = [0, 0, 0] # will remain sorted highest to lowest (TODO max heap)
  cur_count = 0
  for line in lines:
    if line == "\n":
      # kick out min number if cur_count is bigger than any element of the array
      for i, elem in enumerate(max_counts):
        if cur_count > elem:
          max_counts = max_counts[:i] + [cur_count] + max_counts[i:-1]
          break 
      cur_count = 0
    else:
      cur_count += int(line)
  print(sum(max_counts))
    

  

if __name__ == "__main__":
  print(os.getcwd())
  lines = read_file("input.txt")
  part_one(lines)
  part_two(lines)
