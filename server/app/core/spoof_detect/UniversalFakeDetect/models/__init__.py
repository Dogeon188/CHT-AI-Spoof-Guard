from .clip_models import CLIPModel


VALID_NAMES = [

    'CLIP:RN50', 
    'CLIP:RN101', 
    'CLIP:RN50x4', 
    'CLIP:RN50x16', 
    'CLIP:RN50x64', 
    'CLIP:ViT-B/32', 
    'CLIP:ViT-B/16', 
    'CLIP:ViT-L/14', 
    'CLIP:ViT-L/14@336px',
]





def get_model(name):
    assert name in VALID_NAMES
    if name.startswith("CLIP:"):
        return CLIPModel(name[5:])  
    else:
        assert False 
