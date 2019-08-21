AhoCorasick - String Searching Algorithm.

SHEIKH NASRULLAH

INTRODUCTION:
  Aho - Corasick string matching algorithm is a string searching algorithm. It performs fast mulitple keyword
  search across the text. It constructs a finite state maching that resembles a trie with additional links 
  between the various internal nodes. These additional links allow fast transitions between failed pattern matches.

  It's described in the classic paper 'Efficient string matching: an aid to bibliographic search':

    http://portal.acm.org/citation.cfm?id=360855&dl=ACM&coll=GUIDE

  
USAGE::
  import ahocorasick
  tree.add_keyword("he", 1)        // Adds keywords with their ID's into the tree  
  tree.add_keyword("she",2)
  tree.add_keyword("his", 3)

  tree.set_fail_transitions()       // sets the fail transition of the tree

  search_result = tree.start_match(string)  // Starts the search of string in tree. Returns the first MatchResult.
  next_result = tree.next_match(sr)         // Starting from the previous match, it Searches for the next match


  RELEASES ::
    The package contains three classes::

    1. AhoCorasick::
         It has the following methods
	
	add_keyword (string, ID)
	   Add's new keyword in the tree
	 
	set_fail_transitions()
	   This is the failure function. It must be called before any searching in the tree

	find_all(string)
	  It returns list of all matches 

	start_match(string)
	  It return the first occurance of the match otherwise None. It must be called before calling next_match.

	next_match(MatchResult)
	  Starting from the previous match, it returns the next match

	display_tree()
	  It displays the state id's and state values of all states in tree.

	display_output()
	  it displays the outputs at a node in a tree
	
     2. State

	 get_transition(val)
	   It returns the transition state for the value val and current state.

	 test_transition(val)
	   Returns true if there is transition from current state, otherwise false

	 add_output()
	   it adds the output to output_set

     3. MatchResult:
           get_match_result()
	      it returns the matched output string.

	    get_matched_state()
	       it returns the State of the match

	  

