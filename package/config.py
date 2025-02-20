from pathlib import Path
from dataclasses import dataclass
from loguru import logger


@dataclass
class Arguments:


    # data pre-processing
    

    # training parameters
    max_epochs:int
    learning_rate:float
    weightdecay:float

    # data augmentation



