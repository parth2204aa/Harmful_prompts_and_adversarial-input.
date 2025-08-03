def generate_response(prompt: str) -> str:
    """
    Simulates model response. Replace with real model inference/API.
    """
    # Mock behavior: echo prompt or return canned reply
    if "bomb" in prompt.lower():
        return "I'm sorry, I can't help with that."
    return f"Response to: {prompt}"
