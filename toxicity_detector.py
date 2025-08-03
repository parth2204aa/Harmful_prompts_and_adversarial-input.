# toxicity_detector.py

from detoxify import Detoxify

model = Detoxify('original')

def is_response_harmful(response: str) -> bool:
    """
    Check if the response contains harmful content using Detoxify.
    """
    scores = model.predict(response)
    return any(scores[key] > 0.5 for key in scores)
