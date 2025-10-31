"""
Tests for the stat command
"""
import pytest
import nbformat
from nbutils.core.notebook import Notebook
from nbutils.core.cleaner import NotebookCleaner

@pytest.fixture
def sample_notebook(tmp_path):
    """Create a sample notebook with outputs"""
    nb = nbformat.v4.new_notebook()
    
    # Add a code cell with output
    code_cell = nbformat.v4.new_code_cell(
        source="print('hello')",
        execution_count=1,
        outputs=[
            nbformat.v4.new_output(
                output_type='stream',
                name='stdout',
                text='hello\n'
            )
        ]
    )
    nb.cells.append(code_cell)
    
    # Add a markdown cell
    nb.cells.append(nbformat.v4.new_markdown_cell("# Title"))
    
    # Add metadata
    nb.metadata['custom_field'] = 'should be removed'
    code_cell.metadata['custom_cell_field'] = 'should be removed'
    
    # Save notebook
    nb_path = tmp_path / "test.ipynb"
    with open(nb_path, 'w') as f:
        nbformat.write(nb, f)
    
    return nb_path


def test_stat_notebook(sample_notebook):
    """Test that stat shows notebook statistics"""
    nb = Notebook(sample_notebook)
    stats = nb.get_stats()
    assert stats['total_cells'] == 2
    assert stats['code_cells'] == 1
    assert stats['markdown_cells'] == 1
    assert stats['file_size'] > 0