config = {
  "prompt" : {
    "image_prompt" : "The image provided with this prompt is mentioned in ",
    "alt_prompt" : "Please provide the alt text (to be used on html img tag) for this image, also use provided image url or article slug to determine character name, movies or any to get relevant info if any ensuring it describes the image for individuals who cannot see it. Only report output on plain text and make it precise and maximum 125 character"
  },
  "replicate_hosted_url" : "https://alt-text-generator.vercel.app",
}


def get_config_by_name(name):
    """
    Retrieves a configuration value by its name.

    Args:
        name (str): The name of the configuration value to retrieve.

    Returns:
        The value associated with the given name, or None if the name is not found in the configuration.

    """
    return config.get(name, None)