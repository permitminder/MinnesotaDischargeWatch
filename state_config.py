"""
State configuration for this MinnesotaDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "MN"
STATE_NAME = "Minnesota"
APP_NAME = "MinnesotaDischargeWatch"
APP_TAGLINE = "Minnesota Discharge Monitoring"
DOMAIN = "minnesotadischargewatch.org"
DATA_FILE = "mn_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@minnesotadischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "CST"
EPA_REGION = 5
