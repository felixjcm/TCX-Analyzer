import xml.etree.ElementTree as ET

def parse_tcx(file_path):
    # Load and parse the file
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    # Define namespace as dictionary
    ns = {'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2'}
    
    data_points = []
    
    # Iterate through trackpoints and extract data
    for trackpoint in root.findall('.//ns:Trackpoint', ns):
        point_data = {}
        
        # Timestamp
        time_tag = trackpoint.find('ns:Time', ns)
        point_data['time'] = time_tag.text if time_tag is not None else None
        
        # Position
        pos = trackpoint.find('ns:Position', ns)
        if pos is not None:
            point_data['lat'] = float(pos.find('ns:LatitudeDegrees', ns).text)
            point_data['lon'] = float(pos.find('ns:LongitudeDegrees', ns).text)
        else:
            point_data['lat'] = point_data['lon'] = None
            
        # Altitude
        alt = trackpoint.find('ns:AltitudeMeters', ns)
        point_data['altitude'] = float(alt.text) if alt is not None else None
        
        data_points.append(point_data)
        
    return data_points