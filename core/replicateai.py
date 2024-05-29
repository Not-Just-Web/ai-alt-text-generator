import requests
import replicate
from core.config import get_config_by_name


def setup_replicate_api(api_key: str):
    """
    Sets up the Replicate API client.

    Returns:
        The Replicate API client.
    """
    replicate_api = replicate.Client(api_token=api_key)
    return replicate_api

def get_image_alt_text_from_replicate_hosted(image_url):
    """
    Gets the alt text for an image from the hosted Replicate API.

    Args:
        image_url: The URL of the image.

    Returns:
        The alt text for the image.
    """
    replicate_hosted_url = get_config_by_name("replicate_hosted_url")
    url = replicate_hosted_url + "/api/generate"
    params = {"imageUrl": image_url}

    response = requests.get(url, params=params)

    return response.text

### Replicate API
def get_image_alt_text_from_replicate_api(api_key, image_url="https://replicate.delivery/pbxt/KRULC43USWlEx4ZNkXltJqvYaHpEx2uJ4IyUQPRPwYb8SzPf/view.jpg"):
    """
    Gets the alt text for an image from the Replicate API.

    Args:
        image_url: The URL of the image.

    Returns:
        The alt text for the image.
    """
    input = {
        "image": image_url,
        "prompt": get_config_by_name("prompt")['alt_prompt'],
    }
    replicate_api = setup_replicate_api(api_key)
    output = replicate_api.run("yorickvp/llava-13b:b5f6212d032508382d61ff00469ddda3e32fd8a0e75dc39d8a4191bb742157fb", input=input)
    output_string = ''.join(str(item) for item in output)
    return output_string