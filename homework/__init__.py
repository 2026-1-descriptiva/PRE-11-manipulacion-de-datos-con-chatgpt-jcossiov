import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Read input files
    drivers = pd.read_csv('files/input/drivers.csv')
    timesheet = pd.read_csv('files/input/timesheet.csv')
    
    # Group timesheet by driverId and sum hours and miles
    summary = timesheet.groupby('driverId').agg({'hours-logged': 'sum', 'miles-logged': 'sum'}).reset_index()
    
    # Merge with drivers to get names
    summary = summary.merge(drivers[['driverId', 'name']], on='driverId')
    
    # Save summary.csv
    summary.to_csv('files/output/summary.csv', index=False)
    
    # Get top 10 by miles
    top10 = summary.sort_values('miles-logged', ascending=False).head(10)
    
    # Save top10drivers.csv
    top10.to_csv('files/output/top10drivers.csv', index=False)
    
    # Create plots directory if not exists
    os.makedirs('files/plots', exist_ok=True)
    
    # Plot top 10 drivers
    plt.figure(figsize=(10, 6))
    plt.bar(top10['name'], top10['miles-logged'])
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Driver Name')
    plt.ylabel('Miles Logged')
    plt.title('Top 10 Drivers by Miles Logged')
    plt.tight_layout()
    plt.savefig('files/plots/top10_drivers.png')
    plt.close()

if __name__ == '__main__':
    main()