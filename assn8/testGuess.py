import unittest

from guess import Guess
from hangman import Hangman
from word import Word

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('apple')
        self.h1 = Hangman()
        self.w1 = Word('words.txt')

    def tearDown(self):
        pass

    #guess
    def testGuess(self):
        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.guess('s'))

    def testFinished(self):
        self.assertFalse(self.g2.finished())
        self.g2.guess('a')
        self.assertFalse(self.g2.finished())
        self.g2.guess('p')
        self.assertFalse(self.g2.finished())
        self.g2.guess('l')
        self.assertTrue(self.g2.finished())

    def testFinished2(self):
        self.assertFalse(self.g2.finished())
        for i in 'apl':
            self.g2.guess(i)
        self.assertTrue(self.g2.finished())

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    #hangman
    def testDecreaseLife(self):
        self.assertEqual(self.h1.remainingLives, 6)
        self.h1.decreaseLife()
        self.assertEqual(self.h1.remainingLives, 5)

    def testCurrentShape(self):
        self.assertEqual(self.h1.currentShape(), self.h1.text[6])

    #word
    def testTest(self):
        self.assertEqual(self.w1.test(), 'default')

    def testRandFromDB(self):
        self.assertTrue(self.w1.randFromDB() in self.w1.words)

if __name__ == '__main__':
    unittest.main()

