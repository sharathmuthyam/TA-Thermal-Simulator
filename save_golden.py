import json
from simulator import generate_thermal_signal
from software_simulator import process_signals

def save_golden_file():
    # generate signals
    readings = generate_thermal_signal()
    
    # process them
    output = process_signals(readings)
    
    # save as golden file
    golden_data = {
        "readings": readings,
        "expected_output": output
    }
    
    with open("golden_files/baseline.json", "w") as f:
        json.dump(golden_data, f, indent=4)
    
    print("✅ Golden file saved!")
    print(json.dumps(golden_data, indent=4))

if __name__ == "__main__":
    save_golden_file()