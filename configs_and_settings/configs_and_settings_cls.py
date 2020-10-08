import os
import json


class Settings:
	def __init__(self, ini_file_path):
		self._config = json.load(open(ini_file_path, "r"))
	
	def __getitem__(self, key):
		return self._config[key]
	
	def display_top_setting_keys(self):
		top_setting_keys = list(self.__dict__['_config'].keys())
		return top_setting_keys


general_settings_obj = Settings(os.path.join(os.path.dirname(os.path.realpath(__file__)), "configs_and_settings.json"))
