# Jerrichas by Jerricha@chat.cohtitan.com, Summer 2015!
# GPLv3


class TailorCostume(object):
    """
    Represents a .costume file saved from in-game tailor
    """
    def __init__(self, path):
        """
        :param path: /.costume file path
        :type path: str
        """
        self.path = path

    def clamp_scales(value):
        """
        :param value: value to be clamped
        :return: clamps value between -1.0 and 1.0
        """
        return max(min(value, 1.0), -1.0)

    def is_clamped(value):
        """
        :param value: value to be checked for clampedness
        :return: true if value between -1.0 and 1.0
        """
        return -1 < value < 1

    def signum(value):
        """
        :param value: value to be evaluated for sign
        :return: signum; 1 if value positive, -1 if value negative, 0 if value is 0
        """
        return value and (1, -1)[value < 0]

    def encode_colour(list):
        """
        :param list: list of three decimal integers clamped between 0~255
        :return: a colour string in format "rrggbbaa", where aa is 'ff' and all alphabetical numbers are lower case
        """
        assert(list.__len__() == 3)
        for colour in list:
            assert(0 <= colour <= 255)
        return format(colour[0], 'x') + format(colour[1], 'x') + format(colour[2], 'x') + 'ff'

    def parse(self):
        """
        :returns: a list of maps of .costume elements
        """
        file = open(self.path, mode = 'r')
        costume_map = {}
        level = 0
        part_index = 0

        for raw_line in file.readlines():
            line = raw_line.strip()
            segments = [segment.strip() for segment in line.split(',')]
            segments[0] = segments[0].lower()
            key_name = segments[0]
            if line == '' or line == '\n' or line.startswith("CostumePart"):
                pass
            if level == 0:
                if line == '{':
                    level = 1
            elif level == 1:
                if line == '{':
                    level = 2
                elif line == '}':
                    level = 0
                else:
                    if key_name == 'costumefileprefix' or key_name == 'numparts': # unused values
                        pass
                    elif key_name == 'scale':
                        key_name = 'bodyscale'

                    # convert arrays of decimals into single integer per ParagonChat db schema
                    if key_name.endswith('scales'):
                        scales = [float(each) for each in segments[1:]]
                        assert(scales.__len__() == 3)
                        scales_as_int = 0;
                        scales_as_int += int(abs(scales[0] * 100)) | 0x80\
                                  if self.signum(scales[0]) == -1\
                                  else int(abs(scales[0] * 100)) | 0
                        scales_as_int += (int(abs(scales[1] * 100)) | 0x80) << 8\
                                  if self.signum(scales[1]) == -1\
                                  else (int(abs(scales[1] * 100)) | 0) << 8
                        scales_as_int += (int(abs(scales[2] * 100)) | 0x80) << 16\
                                  if self.signum(scales[2]) == -1\
                                  else (int(abs(scales[2] * 100)) | 0) << 16
                        costume_map[key_name] = scales_as_int
                    # convert skincolor RGB values into single integer per ParagonChat db schema
                    elif key_name == 'skincolor':
                        colour_vals = [int(each) for each in segments[1:]]
                        costume_map[key_name] = self.encode_colour(colour_vals)
                    else:
                        costume_map[key_name] = segments[1:]
            elif level == 2:
                if line == '}':
                    level = 1
                    part_index += 1
                else:
                    if part_index not in costume_map:
                        costume_map[part_index] = {'part': part_index}
                    if key_name == 'geometry':
                        key_name = 'geom'
                    elif key_name == 'texture1':
                        key_name = 'tex1'
                    elif key_name == 'texture2':
                        key_name = 'tex2'
                    elif key_name == 'regionname':
                        key_name = 'region'
                    elif key_name == 'bodysetname':
                        key_name = 'bodyset'

                    if key_name.startswith('color'):
                        colour_vals = [int(each) for each in segments[1:]]
                        costume_map[key_name] = self.encode_colour(colour_vals)
                    else:
                        costume_map[part_index][key_name] = segments[1:]
        
        return costume_map


    def get_costumeparts(self):
        """
        :returns: a mapping of /.costume elements to ParagonChatDB 'costumepart' columns
        """
        return None

    def get_proportions(self):
        """
        :returns: a mapping of /.costume records to ParagonChatDB 'costume' columns.
        """
        return None