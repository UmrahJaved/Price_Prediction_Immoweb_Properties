from pydantic import BaseModel,Field
from typing import Literal, Optional

"""
Validating  user_input 

"""
class feature():
    yes = "True"
    no = "False"

class validate(BaseModel):
    proprety_type: str = "House"
    bedrooms: int = 2
    area: int
    equipped_kitchen: Optional[str] = "Installed"
    furnished: feature = Optional[bool]
    open_fire: Optional[bool] = Field(0)
    terrace: Optional[bool] = False
    terrace_area: Optional[int] = 0
    garden: Optional[bool] = False
    garden_area: Optional[int] = 0
    surface: Optional[int] = 201
    surface_plot: Optional[int] = 201
    facade: Optional[int] = 2
    state: Optional[Literal["NEW", "GOOD", "TO RENOVATE", "JUST RENOVATED", "TO REBUILD"]] = "GOOD"
    swimming_pool: Optional[bool] = False
    Address: Optional[str]

    class config():
        arbitrary_types_allowed= True


       
    
    
    
    
    
   
    
    
    
    
    

