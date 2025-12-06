"""
Advent of Code Day 6 - Cephalopod Math Worksheet

The worksheet contains math problems arranged vertically:
- Numbers are stacked in columns
- Operators are at the bottom row
- Problems are separated by full columns of spaces
- Each problem needs to be solved and all results summed
"""

from typing import List, Tuple, Optional
import sys


class MathProblem:
    """Represents a single math problem with numbers and an operator."""
    
    def __init__(self, numbers: List[int], operator: str):
        """
        Initialize a math problem.
        
        Args:
            numbers: List of numbers to operate on
            operator: The operation to perform ('+' or '*')
        """
        self.numbers = numbers
        self.operator = operator
    
    def solve(self) -> int:
        """
        Solve the math problem.
        
        Returns:
            The result of applying the operator to all numbers
        """
        if not self.numbers:
            return 0
        
        if self.operator == '+':
            return sum(self.numbers)
        elif self.operator == '*':
            result = 1
            for num in self.numbers:
                result *= num
            return result
        else:
            raise ValueError(f"Unknown operator: {self.operator}")
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        op_str = f" {self.operator} ".join(str(n) for n in self.numbers)
        return f"{op_str} = {self.solve()}"


class MathWorksheet:
    """Parses and solves a cephalopod math worksheet."""
    
    def __init__(self, lines: List[str], right_to_left: bool = False):
        """
        Initialize with worksheet lines.
        
        Args:
            lines: List of strings representing each row of the worksheet
            right_to_left: If True, parse numbers right-to-left in columns
        """
        self.lines = [line.rstrip('\n') for line in lines]
        self.problems: List[MathProblem] = []
        self.right_to_left = right_to_left
    
    def parse(self):
        """Parse the worksheet and extract all problems."""
        if not self.lines:
            return
        
        # Find the operator row (last non-empty line)
        operator_row_idx = None
        for i in range(len(self.lines) - 1, -1, -1):
            if self.lines[i].strip():
                operator_row_idx = i
                break
        
        if operator_row_idx is None:
            return
        
        # Get the maximum width of any line
        max_width = max(len(line) for line in self.lines)
        
        # Parse column by column
        if self.right_to_left:
            problems = self._extract_problems_right_to_left(max_width, operator_row_idx)
        else:
            problems = self._extract_problems(max_width, operator_row_idx)
        self.problems = problems
    
    def _extract_problems(
        self, 
        max_width: int, 
        operator_row_idx: int
    ) -> List[MathProblem]:
        """
        Extract problems by analyzing columns.
        
        Args:
            max_width: Maximum width of any line
            operator_row_idx: Index of the row containing operators
            
        Returns:
            List of MathProblem objects
        """
        problems = []
        col = 0
        
        while col < max_width:
            # Check if this column is part of a problem or a separator
            if self._is_separator_column(col):
                col += 1
                continue
            
            # Extract a problem starting at this column
            problem, next_col = self._extract_problem_at_column(
                col, 
                max_width, 
                operator_row_idx
            )
            
            if problem:
                problems.append(problem)
            
            col = next_col
        
        return problems
    
    def _is_separator_column(self, col: int) -> bool:
        """
        Check if a column is a separator (all spaces).
        
        Args:
            col: Column index to check
            
        Returns:
            True if the column contains only spaces
        """
        for line in self.lines:
            if col < len(line) and line[col] != ' ':
                return False
        return True
    
    def _extract_problem_at_column(
        self, 
        start_col: int, 
        max_width: int, 
        operator_row_idx: int
    ) -> Tuple[Optional[MathProblem], int]:
        """
        Extract a single problem starting at a given column.
        
        Args:
            start_col: Starting column index
            max_width: Maximum width of any line
            operator_row_idx: Index of the row containing operators
            
        Returns:
            Tuple of (MathProblem or None, next_column_index)
        """
        numbers = []
        operator = None
        col = start_col
        
        # Find the end of this problem (next separator column)
        end_col = start_col
        while end_col < max_width and not self._is_separator_column(end_col):
            end_col += 1
        
        # Extract numbers from each row (except the operator row)
        for row_idx in range(len(self.lines)):
            if row_idx == operator_row_idx:
                # Extract operator from this row
                operator = self._extract_operator_in_range(
                    self.lines[row_idx], 
                    start_col, 
                    end_col
                )
            else:
                # Extract number from this row
                number = self._extract_number_in_range(
                    self.lines[row_idx], 
                    start_col, 
                    end_col
                )
                if number is not None:
                    numbers.append(number)
        
        if operator and numbers:
            return MathProblem(numbers, operator), end_col + 1
        
        return None, end_col + 1
    
    def _extract_number_in_range(
        self, 
        line: str, 
        start_col: int, 
        end_col: int
    ) -> Optional[int]:
        """
        Extract a number from a line within a column range.
        Numbers may be left/right aligned, so we look for digits.
        
        Args:
            line: The line to extract from
            start_col: Start of the column range
            end_col: End of the column range (exclusive)
            
        Returns:
            Integer if found, None otherwise
        """
        # Extract the substring for this column range
        if start_col >= len(line):
            return None
        
        segment = line[start_col:end_col].strip()
        
        if not segment:
            return None
        
        # Try to parse as integer
        try:
            return int(segment)
        except ValueError:
            return None
    
    def _extract_operator_in_range(
        self, 
        line: str, 
        start_col: int, 
        end_col: int
    ) -> Optional[str]:
        """
        Extract an operator from a line within a column range.
        
        Args:
            line: The line to extract from
            start_col: Start of the column range
            end_col: End of the column range (exclusive)
            
        Returns:
            Operator character ('+' or '*') if found, None otherwise
        """
        if start_col >= len(line):
            return None
        
        segment = line[start_col:end_col].strip()
        
        if segment in ['+', '*']:
            return segment
        
        return None
    
    def solve_all(self) -> int:
        """
        Solve all problems and return the grand total.
        
        Returns:
            Sum of all problem solutions
        """
        if not self.problems:
            self.parse()
        
        total = 0
        for problem in self.problems:
            total += problem.solve()
        
        return total
    
    def _extract_problems_right_to_left(
        self, 
        max_width: int, 
        operator_row_idx: int
    ) -> List[MathProblem]:
        """
        Extract problems reading right-to-left, with numbers in individual columns.
        
        Args:
            max_width: Maximum width of any line
            operator_row_idx: Index of the row containing operators
            
        Returns:
            List of MathProblem objects
        """
        problems = []
        col = max_width - 1  # Start from the rightmost column
        
        while col >= 0:
            # Check if this column is part of a problem or a separator
            if self._is_separator_column(col):
                col -= 1
                continue
            
            # Extract a problem starting at this column (reading right-to-left)
            problem, next_col = self._extract_problem_right_to_left_at_column(
                col, 
                operator_row_idx
            )
            
            if problem:
                problems.append(problem)
            
            col = next_col
        
        return problems
    
    def _extract_problem_right_to_left_at_column(
        self, 
        start_col: int, 
        operator_row_idx: int
    ) -> Tuple[Optional[MathProblem], int]:
        """
        Extract a single problem reading right-to-left.
        Each number occupies its own column, with digits stacked vertically.
        
        Args:
            start_col: Starting column index (rightmost column of the problem)
            operator_row_idx: Index of the row containing operators
            
        Returns:
            Tuple of (MathProblem or None, next_column_index)
        """
        numbers = []
        operator = None
        
        # Find the left boundary of this problem (next separator column to the left)
        left_col = start_col
        while left_col >= 0 and not self._is_separator_column(left_col):
            left_col -= 1
        left_col += 1  # Move back to first non-separator column
        
        # Extract numbers by reading columns right-to-left
        # Each number is in its own column, digits stacked top-to-bottom
        col = start_col
        
        while col >= left_col:
            # Check if this column has any digits (excluding operator row)
            column_digits = []
            
            for row_idx in range(len(self.lines)):
                if row_idx == operator_row_idx:
                    # Check for operator in this column
                    if col < len(self.lines[row_idx]):
                        char = self.lines[row_idx][col]
                        if char in ['+', '*']:
                            operator = char
                    continue
                
                if col < len(self.lines[row_idx]):
                    char = self.lines[row_idx][col]
                    if char.isdigit():
                        # Store digit with its row index for proper ordering
                        column_digits.append((row_idx, char))
            
            if column_digits:
                # This column contains a number (digits stacked top-to-bottom)
                # Sort digits by row index (top to bottom)
                column_digits.sort(key=lambda x: x[0])
                # Extract digits in order and form the number
                digits_str = ''.join(digit for _, digit in column_digits)
                try:
                    numbers.append(int(digits_str))
                except ValueError:
                    pass
            
            col -= 1
        
        # Reverse numbers since we read right-to-left but want left-to-right order
        numbers.reverse()
        
        if operator and numbers:
            return MathProblem(numbers, operator), left_col - 1
        
        return None, left_col - 1
    
    def get_problem_count(self) -> int:
        """Get the number of problems in the worksheet."""
        if not self.problems:
            self.parse()
        return len(self.problems)


def parse_worksheet(input_text: str, right_to_left: bool = False) -> MathWorksheet:
    """
    Parse input text into a MathWorksheet.
    
    Args:
        input_text: The worksheet text
        right_to_left: If True, parse numbers right-to-left in columns
        
    Returns:
        MathWorksheet object
    """
    lines = input_text.strip().split('\n')
    worksheet = MathWorksheet(lines, right_to_left=right_to_left)
    worksheet.parse()
    return worksheet


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Solve cephalopod math worksheet')
    parser.add_argument('input_file', nargs='?', help='Input file (or read from stdin)')
    parser.add_argument('--part2', action='store_true', help='Use right-to-left parsing')
    args = parser.parse_args()
    
    # Read input from stdin or file
    if args.input_file:
        with open(args.input_file, "r") as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    # Parse and solve the worksheet
    worksheet = parse_worksheet(input_text, right_to_left=args.part2)
    
    # Calculate grand total
    grand_total = worksheet.solve_all()
    
    part_label = "Part 2" if args.part2 else "Part 1"
    print(f"{part_label}: {grand_total}")


if __name__ == "__main__":
    main()

