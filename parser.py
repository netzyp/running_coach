from strava_api import return_strava_data



def parsed_run_data(data):
    run_stats = []
    for x in data:
        if x['type'] == 'Run':
            run_stats.append({
                'name': x['name'],
                'date': x['start_date_local'],
                'distance': x['distance'],
                'average_heartrate': x.get('average_heartrate'),
                'average_temp': x.get('average_temp'),
                'moving_time': x['moving_time'],
                'average_speed': x['average_speed'],
                'total_elevation': x['total_elevation_gain'],
                'max_heartrate': x.get('max_heartrate'),
                'pace': (x['moving_time']/60) / (x['distance'] / 1000)
                })
    return run_stats



print(parsed_run_data(data=return_strava_data()))