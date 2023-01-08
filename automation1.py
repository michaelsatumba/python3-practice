import os

def main():
  # List all files in a directory
  for root, dirs, files in os.walk("/mydir"):
    for file in files:
      print(file)

  # Check if a file exists
  if os.path.isfile("/mydir/myfile.txt"):
    print("File exists")
  else:
    print("File does not exist")

  # Rename a file
  os.rename("/mydir/myfile.txt", "/mydir/newname.txt")

  # Create a new directory
  os.makedirs("/mydir/newdir")

if __name__ == "__main__":
  main()
