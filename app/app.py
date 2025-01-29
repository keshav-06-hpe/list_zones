from flask import Flask, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/list_zones', methods=['GET'])
def list_zones():
    # Get the list of zones and nodes
    zones = subprocess.check_output(["kubectl", "get", "nodes", "-L", "topology.kubernetes.io/zone", "-o", "json"])
    zones_data = json.loads(zones)

    # Extract zones and nodes
    zone_nodes = {}
    for node in zones_data['items']:
        zone = node['metadata']['labels'].get('topology.kubernetes.io/zone', 'unknown')
        if zone not in zone_nodes:
            zone_nodes[zone] = []
        zone_nodes[zone].append(node['metadata']['name'])

    # Save to JSON files
    with open('/app/zones.json', 'w') as f:
        json.dump(list(zone_nodes.keys()), f)
    with open('/app/nodes_by_zone.json', 'w') as f:
        json.dump(zone_nodes, f)

    return jsonify(zone_nodes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)