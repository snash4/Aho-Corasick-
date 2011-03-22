import state
import MatchResult
from collections import deque

class AhoCorasickTree:
    """ This is the main Class for Aho Corasick String Matching Algorithm
        This class has the root of the Tree for AC"""
    root = None
    newstate = None
    prepared = None

    def __init__(self):
        self.root = state.State(0, ' ')
        self.newstate = 0
        self.prepared = False

    def add_keyword(self, keywords, sid):
        """Adds the keyword in the tree"""
    
##        for key in keywords.split(' '):
        j = 0
        current = self.root
        key = keywords.upper()
##        start = 0
        while j < len(key):
            char = key[j]
            j = j+ 1
            child = current.get_transition(char)
            if child != None:
                current = child
            else:
                self.newstate = self.newstate +1
                node = state.State(self.newstate, char)
                current.transition_List.append(node)
                current = node
                while j < len(key):
                    self.newstate = self.newstate +1
                    node2 = state.State(self.newstate, key[j])
                    current.transition_List.append(node2)
                    current = node2
                    j = j+1
                break
        tupl = key, sid
        current.string_id = sid
        current.output_set.add(tupl)
        
##-------------------------------------------------------------------
    def set_fail_transitions(self):
        """Sets the fail transitions in tree"""
        queue = deque()
        current = self.root
        child = self.root

        for node in self.root.transition_List:
            queue.append(node)
            node.fail_state = self.root

        while len(queue) != 0:
            r = queue.popleft()
            for node in r.transition_List:
                queue.append(node)
                val = node.value
                current = r.fail_state
                while True:
                    if current.test_transition(val) == False:
                        current = current.fail_state
                    else:
                        break
                child = current.get_transition(val)
                if child == None:
                    node.fail_state = current
                else:
                    node.fail_state = child
            node.add_output(node.fail_state.output_set)
            
        self.prepared = True
 
##-------------------------------------------------------
    def find_all(self, string):
        """ Finds all substrings of input which are keywords in the tree
        and returns list of MatchResult"""
        
        sr = self.start_match(string)
        out_list = []
        while (sr != None):
            out_list.append(sr)
            sr = self.next_match(sr)

        return out_list
          
##---------------------------------------------------------
    def display_tree(self):
        """ It is used to display the tree of keywords.
            Prints ID of State and value of State"""
        queue = deque()
        for node in self.root.transition_List:
            queue.append(node)

        while len(queue) !=0:
            node = queue.popleft()
            for node_in_list in node.transition_List:
                queue.append(node_in_list)
            print node.state_id, node.value
            
##----------------------------------------------------------------      
    def display_output(self):
        """ This function displays the outputs at a state"""
        queue = deque()
        for node in self.root.transition_List:
            queue.append(node)
        print 'State','\t' 'Output Set'
        while len(queue) !=0:
            node = queue.popleft()
            for node_in_list in node.transition_List:
                queue.append(node_in_list)
            
            if len(node.output_set) !=0:
                print node.state_id, '\t', node.output_set
##--------------------------------------------------------------------

    def start_match(self, string):
        """ Function to start the match of a given substring"""
        if self.prepared == False:
            print " Error... Fail Transitions Not Set"
            return None
        return self.next_match(MatchResult.MatchResult(self.root, string, 0, -1))
                
##--------------------------------------------------------------------
    def next_match(self, previous_match):
        """ Starts the match from wher the previous match ended
            Returns the MatchResult Object"""
        
        current = previous_match.last_matched_state
        indx = previous_match.end_pos
        indx = indx + 1
        string = previous_match.string
        
        count = -1
        while indx < len(string):
            while True:
                if current.test_transition(string[indx]) == False:
                    count = previous_match.start_pos
                    current = current.fail_state                    
                else:
                    child = current.get_transition(string[indx])
                    break
                
            if child != None:
                count = count + 1
                current = child
                if len(child.output_set) != 0:
                    maxlen = 0
                    for opt in child.output_set:
                        if len(opt[0]) > maxlen:
                            maxlen = len(opt[0])
                            
                    start = indx-maxlen+1
                    return MatchResult.MatchResult(child, string, start, indx)

            indx = indx + 1
        return None
