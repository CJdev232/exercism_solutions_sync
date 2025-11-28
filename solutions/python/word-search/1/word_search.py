class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle 

    def search(self, word):
       for row in range(len(self.puzzle)):
           for col in range(len(self.puzzle[0])):
               if self.puzzle[row][col] == word[0]:
                   if len(word) == 1:
                       return (Point(col,row),Point(col,row))
                   dir_available = self._what_direction_available(grid=self.puzzle,pos=(row,col))
                   for dir in dir_available:
                       offset_row,offset_col = dir
                       next_row = row + offset_row
                       next_col = col + offset_col
                       result = self._search_helper(grid=self.puzzle,cur_pos=(next_row,next_col),cur_dir=dir,target_next=word[1:])
    #todo:write proper returning code,but currently struggling.
                       if result is not None:
                           terminus_row,terminus_col = result
                           return (Point(col,row),Point(terminus_col,terminus_row))
                       
                   

    def _what_direction_available(self,*,grid,pos):
        available = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
        #done:check edge cases and reduce not available positions,return a list of tuples of available direction
        return available#just return all directions as a placeholder
    def _search_helper(self,*,grid,cur_pos,cur_dir,target_next):
        cur_pos_horizontal,cur_pos_vertical = cur_pos
        if (cur_pos_horizontal < 0 or cur_pos_horizontal > len(grid) - 1) or (cur_pos_vertical < 0 or cur_pos_vertical > len(grid[0]) - 1):
            return None
        if grid[cur_pos_horizontal][cur_pos_vertical] == target_next[0]:
                offset_horizontal,offset_vertical = cur_dir
                new_pos = (cur_pos_horizontal+offset_horizontal,cur_pos_vertical+offset_vertical)
                if len(target_next)>1:
                    return self._search_helper(grid=self.puzzle,cur_pos=new_pos,cur_dir=cur_dir,target_next=target_next[1:])
        #done:implement a logic to immediately return proper value(but i do not know yet) and leap out the recursion when the letters not match.
                
        #done:given already limited recursion by the target_next length,consider to implement a check of last letter,if it matches,then return last coordinate,else return a proper value to show the process failed to find word in the current mission,question:what this value is,would it be redirection to the previous logic when letters not match?
                else:
                    return cur_pos
                    
        else:
            return None
#fun comment: why the two todos seems order reversed with the code the implementing them,feels a bit unexpected            
        
        
                       
                        
