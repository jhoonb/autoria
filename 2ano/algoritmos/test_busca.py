import unittest
from busca import busca_sequencial, busca_binaria

class TestBusca(unittest.TestCase):

    def test_busca_sequencial(self):
        vetor1 = [10, 11, 12, 13, 14, 15]
        vetor2 = list(range(10_001, 100_000))
        self.assertEqual(busca_sequencial(vetor1, 10), 0, "Deveria ser 0")
        self.assertEqual(busca_sequencial(vetor1, 11), 1, "Deveria ser 1")
        self.assertEqual(busca_sequencial(vetor1, 12), 2, "Deveria ser 2")
        self.assertEqual(busca_sequencial(vetor1, 13), 3, "Deveria ser 3")
        self.assertEqual(busca_sequencial(vetor1, 14), 4, "Deveria ser 4")
        self.assertEqual(busca_sequencial(vetor1, 15), 5, "Deveria ser 5")
        self.assertEqual(busca_sequencial(vetor1, 16), -1, "Deveria ser -1")
        self.assertEqual(busca_sequencial(vetor1, 123456), -1, "Deveria ser -1")

        self.assertEqual(busca_sequencial(vetor2, 10_002), 1, "Deveria ser 1")
        self.assertEqual(busca_sequencial(vetor2, 11_002), 1001, "Deveria ser 1001")
        self.assertEqual(busca_sequencial(vetor2, 10_000), -1, "Deveria ser -1")

    def test_busca_binaria(self):
        vetor1 = [10, 11, 12, 13, 14, 15]
        vetor2 = list(range(10_001, 100_000))
        self.assertEqual(busca_binaria(vetor1, 10), 0, "Deveria ser 0")
        self.assertEqual(busca_binaria(vetor1, 11), 1, "Deveria ser 1")
        self.assertEqual(busca_binaria(vetor1, 12), 2, "Deveria ser 2")
        self.assertEqual(busca_binaria(vetor1, 13), 3, "Deveria ser 3")
        self.assertEqual(busca_binaria(vetor1, 14), 4, "Deveria ser 4")
        self.assertEqual(busca_binaria(vetor1, 15), 5, "Deveria ser 5")
        self.assertEqual(busca_binaria(vetor1, 16), -1, "Deveria ser -1")
        self.assertEqual(busca_binaria(vetor1, 123456), -1, "Deveria ser -1")

        self.assertEqual(busca_binaria(vetor2, 10_002), 1, "Deveria ser 1")
        self.assertEqual(busca_binaria(vetor2, 11_002), 1001, "Deveria ser 1001")
        self.assertEqual(busca_binaria(vetor2, 10_000), -1, "Deveria ser -1")        

if __name__ == '__main__':
    unittest.main()