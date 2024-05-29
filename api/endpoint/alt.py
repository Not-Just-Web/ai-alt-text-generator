from fastapi import Depends, HTTPException, status, APIRouter, Request, Query
from core.openai import set_up_open_ai, get_image_alt_from_open_ai
from core.replicateai import get_image_alt_text_from_replicate_hosted, get_image_alt_text_from_replicate_api
from core.helpers import get_alt_text_for_list_of_image

router = APIRouter()


@router.get('/')
async def get_alt_text_from_open_ai(image_url: str, request: Request, slug: str = ''):
    """
    Generate alt text from the OpenAI API.

    Args:
        image_url (str): The URL of the image for which alt text needs to be generated.
        slug (str, optional): A slug to identify the image. Defaults to ''.
        request (Request): The FastAPI request object.

    Raises:
        HTTPException: If no sitemap is found.

    Returns:
        str: The generated alt text for the image.
    """
    headers = request.headers
    # Access the Open AI headers as needed
    openAIKey = headers.get('access-key')
    if openAIKey is None:
        raise HTTPException(status_code=401, detail="Open AI Key not found in headers")
    
    alt_text = get_image_alt_from_open_ai(openAIKey, image_url, slug)
    if alt_text:
        return alt_text
    else:
        raise HTTPException(status_code=404, detail="Wasn't able to generate alt text for the image.")
    
@router.get('/replicate')
async def get_alt_text_from_replicate_ai(image_url: str, request: Request, slug: str = ''):
    """
    Generate alt text from the OpenAI API.

    Args:
        image_url (str): The URL of the image for which alt text needs to be generated.
        slug (str, optional): A slug to identify the image. Defaults to ''.
        request (Request): The FastAPI request object.

    Raises:
        HTTPException: If no sitemap is found.

    Returns:
        str: The generated alt text for the image.
    """
    headers = request.headers
    # Access the Open AI headers as needed
    replicateKey = headers.get('access-key');
    if replicateKey is None:
        raise HTTPException(status_code=401, detail="Replicate Key not found in headers")
    alt_text = get_image_alt_text_from_replicate_api(replicateKey, image_url)
    if alt_text:
        return alt_text
    else:
        raise HTTPException(status_code=404, detail="Wasn't able to generate alt text for the image.")

@router.get('/from-hosted')
async def get_alt_text_from_replicate_ai(image_url: str):
    """
    Generate alt text from the OpenAI API.

    Args:
        image_url (str): The URL of the image for which alt text needs to be generated.
        slug (str, optional): A slug to identify the image. Defaults to ''.
        request (Request): The FastAPI request object.

    Raises:
        HTTPException: If no sitemap is found.

    Returns:
        str: The generated alt text for the image.
    """
   
    return get_image_alt_text_from_replicate_hosted(image_url)

@router.post('/bulk')
async def get_alt_text_from_api(content: dict, request: Request,  model: str = Query(...)) :
    """
    Generate alt text from the OpenAI API.

    Args:
        image_url (str): The URL of the image for which alt text needs to be generated.
        slug (str, optional): A slug to identify the image. Defaults to ''.
        request (Request): The FastAPI request object.

    Raises:
        HTTPException: If no sitemap is found.

    Returns:
        list: The generated alt text for the each image.
    """
    headers = request.headers
    # Access the Open AI headers as needed
    accessKey = headers.get('access-key')

    return get_alt_text_for_list_of_image(content, accessKey, model)


