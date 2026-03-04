import random
from software_simulator import process_signals

def inject_faults(fault_type):
    
    # normal readings first
    normal = [48.95, 72.33, 99.46, 124.52, 146.91,
              170.66, 199.42, 222.06, 250.36, 274.95]
    
    if fault_type == "out_of_range":
        faulty = normal.copy()
        faulty[4] = 9999.99  # extreme spike
        return faulty
    
    elif fault_type == "noisy_spike":
        faulty = normal.copy()
        faulty[random.randint(0,9)] = random.uniform(500, 1000)
        return faulty
    
    elif fault_type == "timeout":
        return []  # empty - sensor died
    
    elif fault_type == "missing_reading":
        faulty = normal.copy()
        faulty[3] = None  # sensor missed a reading
        return faulty

def run_fault_tests():
    faults = ["out_of_range", "noisy_spike", "timeout", "missing_reading"]
    
    for fault in faults:
        print(f"\n=== Testing fault: {fault} ===")
        faulty_readings = inject_faults(fault)
        
        try:
            output = process_signals(faulty_readings)
            print(f"⚠️  Software processed without crashing: {output}")
        except Exception as e:
            print(f"❌ Software CRASHED: {e}")

if __name__ == "__main__":
    run_fault_tests()