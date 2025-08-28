weather_app/                      # Main project folder (package)
│
├── api/                          # Package (for API handling)
│   ├── __init__.py
│   ├── connection.py             # Module (connect to API)
│   └── authentication.py         # Module (store/manage API key)
│
├── models/                       # Package (for data models)
│   ├── __init__.py
│   ├── weather_data.py           # Module (class WeatherData)
│   └── forecast.py               # Module (class Forecast)
│
├── services/                     # Package (business logic)
│   ├── __init__.py
│   ├── current_weather.py        # Module (get current weather)
│   └── weekly_forecast.py        # Module (get weekly forecast)
│
├── docs/                         # Documentation
│   └── usage.md                  # Explains how to use project
│
├── cli.py                        # CLI interface (main script)
└── README.md                     # Project overview
