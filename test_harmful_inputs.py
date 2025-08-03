# test_harmful_inputs.py

import pytest
import json
from model_interface import generate_response
from toxicity_detector import is_response_harmful

# Load harmful prompts
with open("harmful_prompts.json", "r", encoding="utf-8") as f:
    harmful_prompts = json.load(f)

@pytest.mark.parametrize("prompt_data", harmful_prompts)
def test_harmful_prompt(prompt_data):
    input_text = prompt_data["input"]
    response = generate_response(input_text)

    assert not is_response_harmful(response), \
        f"Harmful response for: {input_text}\nModel Response: {response}"
