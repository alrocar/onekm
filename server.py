from flask import Flask
# from flask import render_template
from flask import request
from flask import send_from_directory

from iso import get_iso_distance, create_map, export_map, delete_map


app = Flask(__name__)


@app.route('/iso')
def export():
    mode = request.args.get('mode', default='walk')
    distance = float(request.args.get('distance', default='1000'))
    lat = float(request.args.get('lat'))
    lon = float(request.args.get('lon'))

    iso, bounds = get_iso_distance(lat, lon, distance=distance, network_type=mode)
    map_id = create_map(iso, lon, lat)
    result = export_map(map_id, bounds)
    delete_map(map_id)

    return send_from_directory('/tmp', result.split('/')[-1], as_attachment=True)

# @app.route('/ui')
# def ui():
#     return render_template('map.html')
