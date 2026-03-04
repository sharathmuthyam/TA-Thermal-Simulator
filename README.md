# TA Thermal Simulator — Virtual Instrument Lab

A Python-based end-to-end test automation framework that simulates thermal analysis instrument signals, validates software output against golden files, and tests fault handling — without requiring physical hardware.

## Project Structure
```
TA_Simulator/
├── simulator.py          # Generates realistic thermal sensor signals
├── software_simulator.py # Mock processor (stands in for real software)
├── save_golden.py        # Saves correct output as golden baseline
├── test_runner.py        # Compares output against golden file
└── fault_injector.py     # Injects bad data to test error handling
```

## How It Works

1. **Simulator** generates temperature readings (25°C–300°C) with realistic noise
2. **Processor** analyzes signals — average, peak, threshold breach detection
3. **Golden files** store known-correct output from a clean run
4. **Test runner** re-runs same readings and compares — catches regressions automatically
5. **Fault injector** sends bad data (out of range, missing, empty) — exposes crashes and silent failures

## Fault Injection Results

| Fault Type | Result | Finding |
|---|---|---|
| Out of range (9999°C) | ⚠️ Processed | Peak value accepted without validation |
| Noisy spike | ⚠️ Processed | Average skewed significantly |
| Timeout (empty) | ❌ Crashed | max() fails on empty list |
| Missing reading (None) | ❌ Crashed | None comparison not handled |

## Why This Matters

These findings would be reported to developers as bugs requiring error handling fixes — exactly how fault injection works in a real test automation pipeline.

## Run It Yourself
```bash
python simulator.py        # generate signals
python save_golden.py      # save golden baseline
python test_runner.py      # validate against golden file
python fault_injector.py   # run fault injection tests
```

## Tech Stack
Python | JSON | Git
