from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here!
class MoveActorsAction(Action):

# Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
# 1) get all the actors from the cast
        self._cast = cast.get_all_actors()
# 2) loop through the actors
        for actor in self._cast:
            actor.move_next()
# 3) call the move_next() method on each actor