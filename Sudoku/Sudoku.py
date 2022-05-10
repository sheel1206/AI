from typing import *
from utils import cross,chunk_string_by_len
ROWS = 'ABCDEFGHI'
COLS = '123456789'
boxes = cross(ROWS, COLS)
row_units = [cross(r,COLS) for r in ROWS]
col_units = [cross(ROWS,c) for c in COLS]
square_units = [cross(r,c) for r in chunk_string_by_len(ROWS) for c in
chunk_string_by_len(COLS)]
unit_list = row_units + col_units + square_units
def get_puzzle(complex:bool = False) -> str:
if complex:
return '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
return '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
def grid_values(puzzle:str,boxes:List[str],replace:bool=True) -> Dict[str,str]:
assert len(puzzle) == 81
return {key : ( '123456789' if value =='.' and replace else value) for key,value in
zip(boxes,puzzle)}
def display_sudoku(p_values:Dict[str,str]) -> None:
assert (len(p_values) == 81),"There must be 81 values in the dictionary."
max_len=len(max(list(p_values.values()),key=len))+2 #max length among all box
units
print(f"\n{' SUDOKU '.center(max_len*9,'=')}\n")
list_puzzle = list(p_values.items())
n=9 #step
for i in range(0,len(p_values),n):
row=''
for index,box in enumerate(list_puzzle[i:i+n]):
if (index > 1 and index < 9) and index % 3 == 0 :
row +='|' #to add a pipe in middle

row +=box[1].center(max_len)
print(row,'\n')
if i == 18 or i== 45 : #to add a decorative line in middle
pt='-'*(max_len*3) #tern
print('+'.join([pt,pt,pt]),'\n')
def find_peers(box:str) -> List[str]:
peers_list=[list for list in unit_list if box in list]
peers = list(set([item for sub_list in peers_list for item in sub_list if item !=box]))
return peers
def eliminate(grids:Dict[str,str]) -> Dict[str,str]:
for key,value in grids.items():
if len(value) > 1:
peers = find_peers(key)
peers_values = [grids.get(k) for k in peers if len(grids.get(k))==1]
for v in peers_values:
value=value.replace(v,"")
grids[key]=value
return grids
def only_choice(grids:Dict[str,str]) -> Dict[str,str]:
for unit in unit_list:
for digit in '123456789':
d_places = [box for box in unit if digit in grids[box]]
if len(d_places) == 1:
grids[d_places[0]] = digit
return grids
def reduce_puzzle(grids:Dict[str,str]) -> Union[Dict[str,str],bool]:
stalled = False
solved = False
while not stalled:
solved_values_before = len([value for value in grids.values() if
len(value)==1])#total units
grids = eliminate(grids)
grids = only_choice(grids)
solved_values_after = len([value for value in grids.values() if len(value)==1])#total
units
stalled = solved_values_before == solved_values_after
if len([box for box in grids.keys() if len(grids[box]) == 0]):
return False
return grids

def search(values:Dict[str,str])->Dict[str,str]:
values = reduce_puzzle(values)
if values is False:
return False ## Failed earlier
if all(len(values[s]) == 1 for s in boxes):
return values ## Solved!
n,k = min((len(v),k) for k,v in values.items() if len(v)>1)
for value in values[k]:
new_sudoku=values.copy()
new_sudoku[k]=value
attempt = search(new_sudoku,)
if attempt:
return attempt
def check_if_sudoku_solved(grids:Dict[str,str]) -> bool:
for unit in unit_list:
unit_values_sum = sum([int(grids.get(k)) for k in unit])
solved = unit_values_sum == 45
return solved
def main(display_units:bool=False):
if display_units:
print(f"boxes : \n{boxes}\n")
print(f"row_units : \n{row_units}\n")
print(f"col_units : \n{col_units}\n")
print(f"square_units : \n{square_units}\n")
print(f"unit_lists : \n{unit_list}\n")
puzzle = get_puzzle(complex=True)
print("\nUnsolved Sudoku.")
display_sudoku(grid_values(puzzle,boxes,replace=False))
print("\nSudoku with replaced dots by 1-9.")
grid_units = grid_values(puzzle,boxes)
display_sudoku(grid_units) #display replaced
print("\nSudoku with eliminated values.")
eliminated_values=eliminate(grid_units)
display_sudoku(eliminated_values) #display eliminated
print("\nSudoku after replacing with only choices.")
elimination_with_only_coices_values=only_choice(eliminated_values)
display_sudoku(elimination_with_only_coices_values)
print("\nSudoku after Constraint Propagation.")
reduced_puzzle_values=reduce_puzzle(eliminated_values)
display_sudoku(reduced_puzzle_values)

solved = check_if_sudoku_solved(reduced_puzzle_values)
if not solved:
print("\nThe SUDOKU is UnSolved and needs searching.")
print("Sudoku after Search.")
solved_puzzle_with_search=search(eliminated_values)
display_sudoku(solved_puzzle_with_search)
solved = check_if_sudoku_solved(solved_puzzle_with_search)
print(f'The SUDOKU is {"Solved" if solved else "UnSolved"}.')
if __name__ == "__main__":
main()