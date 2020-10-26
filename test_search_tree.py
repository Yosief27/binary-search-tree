import unittest
from  binary_tree  import search_tree_dic.Dictionary


class TestBst(unittest.TestCase):
    def test_insert(self):
        d=Dictionary()
        d.insert(15,'value15')
        d.insert(8,'value8')
        d.insert(6,'value6')
        d.insert(9,'value9')
        d.insert(20,'value20')
        d.insert(18,'value18')
        d.insert(24,'value24')
        self.assertEqual(d.get_value(24),"value24",'get 24 key should return current value')
        self.assertEqual(d.get_value(15),"value15",'get 15 key should return current value')
        self.assertEqual(d.get_value(6), "value6",'get 6 key should return current value')
        
    def test_delete(self):
        d=Dictionary()
        d.insert(15,'value15')
        d.insert(8,'value8')
        d.insert(6,'value6')
        d.insert(9,'value9')
        d.insert(20,'value20')
        d.insert(18,'value18')
        d.insert(24,'value24')
        r1=d.delete(24)
        r2=d.delete(8)
        r3=d.delete(15)
        r4=d.delete(24)
        r5=d.insert(9,'value9')
        
        self.assertTrue(r1,'delete of a leaf node should return True when successful')
        self.assertTrue(r2,'delete a node which have two nodes should return True when successful')
        self.assertTrue(r3,'delete of a root node  should return True when successful')
        self.assertFalse(r4,'delete  should return False when the node does not exist')
        self.assertFalse(r5,'delete  should return False when the node already exist in the tree')
       

if __name__=='__main__':
    unittest.main()    