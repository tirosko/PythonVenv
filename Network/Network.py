import subprocess
import json

def run_speedtest():
    try:
        # Run the speedtest command
        result = subprocess.run(['speedtest', '--format=json'], capture_output=True, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            # Parse the JSON output
            data = json.loads(result.stdout)
            
            # Extract relevant information
            download_speed = data['download']['bandwidth'] / 1e6  # Convert from bps to Mbps
            upload_speed = data['upload']['bandwidth'] / 1e6  # Convert from bps to Mbps
            ping = data['ping']['latency']
            
            # Print the results
            print(f"Download Speed: {download_speed:.2f} Mbps")
            print(f"Upload Speed: {upload_speed:.2f} Mbps")
            print(f"Ping: {ping:.2f} ms")
        else:
            print("Speedtest failed to run.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the speedtest
run_speedtest()
