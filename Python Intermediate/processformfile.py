def process_numbers():
    try:
        
        with open(r"c:\Users\acer\OneDrive\Desktop\AI MI RESEARCH INTERN\Python Intermediate\numbers.txt", "r") as f:
            numbers = [int(line.strip()) for line in f if line.strip()]
        
       
        total = sum(numbers)
        average = total / len(numbers)
        
        
        with open("results.txt", "w") as f:
            f.write(f"Total: {total}\n")
            f.write(f"Average: {average:.2f}\n")
            f.write(f"Count: {len(numbers)}\n")
        
        print("Processing complete!")
        
    except FileNotFoundError:
        print("Input file not found!")
    except ValueError:
        print("Invalid number format in file!")
    except ZeroDivisionError:
        print("No numbers to process!")


process_numbers()