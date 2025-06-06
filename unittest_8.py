import unittest
from lab_8 import read_graph_from_csv, edmonds_karp
import tempfile
import os

class TestMaxFlowFromCSV(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile(mode='w+', delete=False)
        self.test_file.write("A,B\nC,D\nA,C,3\nA,D,2\nC,B,2\nD,B,4\n")
        self.test_file.seek(0)
        self.filename = self.test_file.name

    def tearDown(self):
        self.test_file.close()
        os.unlink(self.filename)

    def test_graph_construction(self):
        graph, source, sink = read_graph_from_csv(self.filename)
        self.assertIn('super_source', graph)
        self.assertIn('super_sink', graph)
        self.assertIn('A', graph['super_source'])
        self.assertIn('B', graph)
        self.assertEqual(graph['A']['C'], 3)
        self.assertEqual(graph['D']['B'], 4)

    def test_max_flow(self):
        graph, source, sink = read_graph_from_csv(self.filename)
        result = edmonds_karp(graph, source, sink)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()
