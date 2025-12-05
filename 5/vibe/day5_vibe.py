"""
Advent of Code Day 5 - Ingredient Freshness Checker

The database contains:
1. Fresh ingredient ID ranges (inclusive, can overlap)
2. A blank line
3. Available ingredient IDs

We need to determine which available IDs are fresh (fall into any range).
"""

from typing import List, Tuple
import sys


class IngredientDatabase:
    """Manages ingredient ranges and checks freshness."""
    
    def __init__(self, ranges: List[Tuple[int, int]]):
        """
        Initialize with fresh ingredient ranges.
        
        Args:
            ranges: List of (start, end) tuples representing inclusive ranges
        """
        self.ranges = ranges
    
    def is_fresh(self, ingredient_id: int) -> bool:
        """
        Check if an ingredient ID is fresh (falls into any range).
        
        Args:
            ingredient_id: The ingredient ID to check
            
        Returns:
            True if the ID falls into any fresh range, False otherwise
        """
        for start, end in self.ranges:
            if start <= ingredient_id <= end:
                return True
        return False
    
    def count_fresh(self, ingredient_ids: List[int]) -> int:
        """
        Count how many of the given ingredient IDs are fresh.
        
        Args:
            ingredient_ids: List of ingredient IDs to check
            
        Returns:
            Number of fresh ingredient IDs
        """
        return sum(1 for ingredient_id in ingredient_ids if self.is_fresh(ingredient_id))
    
    def _merge_ranges(self) -> List[Tuple[int, int]]:
        """
        Merge overlapping ranges into non-overlapping intervals.
        
        Returns:
            List of merged (start, end) tuples
        """
        if not self.ranges:
            return []
        
        # Sort ranges by start value
        sorted_ranges = sorted(self.ranges, key=lambda x: x[0])
        merged = [sorted_ranges[0]]
        
        for current_start, current_end in sorted_ranges[1:]:
            last_start, last_end = merged[-1]
            
            # If current range overlaps or is adjacent to the last merged range
            if current_start <= last_end + 1:
                # Merge: extend the end if needed
                merged[-1] = (last_start, max(last_end, current_end))
            else:
                # No overlap, add as new range
                merged.append((current_start, current_end))
        
        return merged
    
    def get_all_fresh_ids(self) -> set:
        """
        Get all unique ingredient IDs that are considered fresh by any range.
        
        Note: For very large ranges, this may be memory-intensive.
        Use count_all_fresh_ids() for efficient counting without storing all IDs.
        
        Returns:
            Set of all fresh ingredient IDs
        """
        fresh_ids = set()
        for start, end in self.ranges:
            # Only expand ranges if they're reasonably small (less than 1M IDs)
            if end - start < 1_000_000:
                fresh_ids.update(range(start, end + 1))
            else:
                # For large ranges, just store the range bounds
                # This is a fallback - count_all_fresh_ids() is preferred
                raise ValueError("Range too large to expand into set. Use count_all_fresh_ids() instead.")
        return fresh_ids
    
    def count_all_fresh_ids(self) -> int:
        """
        Count how many unique ingredient IDs are considered fresh by the ranges.
        Uses efficient range merging to avoid memory issues with large ranges.
        
        Returns:
            Number of unique fresh ingredient IDs
        """
        merged_ranges = self._merge_ranges()
        total = 0
        for start, end in merged_ranges:
            total += (end - start + 1)  # +1 because ranges are inclusive
        return total


def parse_range(range_str: str) -> Tuple[int, int]:
    """
    Parse a range string like "3-5" into a tuple (3, 5).
    
    Args:
        range_str: String in format "start-end"
        
    Returns:
        Tuple of (start, end) integers
    """
    start, end = range_str.split("-")
    return (int(start), int(end))


def parse_database(input_text: str) -> Tuple[List[Tuple[int, int]], List[int]]:
    """
    Parse the database input into ranges and ingredient IDs.
    
    Args:
        input_text: The full database text
        
    Returns:
        Tuple of (ranges, ingredient_ids)
    """
    lines = input_text.strip().split("\n")
    
    ranges = []
    ingredient_ids = []
    
    # Find the blank line separator
    blank_line_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "":
            blank_line_idx = i
            break
    
    if blank_line_idx is None:
        raise ValueError("No blank line found separating ranges from ingredient IDs")
    
    # Parse ranges (before blank line)
    for line in lines[:blank_line_idx]:
        if line.strip():  # Skip empty lines
            ranges.append(parse_range(line.strip()))
    
    # Parse ingredient IDs (after blank line)
    for line in lines[blank_line_idx + 1:]:
        if line.strip():  # Skip empty lines
            ingredient_ids.append(int(line.strip()))
    
    return ranges, ingredient_ids


def main():
    """Main entry point."""
    # Read input from stdin or file
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            input_text = f.read()
    else:
        input_text = sys.stdin.read()
    
    # Parse the database
    ranges, ingredient_ids = parse_database(input_text)
    
    # Create database
    db = IngredientDatabase(ranges)
    
    # Part 1: Count fresh ingredients from available IDs
    part1_count = db.count_fresh(ingredient_ids)
    
    # Part 2: Count all unique fresh IDs from ranges
    part2_count = db.count_all_fresh_ids()
    
    print(f"Part 1: {part1_count}")
    print(f"Part 2: {part2_count}")


if __name__ == "__main__":
    main()

