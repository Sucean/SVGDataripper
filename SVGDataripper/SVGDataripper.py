from svgpathtools import svg2paths
import numpy as np
from collections import Counter

class SVGDataripper():

    def __init__(self, svg_file):
    
        self.paths, self.attributes = svg2paths(svg_file)
        self.xlog, self.ylog = False, False

    def extract_data(self, data_color, data_x_range = (0,100), data_y_range  = (0,100)):

        coords = []
        
        for atr, pth in zip(self.attributes, self.paths):
            
            if data_color in atr['style']:
                for i, seg in enumerate(pth):
                    if i == 0:
                        coords.append((seg.start.real, seg.start.imag))  
                    coords.append((seg.end.real, seg.end.imag))
                    
        self.cumulative = np.array(coords)
        self.distribution = np.unique(self.cumulative, axis=0)
        
        return self.map_datarange(self.distribution, data_x_range, data_y_range)
        

    def find_data(self):

        potential_data = []
        
        for atr in self.attributes:
            str_pos = atr.get('style').find('stroke:')
            str_len = len('stroke:')

            potential_data.append(atr.get('style')[str_pos + str_len : str_pos + str_len + 7])

      
        potential_data = np.array(potential_data)
        
        unique_data = np.unique(potential_data)
        counts = Counter(potential_data)
        
        result_dict = {}
        for unique_element in unique_data:
            count_in_original = counts.get(unique_element, 0)
            result_dict[unique_element] = count_in_original

        return result_dict


    def map_coordinates(self, svg_coords, svg_range, data_range, log_scale = False):
        svg_min, svg_max = svg_range
        data_min, data_max = data_range

        if log_scale:
            if data_min <= 0:
                data_min = 1e-10
            log_data_min, log_data_max = np.log10(data_min), np.log10(data_max)
            log_mapped = log_data_min + (svg_coords - svg_min) * (log_data_max - log_data_min) / (svg_max - svg_min)
            return 10 ** log_mapped
        else:
            return data_min + (svg_coords - svg_min) * (data_max - data_min) / (svg_max - svg_min)
            

    def map_datarange(self, data, data_x_range, data_y_range):
        svg_x_range = (data[:, 0].min(), data[:, 0].max())
        svg_y_range = (data[:, 1].max(), data[:, 1].min()) # Reverse y range due to y axis goes from top to bottom in svg
        
        data_x = self.map_coordinates(data[:, 0], svg_x_range, data_x_range, self.xlog)
        data_y = self.map_coordinates(data[:, 1], svg_y_range, data_y_range, self.ylog)

        return data_x, data_y
        