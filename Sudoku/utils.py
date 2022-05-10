from typing import List
def cross(row: str, col: str) -> List[str]:
return [r + c for r in row for c in col]
def chunk_string_by_len(string: str, n: int = 3) -> List[str]:
return [string[i:i+n] for i in range(0, len(string), n)]