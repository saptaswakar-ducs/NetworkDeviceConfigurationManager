from pathlib import Path

from yangson.datamodel import DataModel
from yangson.exceptions import YangsonException


class ConfigValidator:

    def __init__(self):
        base_path = Path(__file__).parent.parent

        yang_library = base_path / "yang" / "yang-library.json"
        yang_path = base_path / "yang"

        self.data_model = DataModel.from_file(
            str(yang_library),
            [str(yang_path)]
        )

    def validate(self, configuration):

        try:
            root = self.data_model.from_raw(
                configuration
            )

            root.validate()

            return True, "Configuration is valid."

        except YangsonException as error:

            return False, f"Configuration is invalid: {error}"