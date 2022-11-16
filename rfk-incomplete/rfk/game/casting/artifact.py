from game.casting.actor import Actor

class Artifact(Actor):
    """A witty comment or message accompanying the actor including the message of a found kitten. 
    
    The responsibility of Artifact is to set a message to an actor

    Attributes:
        _message(string): A comment that appears on the screen for each actor
    """

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
    def __init__(self):
        super().__init__()
        self._message = " "

    def set_message(self, message):
        """sets the message for the Artifact of the currently constructed Actor.
        
        Args:
            message (string): The message.
        """
        self.message = message

    def get_message(self):
        """Gets the Artifact's message.
        
        Returns:
            string: The message.
        """
        return self.message