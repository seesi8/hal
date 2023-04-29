import os

import yaml


class Skill:
    def __init__(self) -> None:
        pass

    def get():
        with open("./settings.yaml", "r") as stream:
            try:
                result = yaml.safe_load(stream)
                return result
            except yaml.YAMLError as exc:
                print(exc)
