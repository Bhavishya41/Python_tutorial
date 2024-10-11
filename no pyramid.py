# Determine the number of levels
levels = 4

for i in range(1,5):
    # Print leading spaces
    print(" " * (levels - i) , end="")

    # Print the pattern with the required spaces in between
    for j in range(1, i + 1):
        print(j, " ",end="")
    
    # Move to the next line
    print()