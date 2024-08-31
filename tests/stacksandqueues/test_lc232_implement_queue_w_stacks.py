import pytest
from datastructures.stacks_and_queues.lc232_implement_queues_using_stacks.solution import MyQueue


class TestLC232ImplementQueueUsingStacks:
    # @pytest.mark.skip
    def test_valid_push(self):
        # Arrange
        result = MyQueue()

        # Act
        result.push(2)
        result.push(3)
        result.push(4)
        result.push(5)

        # Assert
        assert result.print_queue() == [2,3,4,5]
        assert result.get_length() == 4


    # @pytest.mark.skip
    def test_valid_pop(self):
        # Arrange
        result = MyQueue()

        # Act
        result.push(2)
        result.push(3)
        result.push(4)
        result.push(5)

        # Assert
        assert result.pop() == 2


    # @pytest.mark.skip
    def test_valid_peek(self):
        # Arrange
        result = MyQueue()

        # Act
        result.push(2)
        result.push(3)
        result.push(4)
        result.push(5)
        result.pop()

        # Assert
        assert result.peek() == 3


    # @pytest.mark.skip
    def test_not_empty_queue_returns_false(self):
        # Arrange
        result = MyQueue()

        # Act
        result.push(2)
        result.push(3)
        result.push(4)
        result.push(5)

        # Assert
        assert result.empty() == False

    # @pytest.mark.skip
    def test_valid_empty_queue_returns_true(self):
        # Arrange
        result = MyQueue()

        # Act
        result.push(2)
        result.push(3)
        result.push(4)
        result.push(5)
        result.pop()
        result.pop()
        result.pop()
        result.pop()


        # Assert
        assert result.empty() == True

        

if __name__ == "__main__":
    pytest.main()