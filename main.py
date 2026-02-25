from fun_tcx_parser import parse_tcx
from fun_tcx_basic_analytics import basic_analysis

def main():
    # Use your verified absolute path
    path = '/home/belugaboy/Projekte/Data_Science/running_performance_rating/v1/stp_data.tcx'
    
    # Parse
    workout_data = parse_tcx(path)
    
    # Run basic analysis
    stats = basic_analysis(workout_data)
    
    # Enjoy the fruits of your labor
    if isinstance(stats, dict):
        print("-" * 30)
        print("RUNNING PERFORMANCE SUMMARY")
        print("-" * 30)
        print(f"Distance:  {stats['dist']} km")
        print(f"Duration:  {stats['duration_min']} min")
        print(f"Avg HR:    {stats['hr']} bpm")
        print(f"Pace:      {stats['pace']}")
        print(f"Speed:     {stats['speed']} km/h")
        print("-" * 30)
    else:
        # Error message if stats isn't a dictionary
        print(f"Analysis failed: {stats}")

if __name__ == "__main__":
    main()