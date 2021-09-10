from .coco import CocoDataset
from .registry import DATASETS


@DATASETS.register_module
class MyDataset_g(CocoDataset):

    CLASSES = ('1')