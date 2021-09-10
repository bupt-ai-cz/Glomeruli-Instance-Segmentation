from datasets import MyDataset
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True, with_mask=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks']),
]
dataset = MyDataset('/home/chenwenkai/WSI-data/second/new/coco-train-modified.json',train_pipeline,'/home/chenwenkai/WSI-data/second/new/','/home/chenwenkai/WSI-data/second/new/')

print(dataset.__getitem__(0))