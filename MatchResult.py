class MatchResult:
    """ This class hold the result of the search so far. It stores the
    last state where search finished, starting position of search,
    last position of match"""
    last_matched_state = None
    string = None
    start_pos = None
    end_pos = None

    def __init__(self, state, string, start, end):
        self.last_matched_state = state
        self.start_pos = start
        self.end_pos = end
        self.string = string.upper()

    def get_match_result(self):
        """ Returns the output set of the match"""
        
        if len(self.last_matched_state.output_set) != 0:
               ## print self.last_matched_state.state_id,'\t',
                                ##self.last_matched_state.output_set
            return self.last_matched_state.output_set

    def get_matched_state(self):
        """ Returns the previous matched state"""
        return self.last_matched_state
