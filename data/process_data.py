import pandas as pd
from datetime import timedelta

# Configuration
INPUT_FILE = 'JC-202509-citibike-tripdata-sample10000.csv'
OUTPUT_FILE = 'JC-202509-citibike-tripdata-sample.csv'
MIN_DURATION = timedelta(minutes=1)
MAX_DURATION = timedelta(hours=24)

def process_citibike_data():
    """Process Citi Bike trip data by filtering invalid durations."""
    
    # Read data
    print(f"Reading data from: {INPUT_FILE}")
    try:
        df = pd.read_csv(INPUT_FILE)
    except FileNotFoundError:
        print(f"Error: File '{INPUT_FILE}' not found.")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    print(f"Original data rows: {len(df)}")
    
    # Convert time columns to datetime
    df['started_at'] = pd.to_datetime(df['started_at'])
    df['ended_at'] = pd.to_datetime(df['ended_at'])
    
    # Calculate trip duration
    df['duration'] = df['ended_at'] - df['started_at']
    
    # Count invalid records before filtering
    too_short = (df['duration'] < MIN_DURATION).sum()
    too_long = (df['duration'] > MAX_DURATION).sum()
    
    # Filter data: duration >= 1 minute and <= 24 hours
    df_filtered = df[(df['duration'] >= MIN_DURATION) & (df['duration'] <= MAX_DURATION)].copy()
    
    # Remove temporary duration column
    df_filtered.drop(columns=['duration'], inplace=True)
    
    # Print statistics
    print(f"Filtered data rows: {len(df_filtered)}")
    print(f"Removed rows: {len(df) - len(df_filtered)}")
    print(f"\nStatistics:")
    print(f"- Trips shorter than 1 minute: {too_short}")
    print(f"- Trips longer than 24 hours: {too_long}")
    
    # Save processed data
    try:
        df_filtered.to_csv(OUTPUT_FILE, index=False)
        print(f"\nSuccessfully saved cleaned data to: {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    process_citibike_data()
