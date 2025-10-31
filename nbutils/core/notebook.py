"""
Core notebook handling functionality
"""
from pathlib import Path
from typing import Dict, Any, List
import nbformat
from nbformat.notebooknode import NotebookNode


class Notebook:
    """Represents a Jupyter notebook with utility methods"""
    
    def __init__(self, path: Path):
        self.path = path
        self.nb: NotebookNode = self._load()
    
    def _load(self) -> NotebookNode:
        """Load notebook from file"""
        with open(self.path, 'r', encoding='utf-8') as f:
            return nbformat.read(f, as_version=4)
    
    def save(self, output_path: Path = None) -> None:
        """Save notebook to file"""
        target = output_path or self.path
        with open(target, 'w', encoding='utf-8') as f:
            nbformat.write(self.nb, f)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get basic statistics about the notebook"""
        stats = {
            'total_cells': len(self.nb.cells),
            'code_cells': 0,
            'markdown_cells': 0,
            'raw_cells': 0,
            'file_size': self.path.stat().st_size,
        }
        
        for cell in self.nb.cells:
            if cell.cell_type == 'code':
                stats['code_cells'] += 1
            elif cell.cell_type == 'markdown':
                stats['markdown_cells'] += 1
            elif cell.cell_type == 'raw':
                stats['raw_cells'] += 1
        
        return stats
    
    @property
    def metadata(self) -> Dict[str, Any]:
        """Get notebook metadata"""
        return self.nb.metadata
    
    @property
    def cells(self):
        """Get notebook cells"""
        return self.nb.cells
    
    def get_imports(self) -> List[str]:
        """Get imports from the notebook"""
        imports = []
        for cell in self.nb.cells:
            if cell.cell_type == 'code':
                for line in cell.source.split('\n'):
                    if line.startswith('import') or line.startswith('from'):
                        imports.append(line)
        return imports