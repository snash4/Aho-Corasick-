import AhoCorasick
import unittest

class AhoCorasickTest(unittest.TestCase):
  
    
    def setUp(self):
        self.tree = AhoCorasick.AhoCorasickTree()

    def testSimple(self):
        self.tree.add_keyword("foo",1)
        self.tree.add_keyword("bar",2)
        self.tree.set_fail_transitions()
        sr= self.tree.start_match("this is a foo message")
        self.assertEqual((10,12),(sr.start_pos,sr.end_pos))

    def testKeyworkdAsPrefix(self):
        self.tree.add_keyword('foobar',1)
        self.tree.add_keyword('foo',2)
        self.tree.add_keyword('bar',3)
        self.tree.set_fail_transitions()
        sr= self.tree.start_match("xxxfooyyy")
        self.assertEqual((3,5), (sr.start_pos, sr.end_pos))
        sr = self.tree.next_match(sr)
        self.assertEqual(sr, None)
        sr= self.tree.start_match("foo")
        self.assertEqual((0,2),(sr.start_pos, sr.end_pos))
        

    def testFullMatch(self):
        string = "The quick brown fox jumps right over the lazy dog"
        self.tree.add_keyword(string, 1)
        self.tree.set_fail_transitions()
        sr = self.tree.start_match(string)
        self.assertEqual((0,len(string)-1), (sr.start_pos, sr.end_pos))

    def testPaperExample(self):
        self.tree.add_keyword("he",1)
        self.tree.add_keyword("she",2)
        self.tree.add_keyword("his",3)
        self.tree.add_keyword("hers",4)
        self.tree.set_fail_transitions()
        sr=self.tree.start_match("ushers")
        self.assertEqual((1,3), (sr.start_pos, sr.end_pos))

        
       
        
if __name__ == '__main__':
    unittest.main()

        
