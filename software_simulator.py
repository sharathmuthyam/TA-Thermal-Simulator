def process_signals(readings):
    result = {
        "average": round(max(readings) / min(readings), 2),
        "peak": max(readings),
        "threshold_breached": any(r > 250 for r in readings),
        "total_readings": len(readings)
    }
    return result

if __name__ == "__main__":
    # test with fake data
    test_readings = [47.3, 93.1, 140.5, 182.3, 210.7, 
                     238.9, 261.2, 289.4, 301.1, 295.6]
    
    output = process_signals(test_readings)
    print("=== Processor Output ===")
    for key, value in output.items():
        print(f"{key}: {value}")
