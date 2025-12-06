import io

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Create the actual file
        # TODO: Create 4 counters here (all start at 0):
        # - self._??? for total bytes read
        self._bytes_read = 0
        # - self._??? for number of read operations
        self._read_ops =0
        # - self._??? for total bytes written 
        self._bytes_written = 0
        # - self._??? for number of write operations
        self._write_ops = 0
        

    def __enter__(self):
        # Just return self (for 'with' statement)
        # Hint: return self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Call parent's __exit__ to close the file properly
        # Hint: return super().__exit__(exc_type, exc_val, exc_tb)
        return super().__exit__(exc_type,exc_val,exc_tb)

    def __iter__(self):
        # Return self to make iteration work
        # Hint: return self
        return self

    def __next__(self):
        # Pattern:
        # 1. line = super().__next__()  # Get the next line
        line = super().readline()
        if not line:
            raise StopIteration
        # 2. self._??? += len(line)    # Track bytes
        self._bytes_read += len(line)
        # 3. self._??? += 1              # Track operation
        self._read_ops += 1
        # 4. return line
        return line
        

    def read(self, size=-1):
        # Pattern (JUST LIKE THE EXAMPLE ABOVE!):
        # 1. data = super().read(size)  # Do actual reading
        data = super().read(size)
        # 2. self._??? += len(data)      # Track bytes
        self._bytes_read += len(data)
        # 3. self._??? += 1              # Track operation
        self._read_ops += 1
        # 4. return data
        return data

    @property
    def read_bytes(self):
        # Just return the counter!
        # Hint: return self._read_bytes_counter (or whatever you named it)
        return self._bytes_read

    @property
    def read_ops(self):
        # Just return the counter!
        return self._read_ops

    def write(self, b):
        # Pattern:
        # 1. count = super().write(b)   # Do actual writing, get bytes written
        count = super().write(b)
        # 2. self._??? += count          # Track bytes (write returns an int!)
        self._bytes_written += count
        # 3. self._??? += 1              # Track operation
        self._write_ops += 1
        # 4. return count               # Return what write() returned
        return count

    @property
    def write_bytes(self):
        return self._bytes_written

    @property
    def write_ops(self):
        return self._write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket  # Store the wrapped socket!
        # TODO: Create 4 counters (just like MeteredFile)
        # - self._??? for bytes received
        self._bytes_received = 0#which is better,self._bytes_received or self._bytes_received_counter(same question for 4 )
        # - self._??? for recv operations
        self._recv_ops = 0
        # - self._??? for bytes sent
        self._bytes_sent = 0
        # - self._??? for send operations
        self._send_ops = 0
        

    def __enter__(self):
        # Return self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Call self._socket.__exit__() to close socket
        # Hint: return self._socket.__exit__(exc_type, exc_val, exc_tb)
        return self._socket.__exit__(exc_type,exc_val,exc_tb)

    def recv(self, bufsize, flags=0):
        # Pattern (DELEGATION - different from inheritance!):
        # 1. data = self._socket.recv(bufsize, flags)  # Call the wrapped socket
        data = self._socket.recv(bufsize,flags)
        # 2. self._??? += len(data)  # Track bytes
        self._bytes_received +=len(data)
        # 3. self._??? += 1          # Track operation
        self._recv_ops += 1
        # 4. return data
        return data

    @property
    def recv_bytes(self):
        return self._bytes_received

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        # Pattern:
        # 1. count = self._socket.send(data, flags)  # Call wrapped socket
        count =self._socket.send(data,flags)
        # 2. self._??? += count  # Track bytes (send returns int!)
        self._bytes_sent += count
        # 3. self._??? += 1      # Track operation
        self._send_ops += 1
        # 4. return count
        return count
        

    @property
    def send_bytes(self):
        return  self._bytes_sent

    @property
    def send_ops(self):
        return  self._send_ops


# ============= KEY DIFFERENCES =============
# MeteredFile (INHERITANCE):
#   - Use: super().read()  
#   - Because: MeteredFile IS a BufferedRandom
#
# MeteredSocket (DELEGATION):  
#   - Use: self._socket.recv()
#   - Because: MeteredSocket HAS a socket
# ===========================================