from typing import Literal
from pydantic import BaseModel, Field, AfterValidator
from uuid import UUID
from typing import Annotated


# Base models for request and response

ImageModel = Annotated[
    str,
    Field(
        description="Image data in (data) URL string format",
        examples=[
            "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBYRXhpZgAATU0AKgAAAAgAA1IBAAABAAEAAAgAA1...",
            "https://example.com/image.jpg"
        ])
]


class ProcessingTime(BaseModel):
    """Processing time model"""
    start: float = Field(
        description="Timestamp of start of processing",
        example=1620000000.0)
    end: float = Field(
        description="Timestamp of end of processing",
        example=1620000001.0)
    duration_ms: float = Field(
        description="Duration of processing in milliseconds",
        example=1000.0)


class QueryRequestBase(BaseModel):
    """Base model for query request"""
    uuid: UUID = Field(
        description="Unique identifier of the request session, in UUID v4 format")
    model: str = Field(
        description="Name of the model to be used for processing",
        example="v0")


class QueryResponseBase(BaseModel):
    """Base class for query response
    Attributes:
        uid: Unique identifier of the request
        result: Result of the processing
        processing_time: Processing time of the request"""
    uuid: UUID = Field(
        description="Unique identifier of the request session, in UUID v4 format")
    model: str = Field(
        description="Name of the model used for processing",
        example="v0")
    processing_time: ProcessingTime


# Models for request and response of spoof_detect


class SpoofDetectRequest(QueryRequestBase):
    """Request class for spoof_detect"""
    image: ImageModel


class SpoofDetectResponse(QueryResponseBase):
    """Response class for spoof_detect"""
    result: Literal["real", "spoof"] = Field(
        description="Result of the AI image spoof detection, either 'real' or 'spoof'",
        example="real")
    confidence: float = Field(
        description="Confidence of the result, between 0 and 1",
        example=0.9)


# Models for request and response of text_image_relation


class TextImageRelationRequest(QueryRequestBase):
    """Request class for text_image_relation"""
    text: str = Field(
        description="Text to be queried",
        example="A cat is sitting on a mat")
    image: ImageModel


class TextImageRelationResponse(QueryResponseBase):
    """Response class for text_image_relation"""
    result: Literal["related", "unrelated"] = Field(
        description="Result of the AI text-image relationship calculation, either 'related' or 'unrelated'",
        example="related")
    confidence: float = Field(
        description="Score of the relationship, between 0 and 1",
        example=0.9)
