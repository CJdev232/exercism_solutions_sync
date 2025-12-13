class StackUnderflowError(Exception):
    pass


class Evaluate:
    def __init__(self, input_data):
        self.input_data = input_data
        self.stack = []
        self.ops_dict = {}
    
    def _tokenizer(self, input_data=None):
        if input_data is None:
            input_data = self.input_data 
        
        if not input_data:
            raise ValueError("Input empty")
        
        tokens = []
        
        # Input is a list of strings
        if isinstance(input_data, list):
            for item in input_data:
                # Each item is a string, split it
                tokens.extend(item.split())  # ← extend() adds all tokens
        else:
            # If it's just a string, split it
            tokens = input_data.split()
        
        return tokens
    
    def _calculate(self, num1, num2, op_type):
        if op_type == '+':
            result = num1 + num2
        elif op_type == '-':
            result = num1 - num2
        elif op_type == '*':
            result = num1 * num2
        elif op_type == '/':
            if num2 == 0:
                raise ZeroDivisionError("divide by zero")
            result = num1 // num2  # ✓ Integer division
        else:
            raise ValueError(f"undefined operation: {op_type}")
        return result
    
    def _execute_custom_word(self, word_name):
        """Execute a custom word by re-running its definition tokens"""
        if word_name not in self.ops_dict:
            raise ValueError(f"undefined custom operation: {word_name}")
        
        definition = self.ops_dict[word_name]
        # We'll implement this after testing basic operations
        
        for token in definition:
            self._execute_token(token)
        
    def _execute_token(self, token):
        """Execute a single token. Shared by run() and custom words."""
        token = token.upper()
        
        # Handle numbers (ALWAYS, cannot be overridden)
        if token.lstrip('-').isdigit():
            self.stack.append(int(token))
        
        # Handle custom words (check BEFORE built-ins)
        elif token in self.ops_dict:
            self._execute_custom_word(token)
        
        # Handle arithmetic operations
        elif token in ['+', '-', '*', '/']:
            if len(self.stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            popped_1 = self.stack.pop()
            popped_2 = self.stack.pop()
            result = self._calculate(num1=popped_2, num2=popped_1, op_type=token)
            self.stack.append(result)
        
        # Handle DUP
        elif token == 'DUP':
            if len(self.stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack.append(self.stack[-1])
        
        # Handle DROP
        elif token == 'DROP':
            if len(self.stack) < 1:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack.pop()
        
        # Handle SWAP
        elif token == 'SWAP':
            if len(self.stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]
        
        # Handle OVER
        elif token == 'OVER':
            if len(self.stack) < 2:
                raise StackUnderflowError("Insufficient number of items in stack")
            self.stack.append(self.stack[-2])
        
        else:
            #raise ValueError(f"undefined operation: {token}")
            raise ValueError(f"undefined operation")#just because test is hardcoded,after this 50 pass / 4 fail
    def _store_definition(self, tokens):
        """Store a definition, expanding custom words at definition time."""
        expanded = []
        for token in tokens:
            if token in self.ops_dict:
                # Recursively expand custom words
                expanded.extend(self._store_definition(self.ops_dict[token]))
            else:
                expanded.append(token)
        return expanded
  
    def run(self):
        input_list = self._tokenizer()
        if not input_list:
            raise ValueError("Input empty")
        
        index = 0
        while index < len(input_list):
            token = input_list[index].upper()
            
            # Handle word definitions
            if token == ':':
                word_name = input_list[index + 1].upper()
                if word_name.lstrip('-').isdigit():
                    raise ValueError("illegal operation")#add validation for custom word name cannot be a number,currently 52 pass / 2 fail
                definition = []
                index += 2
                
                # Collect tokens until ';'
                while index < len(input_list) and input_list[index] != ';':
                    definition.append(input_list[index].upper())
                    index += 1
                
                if index >= len(input_list):
                    raise ValueError("Unterminated word definition (missing ';')")
                # ✓ If redefining, save old definition temporarily
                old_definition = self.ops_dict.get(word_name)
                if old_definition:
                    # Temporarily store with a shadow name
                    shadow_name = f"__OLD_{word_name}__"
                    self.ops_dict[shadow_name] = old_definition
                
                # Replace references to word_name in definition with shadow_name
                for i, tok in enumerate(definition):
                    if tok == word_name and old_definition:
                        definition[i] = shadow_name    #great,add this,only one test fail
                expanded_definition = self._store_definition(definition)#changing position still not work
                self.ops_dict[word_name] = expanded_definition#great,just change the definition to expanded_definition and all tests pass
                #expanded_definition = self._store_definition(definition)#added this but still not work,considering changing it before adding it to dict
                index += 1  # Skip the ';'
            else:
                self._execute_token(token)
                index +=1
            
        return self.stack 
        


def evaluate(input_data):
   
    evaluator = Evaluate(input_data)
    return evaluator.run()