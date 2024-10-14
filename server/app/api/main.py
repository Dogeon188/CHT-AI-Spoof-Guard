from fastapi import APIRouter, HTTPException

from .models import SpoofDetectRequest, SpoofDetectResponse, TextImageRelationRequest, TextImageRelationResponse
from app.core.spoof_detect import models as spoof_detect_models
from app.core.text_image_relation import models as text_image_relation_models


router = APIRouter()


@router.post("/spoof_detect", name="Image Spoof Detection")
async def spoof_detect(body: SpoofDetectRequest) -> SpoofDetectResponse:
    """Detect AI spoof of a given image"""

    model = spoof_detect_models.get(body.model)
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Model not found: {body.model}. "
            f"Available models: {', '.join(spoof_detect_models.keys())}")

    # TODO: Get the image from the request

    # TODO: Use the AI model to detect spoof

    # TODO: Return the result
    return model.reference(body)


@ router.post("/text_image_relation", name="Text Image Relationship Calculation")
async def text_image_relation(body: TextImageRelationRequest) -> TextImageRelationResponse:
    """Calculate the (evidential) relationship between a given text and image"""

    model = text_image_relation_models.get(body.model)
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Model not found: {body.model}. "
            f"Available models: {', '.join(text_image_relation_models.keys())}")

    # TODO: Get the text from the request

    # TODO: Get the image from the request

    # TODO: Use the AI model to calculate the relationship

    # TODO: Return the result
    return model.reference(body)
