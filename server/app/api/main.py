from fastapi import APIRouter, HTTPException

from .models import SpoofDetectRequest, SpoofDetectResponse, TextImageRelationRequest, TextImageRelationResponse
from app.core.spoof_detect import models as spoof_detect_models
from app.core.text_image_relation import models as text_image_relation_models


router = APIRouter()


@router.get("/spoof_detect/models", name="List Image Spoof Detection Models")
async def list_spoof_detect_models() -> list[str]:
    """List available image spoof detection models"""

    return list(spoof_detect_models.keys())


@router.post("/spoof_detect", name="Image Spoof Detection")
async def spoof_detect(body: SpoofDetectRequest) -> SpoofDetectResponse:
    """Detect AI spoof of a given image"""

    # Get model from request
    model = spoof_detect_models.get(body.model)
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Model not found: {body.model}. "
            f"Available models: {', '.join(spoof_detect_models.keys())}")

    # TODO
    # Get image from request

    # TODO
    # Use the AI model to detect spoof

    # Return the result
    return model.reference(body)


@router.get("/text_image_relation/models", name="List Text Image Relationship Models")
async def list_text_image_relation_models() -> list[str]:
    """List available text-image relationship models"""

    return list(text_image_relation_models.keys())


@ router.post("/text_image_relation", name="Text Image Relationship Calculation")
async def text_image_relation(body: TextImageRelationRequest) -> TextImageRelationResponse:
    """Calculate the (evidential) relationship between a given text and image"""

    # Get model from request
    model = text_image_relation_models.get(body.model)
    if model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Model not found: {body.model}. "
            f"Available models: {', '.join(text_image_relation_models.keys())}")

    # TODO
    # Get the text from request

    # TODO
    # Get the image from request

    # TODO
    # Use the AI model to calculate the relationship

    # Return the result
    return model.reference(body)
