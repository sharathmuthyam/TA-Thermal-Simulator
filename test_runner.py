import json
from software_simulator import process_signals

def run_test():
    # load golden file
    with open("golden_files/baseline.json", "r") as f:
        golden_data = json.load(f)
    
    golden_readings = golden_data["readings"]
    expected_output = golden_data["expected_output"]
    
    # run same readings through processor
    actual_output = process_signals(golden_readings)
    
    print("=== Test Runner ===")
    print(f"Expected: {expected_output}")
    print(f"Actual:   {actual_output}")
    
    # compare each field
    all_passed = True
    for key in expected_output:
        if expected_output[key] == actual_output[key]:
            print(f"✅ {key}: PASS")
        else:
            print(f"❌ {key}: FAIL")
            print(f"   Expected: {expected_output[key]}")
            print(f"   Actual:   {actual_output[key]}")
            all_passed = False
    
    if all_passed:
        print("\n✅ ALL TESTS PASSED")
    else:
        print("\n❌ TESTS FAILED - regression detected!")

if __name__ == "__main__":
    run_test()