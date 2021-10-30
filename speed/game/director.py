from time import sleep
from game import constants
from game.buffer import Buffer
from game.score import Score
from game.words import Words
import random

class Director:
    '''A code template for a person who directs the game. The responsibility of
    this class of objects is to control the sequence of play.
    Stereotype:
        Controller
    Attributes:
        _buffer (Buffer): an instance of Buffer.
        _input_service (InputService): The input mechanism.
        _keep_playing (boolean): Whether or not the game can continue.
        _output_service (OutputService): The output mechanism.
        _score (Score): an instance of Score.
        _Word (Words): an instance of Words.
    '''

    
    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        
        self._words = Words()
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        

    
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)
        

    
    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the key and pasing it to the buffer.
        Args:
            self (Director): An instance of Director.
        """
        
        key = self._input_service.get_letter()
        self._buffer.add_letter(key)

        for i in range(0, len(self._words.get_all())):
            self._words.move_word(i, 1, 1)

    
    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking if enter was pressed.
        Args:
            self (Director): An instance of Director.
        """

        self._handle_enter()
        

    
    def _do_outputs(self):
        """Outputs the important game information during game play. This means it shows and clears 
        the screen, draws the score, words and buffer. Also clears the buffer.
        
        Args:
            self (Director): An instance of Director
        """
        
        self._output_service.clear_screen()
        self._output_service.draw_actor(self._buffer)
        self._output_service.draw_actors(self._words.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.flush_buffer()


   
    def _handle_enter(self):
        """What gets handled when the enter is pressed, the word gets the star removed and 
        the points get added then it resets.
        
        Args: 
            self (director): An instance of actor.
         """
        word = self._buffer.get_word()
        
        if '*' in word:
            new_word = word[:-1]
            points = self._words.word_check(new_word)
            self._score.add_points(points)
            self._buffer.reset()
            self._words._reset()