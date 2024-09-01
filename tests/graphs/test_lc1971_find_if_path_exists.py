import pytest
from datastructures.graphs.lc1971_find_if_path_exists_in_graph.solution import valid_path


class TestLC1971FindIfPathExistsInAGraph:
    # @pytest.mark.skip
    def test_valid_path_returns_true(self):
        # Arrange
        n = 3
        edges = [[0,1],[1,2],[2,0]]
        source = 0
        destination = 2
        # Act
        result = valid_path(n, edges, source, destination)
        # Assert
        assert result == True


    # @pytest.mark.skip
    def test_empty_graph_returns_false(self):
        # Arrange
        n = 0
        edges = []
        source = None
        destination = None
        # Act
        result = valid_path(n, edges, source, destination)
        # Assert
        assert result == False


    # @pytest.mark.skip
    def test_graph_with_one__returns_true(self):
        # Arrange
        n = 1
        edges = [[0, None]]
        source = 0
        destination = 0
        # Act
        result = valid_path(n, edges, source, destination)
        # Assert
        assert result == True

    # @pytest.mark.skip
    def test_graph_with_self_edge_returns_false(self):
        # Arrange
        n = 3
        edges = [[0, 0]]
        source = 0
        destination = 0
        # Act
        result = valid_path(n, edges, source, destination)
        # Assert
        assert result == False

    # @pytest.mark.skip
    def test_no_valid_path_False(self):
        # Arrange
        n = 6
        edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
        source = 0
        destination = 5
        # Act
        result = valid_path(n, edges, source, destination)
        # Assert
        assert result == False


if __name__ == "__main__":
    pytest.main()