import configparser

class Configuration:
    """
    This class will handle the configuration file and store the configuration data.
    """
    
    def __init__(self, path):
        """
        Constructor
        """
        self.config = configparser.ConfigParser()
        self.config.read(path)

        # Screen
        self.screen_resolution = (int(self.config['SCREEN']['resolution_w']), int(self.config['SCREEN']['resolution_h']))
        self.screen_number = int(self.config['SCREEN']['monitor'])

        # Fishing
        self.fishing_region = (int(self.config['FISHING']['region_w']), int(self.config['FISHING']['region_h']))
        self.fishing_threshold = float(self.config['FISHING']['threshold'])
        self.fishing_key = self.config['FISHING']['activity_key']
        self.fishing_interval = float(self.config['FISHING']['interval'])
        self.fishing_max_time = int(self.config['FISHING']['max_time'])
        self.fishing_template = self.config['FISHING']['template']

        # Input
        self.human_hold_range = (int(self.config['INPUT']['hold_min']), int(self.config['INPUT']['hold_max']))

        

    def get(self, section, key):
        """
        This method will return the value of the key in the section.
        """
        return self.config[section][key]

    def get_sections(self):
        """
        This method will return the list of sections in the configuration file.
        """
        return self.config.sections()

    def get_keys(self, section):
        """
        This method will return the list of keys in the specified section.
        """
        return self.config[section].keys()

