import datetime
import os

def write_log(message):
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create log entry
    log_entry = f"[{timestamp}] {message}\n"
    
    # Write to log file
    log_file = 'logs/app.log'
    try:
        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(log_entry)
        print(f"Log written successfully: {log_entry.strip()}")
    except Exception as e:
        print(f"Error writing to log file: {str(e)}")

if __name__ == "__main__":
    # Example usage
    write_log("Script started")
    write_log("Processing data...")
    write_log("Script completed") 