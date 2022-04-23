from campaign.event_20200521_cn.b1 import Config as ConfigBase
from module.campaign.campaign_base import CampaignBase
from module.logger import logger
from module.map.map_base import CampaignMap
from module.map.map_grids import RoadGrids, SelectedGrids

MAP = CampaignMap()
MAP.map_data = """
    -- -- -- -- -- -- -- -- -- -- -- -- -- ++
    -- -- -- -- -- -- -- -- -- -- -- -- -- --
    ++ -- -- -- -- -- -- -- -- -- -- -- -- --
    ++ -- -- -- -- -- -- -- -- -- -- -- -- --
    -- -- -- -- -- -- -- -- -- -- -- -- ++ ++
    -- ++ -- -- ++ ++ -- -- ++ ++ -- -- -- --
    -- ++ -- -- ++ ++ -- -- ++ ++ -- -- -- --
    -- -- -- -- -- -- -- -- -- -- -- -- ++ ++
    ++ -- -- -- -- -- -- -- -- -- -- -- ++ ++
    -- -- -- -- -- -- -- -- -- -- -- -- -- --
"""
MAP.camera_data = ['G8', 'G6', 'F3', 'H4']
MAP.wall_data = """
    ·   ·   ·   ·   · | ·   ·   ·   · | ·   ·   ·   ·   · ,
          +-----------+               +-----------+       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          |           |               |           |       ,
    ·   · | ·   ·   · | ·   ·   ·   · | ·   ·   · | ·   · ,
          +---+       +---+       +----+       +---+       ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |            ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              |                               |           ,
    ·   ·   · | ·   ·   ·   ·   ·   ·   ·   · | ·   ·   · ,
              +-----------+       +-----------+           ,
    ·   ·   ·   ·   ·   · | ·   · | ·   ·   ·   ·   ·   · ,
"""


class Config(ConfigBase):
    FLEET_BOSS = 2

    MAP_HAS_WALL = True
    MAP_SIREN_TEMPLATE = ['LaGalissonniere', 'Vauquelin']


class Campaign(CampaignBase):
    MAP = MAP
