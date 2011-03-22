class State:
    """ State Class is used to store the state at each node of the tree
        Each state has state id (sid), value, and list of nodes (transition_List)
        of which we have a transition from the state,
        outputs at this state (output_set)
        and lastly fail_state for fail tranaitions"""
        
    state_id = None        ## store the id of state
    value = None      ## stores values of state
    transition_List = None    ## used to store the list of
                                ## next states for transition
    output_set = None    ## it is set datastructure for storing
                        ## the outputs (keywords + string id) at that state
    fail_state = None
    
    def __init__(self, sid, val):
        self.state_id = sid
        self.value = val
        self.transition_List = []
        self.fail_state = 0
        self.string_id=0
        self.output_set = set()

    def get_transition(self, val):
        """ this function gets the next state on input val"""
        for node in self.transition_List:
            if node.value == val:
                return node
        return None
    

    def test_transition(self, val):
        """ This checks whether there is transition or not on input val
         for current state, the transition is always true on any input"""

        if self.state_id == 0:     
           return True
        else:
            for node in self.transition_List:
                if node.value == val:
                    return True
            return False

        
    def add_output(self, key):
        """This adds the key to the output in the state"""
        self.output_set = self.output_set ^ key
        
