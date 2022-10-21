class FirstResourse(Resource):
    """
    Ресурс для чего-то
    """

    def get(self):
        """Какой-то комментарий"""
        ...

    ...


api.add_resource(FirstResourse, '/get_something')
