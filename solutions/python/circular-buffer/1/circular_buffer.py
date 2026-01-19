class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_pointer = 0
        self.write_pointer = 0
        self.count = 0

    def read(self):
        if self.count == 0:
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.read_pointer]
        self.buffer[self.read_pointer]  = None
        self.read_pointer = (self.read_pointer+1) % self.capacity
        self.count -= 1
        return value
    def write(self, data):
        if self.count == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_pointer] = data
        self.write_pointer = (self.write_pointer + 1) % self.capacity
        self.count += 1

    def overwrite(self, data):
        if self.count == self.capacity:
            self.read_pointer = (self.read_pointer + 1) % self.capacity
        else:
            self.count += 1
        self.buffer[self.write_pointer] = data
        self.write_pointer = (self.write_pointer + 1) % self.capacity
        

    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_pointer = 0
        self.write_pointer = 0
        self.count = 0