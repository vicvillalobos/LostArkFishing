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
        self.times_to_repair = int(self.config['FISHING']['times_to_repair'])

        # Input
        self.human_hold_range = (int(self.config['INPUT']['hold_min']), int(self.config['INPUT']['hold_max']))
        self.human_mouse_movement_range = int(self.config['INPUT']['mouse_move_range'])
        self.human_mouse_movement_duration_range = int(self.config['INPUT']['mouse_move_duration_range'])
        self.inventory_key = self.config['INPUT']['inventory_key']
        # UI
        self.ui_mail_icon_position = (int(self.config['UI']['mail_icon_x']), int(self.config['UI']['mail_icon_y']))
        self.ui_first_mail_position = (int(self.config['UI']['first_mail_x']), int(self.config['UI']['first_mail_y']))
        self.ui_mail_accept_position = (int(self.config['UI']['mail_accept_x']), int(self.config['UI']['mail_accept_y']))
        self.ui_mail_remove_position = (int(self.config['UI']['mail_remove_x']), int(self.config['UI']['mail_remove_y']))
        self.ui_inventory_close_button_position = (int(self.config['UI']['inventory_close_button_x']), int(self.config['UI']['inventory_close_button_y']))
        

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

