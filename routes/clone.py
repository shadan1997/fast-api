from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from controllers.clone_logic import *


router = APIRouter()


# add head only


@router.get("/check_clone")
async def root():
    return check_from_clone()


@router.get("/get_a_b")
async def get_a_b(a: int, b: int, token: Optional[str] = None):
    try:
        result = await fun_logic(a, b)
        return {"message": result}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
