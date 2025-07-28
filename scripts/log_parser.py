"""
SOC Log Analysis Tool
Purpose: Identify brute force attacks in authentication logs
Next Steps: Add Splunk integration
"""
import pandas as pd

def analyze_logs(file):
    """Detects failed login attempts"""
    logs = pd.read_csv(file)
    return logs[logs['status'] == 'FAILED']