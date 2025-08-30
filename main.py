import os
from smolagents import CodeAgent, InferenceClientModel, tool

@tool
def get_weather(city: str) -> dict:
    """Returns sample weather data for a given city.
    
    Args:
        city: The name of the city to get weather data for
        
    Returns:
        A dictionary containing weather information
    """
    sample_data = {
        "paris": {"temperature": 18, "humidity": 65, "description": "Partly cloudy"},
        "new york": {"temperature": 20, "humidity": 80, "description": "Sunny"}
    }
    return sample_data.get(city.lower(), {"error": f"No data for {city}"})

# Try with explicit token
model = InferenceClientModel(token=os.getenv("HF_TOKEN"))
agent = CodeAgent(tools=[get_weather], model=model)

try:
    result = agent.run("What is the current weather in Paris?")
    print(result)
except Exception as e:
    print(f"HF Error: {e}")