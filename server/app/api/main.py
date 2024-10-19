from fastapi import APIRouter, HTTPException
from time import time

from .models import SpoofDetectRequest, SpoofDetectResponse, TextImageRelationRequest, TextImageRelationResponse
from app.core import spoof_detect_models, text_image_relation_models


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

    # Get image from request
    image_url = body.image

    # Use the AI model to detect spoof
    try:
        start_time = time()
        res = model.reference(image=image_url)
        end_time = time()

        # Return the result
        return SpoofDetectResponse(
            uuid=body.uuid,
            model=body.model,
            processing_time={
                "start": start_time,
                "end": end_time,
                "duration_ms": (end_time - start_time) * 1000},
            result=res.result,
            confidence=res.confidence
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e))


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

    # Get the text & image from request
    text = body.text
    image_url = body.image

    # Use the AI model to calculate the relationship
    start_time = time()
    res = model.reference(text=text, image=image_url)
    end_time = time()

    # Return the result
    return TextImageRelationResponse(
        uuid=body.uuid,
        model=body.model,
        processing_time={
            "start": start_time,
            "end": end_time,
            "duration_ms": (end_time - start_time) * 1000},
        result=res.result,
        confidence=res.confidence
    )
