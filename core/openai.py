from openai import OpenAI
from core.config import get_config_by_name


def set_up_open_ai(api_key: str):
    """
    Sets up the OpenAI API client.

    Returns:
        The OpenAI API client.
    """
    OpenApi_client = OpenAI(api_key=api_key)
    return OpenApi_client


def get_image_alt_from_open_ai(api_key, image_url, slug=''):
    """
    Gets the alt text for an image from the OpenAI API.

    Args:
        api_key: The OpenAI API key.
        image_url: The URL of the image.
        slug: The slug to append to the prompt.

    Returns:
        The alt text for the image.
    """
    openAiclient = set_up_open_ai(api_key)
    prompt = get_config_by_name("prompt")
    image_name_prompt = prompt.get("image_prompt")
    alt_prompt = prompt.get("alt_prompt")
    prompt_to_send = image_name_prompt + slug + '.' + alt_prompt
    response = openAiclient.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_to_send},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    if response.choices is not None and response.choices[0].message is not None and response.choices[0].message.content is not None:
        return response.choices[0].message.content
    else:
        return None