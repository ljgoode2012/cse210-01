from game.scripting.action import Action


class LoadAssetsAction(Action):

    def __init__(self, audio_service, video_service):
        self._audio_service = audio_service
        self._video_service = video_service

    def execute(self, cast, script, callback):
        self._audio_service.load_sounds("c:\\Users\\Brandon\\Desktop\\Pathway\\cse210-01\\batter-incomplete\\batter\\assets\\sounds")
        self._video_service.load_fonts("c:\\Users\\Brandon\\Desktop\\Pathway\\cse210-01\\batter-incomplete\\batter\\assets\\fonts")
        self._video_service.load_images("c:\\Users\\Brandon\\Desktop\\Pathway\\cse210-01\\batter-incomplete\\batter\\assets\\images")
        