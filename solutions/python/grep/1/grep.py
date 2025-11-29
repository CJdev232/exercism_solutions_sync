class Grep:
    def __init__(self, pattern, flags, files):
        """Initialize the grep object"""
        self.pattern = pattern
        self.flags = flags
        self.files = files
        
        # Parse flags into boolean attributes for easy checking
        self.flag_n = '-n' in flags  # line numbers
        self.flag_l = '-l' in flags  # filenames only
        self.flag_i = '-i' in flags  # case insensitive
        self.flag_v = '-v' in flags  # invert match
        self.flag_x = '-x' in flags  # exact match
    
    def _should_match_line(self, line):
        """Determine if a line matches based on pattern and flags"""
        # Prepare comparison based on case sensitivity
        if self.flag_i:
            compare_pattern = self.pattern.lower()
            compare_line = line.lower()
        else:
            compare_pattern = self.pattern
            compare_line = line
        
        # Perform match based on exact or substring
        if self.flag_x:
            matches = compare_pattern == compare_line
        else:
            matches = compare_pattern in compare_line
        
        # Invert result if needed
        if self.flag_v:
            matches = not matches
        
        return matches
    
    def _process_file(self, filename):
        """Process a single file and return matching lines"""
        results = []
        
        with open(filename, 'r') as f:
            lines = f.read().splitlines()
        
        multiple_files = len(self.files) > 1
        
        for line_num, line in enumerate(lines, start=1):
            if self._should_match_line(line):
                formatted = self._format_line(filename, line_num, line, multiple_files)
                results.append(formatted)
        
        return results
    
    def _format_line(self, filename, line_number, line_content, multiple_files):
        """Format a matching line based on flags"""
        parts = []
        
        if multiple_files:
            parts.append(filename)
        
        if self.flag_n:
            parts.append(str(line_number))
        
        parts.append(line_content)
        
        return ':'.join(parts)
    
    def search(self):
        """Main search method - processes all files and returns results"""
        all_results = []
        
        for filename in self.files:
            file_results = self._process_file(filename)
            
            if self.flag_l and file_results:
                all_results.append(filename)
            else:
                all_results.extend(file_results)
        
        return all_results


def grep(pattern, flags, files):
    """Main grep function - creates Grep object and runs search"""
    grepper = Grep(pattern, flags, files)
    results = grepper.search()
    return '\n'.join(results) + '\n' if results else ''