from datetime import datetime

def basic_analysis(data):
    if not data:
        return "No data found."

    # Distance
    total_m = data[-1].get('distance') or 0
    total_km = total_m / 1000

    # Time (using fromisoformat)
    try:
        start_str = data[0]['time'].replace('Z', '+00:00')
        end_str = data[-1]['time'].replace('Z', '+00:00')
        
        start = datetime.fromisoformat(start_str)
        end = datetime.fromisoformat(end_str)
        duration_sec = (end - start).total_seconds()
    except Exception as e:
        return f"Time parsing error: {e}"

    # Metrics
    hr_list = [d['heart_rate'] for d in data if d.get('heart_rate')]
    avg_hr = sum(hr_list) / len(hr_list) if hr_list else 0
    avg_kmh = (total_km / (duration_sec / 3600)) if duration_sec > 0 else 0

    # Calculate Pace
    if total_km > 0:
        total_min = duration_sec / 60
        pace_dec = total_min / total_km
        p_min = int(pace_dec)
        p_sec = int((pace_dec - p_min) * 60)
        pace_str = f"{p_min}:{p_sec:02d} min/km"
    else:
        pace_str = "0:00"

    return {
        "dist": round(total_km, 2),
        "hr": int(avg_hr),
        "speed": round(avg_kmh, 2),
        "duration_min": round(duration_sec / 60, 2),
        "pace": pace_str
    }