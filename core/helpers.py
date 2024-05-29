import html
import os
import pandas as pd
import re
import requests
import numpy as np
from tqdm import tqdm
from core.replicateai import get_image_alt_text_from_replicate_hosted, get_image_alt_text_from_replicate_api
from core.openai import get_image_alt_from_open_ai

import urllib.parse

## Helper Functions

### Get Slug from url
def get_slug_from_url(url):
    """
    Extracts the slug from the last part of the URL.

    Args:
        url: The URL to extract the slug from.

    Returns:
        The slug extracted from the URL.
    """
    parsed_url = urllib.parse.urlparse(url)
    path_segments = parsed_url.path.split("/")
    slug = path_segments[-1]
    return slug


### HTML decoder
def decode_html_entities(text):
    """Unescapes HTML entities in a string."""
    return html.unescape(text)


### Check if file exists
def check_if_file_exists(file_path):
    """Check if the given file exists.

    Args:
        file_path: The path to the file.

    Returns:
        True if the file exists, False otherwise.
    """
    return os.path.exists(file_path) and os.path.isfile(file_path)


### Dataframe configuration
def create_or_append_dataframe(df_dictionary, data_frame=pd.DataFrame()):
    """
    Creates or appends a dictionary to a DataFrame.

    Args:
        df_dictionary: The dictionary to append.
        data_frame: The DataFrame to append to.

    Returns:
        The updated DataFrame.
    """
    df_to_append = pd.DataFrame([df_dictionary])
    data_frame = pd.concat([data_frame, df_to_append], ignore_index=True)
    return data_frame


def check_dataframe_is_not_empty(df):
    """
    Checks if a variable is a non-empty DataFrame.

    Args:
        df: The variable to check.

    Returns:
        True if the variable is a non-empty DataFrame, False otherwise.
    """
    if df is None:
        return False
    if isinstance(df, pd.DataFrame):
        return not df.empty
    return False


### Find the value in dataframe
def check_value_in_dataframe_api(value, column, dataframe):
    """
    Checks if a value exists n a DataFrame column.

    Args:
        value: The value to search for.
        column: The column to search in.
        dataframe: The DataFrame to search in.

    Returns:
        The matching row as a dictionary if found, None otherwise.
    """
    current_row = pd.DataFrame()
    if type(value) == list:  # if passed as array
        current_row = dataframe.loc[dataframe[column].isin(value)]
    else:  # else assuming it's a string or integer (single value)
        current_row = dataframe.loc[dataframe[column] == value]
    return current_row.to_dict('records')[0] if not current_row.empty else None


def convert_the_image_url_to_image_cdn(image_url):
    """
    Gets the CDN image URL for an image from the WordPress API.

    Args:
        image_url: The URL of the image.

    Returns:
        The CDN image URL and the redirected URL.
    """
    redirected_url = get_redirect_url(image_url)
    http_removed_url = re.sub(r'^https://', '', redirected_url)
    # Return the new image URL
    return 'https://i0.wp.com/' + http_removed_url, redirected_url


### Media Response
def get_redirect_url(url):
    """
    Gets the final redirected URL from a given URL.

    Args:
        url: The URL to get the final redirected URL for.

    Returns:
        The final redirected URL.
    """
    # Fetch the image from the URL
    response = requests.get(url, allow_redirects=True, headers=request_crawl_header)

    # If there were redirects, return the final URL, otherwise return the original URL
    if response.history:
        return response.url
    else:
        return url

def get_alt_text_for_image(image_url, access_key, model= 'replicate'):
    if( model == 'replicate' ):
        return get_image_alt_text_from_replicate_api(access_key, image_url)
    elif( model == 'openai'):
        return get_image_alt_from_open_ai(access_key, image_url)
    else : 
        return get_image_alt_text_from_replicate_hosted(image_url)
    

# multiple repo
def get_alt_text_for_list_of_image(image_list, access_key , model  = ''):
    """
    Get the alt text for a list of images.

    Args:
        image_list: The list of images to get the alt text for.

    Returns:
        The alt text for the list of images.
    """
    # Initialize the alt text list
    alt_text_list = []

    # Iterate through the list of images
    for image in image_list:
        # Get the alt text for the image
        alt_text = get_alt_text_for_image(image['url'], access_key, model)
        # Create a dictionary with the image URL and alt text
        image_dict = {'url': image, 'alt_text': alt_text}
        # Append the dictionary to the list
        alt_text_list.append(image_dict)

    return alt_text_list














