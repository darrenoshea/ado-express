import datetime


class ReleaseDetails:
    """
    :param release_project_name:
    :type release_project_name: str
    :param release_definition:
    :type release_definition: str
    :param release_name:
    :type release_name: str
    :param release_env:
    :type release_env: str
    :param is_deployed:
    :type is_deployed: bool
    :param modified_on:
    :type modified_on: datetime
    :param url:
    :type url: str
    :param id:
    :type id: str
    """
    def __init__(self, release_project_name: str, release_definition: str, release_name: str, release_env: str, is_deployed: bool, modified_on: datetime, url: str, id: str):
        self.release_project_name = release_project_name
        self.release_definition = release_definition
        self.release_name = release_name
        self.release_env = release_env
        self.is_deployed = is_deployed
        self.modified_on = modified_on
        self.url = url
        self.release_number = int(release_name.split('-')[1])
        self.id = id