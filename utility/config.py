import os.path
import shutil
import json

default_config_file_path = './utility/default-config.json'
actual_config_file_path = './config.json'

class Config:
    @classmethod
    def initialize(cls):
        is_file_exists = cls.__check_config_file_exists(cls)

        if not is_file_exists:
            print('Config file "config.json" does not exist. Creating default...')
            cls.__create_default_config_file(cls)
            is_created = cls.__check_config_file_exists(cls)

            if is_created:
                print('SUCCESS: default config file created')
            else:
                print('ERROR: default config file was not created')
        else:
            print('Using existing config file')

    def set_target_dir(self, source_name: str, source_dir: str, target_dir: str):
        """
        Set a directory for storing backuped files per source name

        Arguments:\n
        source_name -- name of the source\n
        """
        with open(actual_config_file_path) as config_json:
            print(json.load(config_json))

    def __check_config_file_exists(self):
        is_file_exists = os.path.isfile(actual_config_file_path)
        if is_file_exists:
            return True
        else:
            return False

    def __create_default_config_file(self):
        shutil.copyfile(default_config_file_path, actual_config_file_path)

    def __read_config_file(self):
        file = open(actual_config_file_path)
        json_config = json.load(file)
        print(json_config)
