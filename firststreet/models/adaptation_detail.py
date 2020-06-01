from firststreet.models.geometry import Geometry


class AdaptationDetail:

    def __init__(self, response):

        self.adaptationId = response.get('adaptationId')
        self.name = response.get('name')
        self.type = response.get('type')
        self.scenario = response.get('scenario')
        self.conveyance = response.get('conveyance')
        self.returnPeriod = response.get('returnPeriod')
        self.serving = response.get('serving')
        self.geometry = Geometry(response.get('geometry'))
