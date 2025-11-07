"""
Core notebook merge functionality
"""
from pathlib import Path
from typing import List, Dict, Any, Optional
import nbformat
from nbformat.notebooknode import NotebookNode
import difflib


class MergeConflict:
    """Represents a merge conflict in a cell"""
    
    def __init__(self, cell_index: int, cell_type: str, base_content: str, 
                 ours_content: str, theirs_content: str):
        self.cell_index = cell_index
        self.cell_type = cell_type
        self.base_content = base_content
        self.ours_content = ours_content
        self.theirs_content = theirs_content
    
    def create_conflict_cell(self) -> NotebookNode:
        """Create a cell with conflict markers"""
        conflict_content = f"""<<<<<<< OURS
{self.ours_content}
=======
{self.theirs_content}
>>>>>>> THEIRS"""
        
        if self.cell_type == 'code':
            return nbformat.v4.new_code_cell(conflict_content)
        elif self.cell_type == 'markdown':
            return nbformat.v4.new_markdown_cell(conflict_content)
        else:
            return nbformat.v4.new_raw_cell(conflict_content)


class NotebookMerger:
    """Handles 3-way merge of notebooks"""
    
    def __init__(self, base_path: Path, ours_path: Path, theirs_path: Path):
        self.base_path = base_path
        self.ours_path = ours_path
        self.theirs_path = theirs_path
        
        self.base_nb = self._load_notebook(base_path)
        self.ours_nb = self._load_notebook(ours_path)
        self.theirs_nb = self._load_notebook(theirs_path)
        
        self.merged_nb: Optional[NotebookNode] = None
        self.conflicts: List[MergeConflict] = []
        self.stats = {
            'cells_merged': 0,
            'conflicts': 0,
            'cells_from_ours': 0,
            'cells_from_theirs': 0,
            'cells_unchanged': 0,
        }
    
    def _load_notebook(self, path: Path) -> NotebookNode:
        """Load a notebook from file"""
        with open(path, 'r', encoding='utf-8') as f:
            return nbformat.read(f, as_version=4)
    
    def _normalize_cell(self, cell) -> str:
        """Normalize cell content for comparison"""
        return cell.source.strip()
    
    def _cells_equal(self, cell1, cell2) -> bool:
        """Check if two cells are equal"""
        if cell1 is None or cell2 is None:
            return False
        if cell1.cell_type != cell2.cell_type:
            return False
        return self._normalize_cell(cell1) == self._normalize_cell(cell2)
    
    def merge(self, strategy: str = 'auto') -> NotebookNode:
        """
        Perform 3-way merge
        
        Args:
            strategy: Merge strategy - 'auto', 'ours', 'theirs', 'cell-append'
        
        Returns:
            Merged notebook
        """
        if strategy == 'ours':
            return self._merge_strategy_ours()
        elif strategy == 'theirs':
            return self._merge_strategy_theirs()
        elif strategy == 'cell-append':
            return self._merge_strategy_append()
        else:
            return self._merge_auto()
    
    def _merge_auto(self) -> NotebookNode:
        """Automatic 3-way merge with conflict detection"""
        # Create new notebook
        self.merged_nb = nbformat.v4.new_notebook()
        
        # Copy metadata from base (could be smarter)
        self.merged_nb.metadata = self.base_nb.metadata.copy()
        
        # Get cells from each version
        base_cells = self.base_nb.cells
        ours_cells = self.ours_nb.cells
        theirs_cells = self.theirs_nb.cells
        
        # Use 3-way diff to merge
        merged_cells = self._three_way_merge_cells(base_cells, ours_cells, theirs_cells)
        self.merged_nb.cells = merged_cells
        
        return self.merged_nb
    
    def _three_way_merge_cells(self, base_cells, ours_cells, theirs_cells) -> List:
        """Perform 3-way merge on cell lists"""
        merged = []
        
        # Convert cells to comparable strings
        base_strs = [self._normalize_cell(c) for c in base_cells]
        ours_strs = [self._normalize_cell(c) for c in ours_cells]
        theirs_strs = [self._normalize_cell(c) for c in theirs_cells]
        
        # Find changes from base to ours and base to theirs
        ours_matcher = difflib.SequenceMatcher(None, base_strs, ours_strs)
        theirs_matcher = difflib.SequenceMatcher(None, base_strs, theirs_strs)
        
        # Track which cells we've processed
        base_idx = 0
        ours_idx = 0
        theirs_idx = 0
        
        # Simple merge: take cells from both sides
        # If both modified same cell, create conflict
        max_len = max(len(base_cells), len(ours_cells), len(theirs_cells))
        
        for i in range(max_len):
            base_cell = base_cells[i] if i < len(base_cells) else None
            ours_cell = ours_cells[i] if i < len(ours_cells) else None
            theirs_cell = theirs_cells[i] if i < len(theirs_cells) else None
            
            # Case 1: All three are the same or two are the same
            if self._cells_equal(base_cell, ours_cell) and self._cells_equal(base_cell, theirs_cell):
                # No changes
                if base_cell:
                    merged.append(base_cell)
                    self.stats['cells_unchanged'] += 1
            
            elif self._cells_equal(base_cell, ours_cell) and not self._cells_equal(base_cell, theirs_cell):
                # Only theirs changed - take theirs
                if theirs_cell:
                    merged.append(theirs_cell)
                    self.stats['cells_from_theirs'] += 1
            
            elif self._cells_equal(base_cell, theirs_cell) and not self._cells_equal(base_cell, ours_cell):
                # Only ours changed - take ours
                if ours_cell:
                    merged.append(ours_cell)
                    self.stats['cells_from_ours'] += 1
            
            elif self._cells_equal(ours_cell, theirs_cell):
                # Both changed to same thing - take either
                if ours_cell:
                    merged.append(ours_cell)
                    self.stats['cells_merged'] += 1
            
            else:
                # Both changed differently - conflict!
                if base_cell and ours_cell and theirs_cell:
                    conflict = MergeConflict(
                        cell_index=len(merged),
                        cell_type=base_cell.cell_type,
                        base_content=base_cell.source,
                        ours_content=ours_cell.source,
                        theirs_content=theirs_cell.source
                    )
                    self.conflicts.append(conflict)
                    merged.append(conflict.create_conflict_cell())
                    self.stats['conflicts'] += 1
                elif ours_cell:
                    merged.append(ours_cell)
                    self.stats['cells_from_ours'] += 1
                elif theirs_cell:
                    merged.append(theirs_cell)
                    self.stats['cells_from_theirs'] += 1
        
        # Handle any remaining cells
        if len(ours_cells) > len(base_cells):
            for cell in ours_cells[len(base_cells):]:
                merged.append(cell)
                self.stats['cells_from_ours'] += 1
        
        if len(theirs_cells) > len(base_cells):
            for cell in theirs_cells[len(base_cells):]:
                merged.append(cell)
                self.stats['cells_from_theirs'] += 1
        
        return merged
    
    def _merge_strategy_ours(self) -> NotebookNode:
        """Take our version in conflicts"""
        self.merged_nb = self.ours_nb
        self.stats['cells_from_ours'] = len(self.ours_nb.cells)
        return self.merged_nb
    
    def _merge_strategy_theirs(self) -> NotebookNode:
        """Take their version in conflicts"""
        self.merged_nb = self.theirs_nb
        self.stats['cells_from_theirs'] = len(self.theirs_nb.cells)
        return self.merged_nb
    
    def _merge_strategy_append(self) -> NotebookNode:
        """Append both versions (keep all cells)"""
        self.merged_nb = nbformat.v4.new_notebook()
        self.merged_nb.metadata = self.base_nb.metadata.copy()
        
        # Add all cells from ours
        for cell in self.ours_nb.cells:
            self.merged_nb.cells.append(cell)
            self.stats['cells_from_ours'] += 1
        
        # Add separator
        separator = nbformat.v4.new_markdown_cell("---\n**Merged from other branch:**")
        self.merged_nb.cells.append(separator)
        
        # Add all cells from theirs
        for cell in self.theirs_nb.cells:
            self.merged_nb.cells.append(cell)
            self.stats['cells_from_theirs'] += 1
        
        return self.merged_nb
    
    def save(self, output_path: Path):
        """Save merged notebook"""
        if self.merged_nb is None:
            raise ValueError("No merged notebook to save. Call merge() first.")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(self.merged_nb, f)
    
    def has_conflicts(self) -> bool:
        """Check if merge has conflicts"""
        return len(self.conflicts) > 0
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get merge statistics"""
        return self.stats.copy()

