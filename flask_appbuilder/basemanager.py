

class BaseManager(object):
    """
        The parent class for all Managers
    """
    def __init__(self, appbuilder):
        self.appbuilder = appbuilder

    def register_views(self):
        pass

    def pre_process(self):
        pass

    def post_process(self):
        pass
    @staticmethod
    def before_request():
        pass
    @staticmethod
    def after_request(response):
        from flask import g
        import logging
        log = logging.getLogger(__name__)
        for callback in getattr(g, 'after_request_callbacks', ()):
            callback(response)
        return response
    