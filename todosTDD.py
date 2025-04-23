import unittest

from TDD.testeAluno import AlunoTestStringMethods
from TDD.testeProfessor import ProfessorTestStringMethods
from TDD.testeTurma import TurmaTestStringMethods
# from TDD.testeIntegracao import IntegracaoTestStringMethods

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(AlunoTestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ProfessorTestStringMethods))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TurmaTestStringMethods))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(IntegracaoTestStringMethods))
    return suite


if __name__ == '__main__':
    # runTests()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())