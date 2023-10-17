def main():
    sequence_of_elements = input().split()
    count_moves = 0
    
    while True:
        count_moves+= 1
        command = input()
        
        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)})")
            
        index1, index2 = map(int, command.split())
        
        
        if is_invalid_input(index1, index2, sequence_of_elements):
            pass
        
        
        
def is_invalid_input(index1, index2, sequence):
      return(
          index1 == index2
          or index1 < 0
          or index2 < 0
          or index1 >= len(sequence)
          or index2 >= len(sequence)
      )         