from fastapi import APIRouter, HTTPException

from .models import SpoofDetectRequest, SpoofDetectResponse, TextImageRelationRequest, TextImageRelationResponse


router = APIRouter()


@router.get("/spoof_detect", name="Image Spoof Detection")
async def spoof_detect(body: SpoofDetectRequest) -> SpoofDetectResponse:
    """Detect AI spoof of a given image"""

    # TODO: Get the image from the request
    # TODO: Use the AI model to detect spoof
    # TODO: Return the result

    raise HTTPException(status_code=501, detail="Not implemented yet")


@ router.get("/text_image_relation", name="Text Image Relationship Calculation")
async def text_image_relation(body: TextImageRelationRequest) -> TextImageRelationResponse:
    """Calculate the (evidential) relationship between a given text and image"""

    # TODO: Get the text and image from the request
    # TODO: Use the AI model to calculate the relationship
    # TODO: Return the result

    raise HTTPException(status_code=501, detail="Not implemented yet")
