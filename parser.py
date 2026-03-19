import xml.etree.ElementTree as ET

def parse_nmap_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()

    results = []

    for host in root.findall('host'):
        for port in host.findall('.//port'):
            port_id = port.get('portid')

            state_elem = port.find('state')
            service_elem = port.find('service')

            state = state_elem.get('state') if state_elem is not None else "unknown"
            service = service_elem.get('name') if service_elem is not None else "unknown"

            results.append({
                "port": port_id,
                "state": state,
                "service": service
            })

    return results

def classify_risk(port, state):
      if state != "open":
        return "Low"
      elif str(port) in ["23", "445", "3389", "139"]:
        return "High"
      else:
        return "Medium"
