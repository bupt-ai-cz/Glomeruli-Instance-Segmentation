# [A deep learning-based approach for glomeruli instance segmentation from multi-stained renal biopsy pathologic images](https://github.com/bupt-ai-cz/Glomeruli-Instance-Segmentation/blob/main/resouces/paper-AJP.pdf)
This repo is the official implementation of our paper "A deep learning-based approach for glomeruli instance segmentation from multi-stained renal biopsy pathologic images".

## Pre-train models
Pytorch version: 1.2.0

[Snapshot images](https://drive.google.com/file/d/11DDUxmUpFDxx0r-Mf37k8_7P_vNgSOGy/view?usp=sharing) 

[WSIs](https://drive.google.com/file/d/1Rb00BRu3adhEVt47ciVZ3WCWQ938eQyV/view?usp=sharing)

## Training
Run 
``` python code/tools/train.py code/tools/cascade_mask_rcnn_r50_fpn_1x.py --work_dir="code/work_dirs" ```

This repo is developed based on [mmdetection](https://github.com/open-mmlab/mmdetection). Please refer to [get_started.md](https://github.com/open-mmlab/mmdetection/blob/master/docs/get_started.md) for more details.


## Please cite this paper, if it helps your research:
```
@article{jiang2021deep,
  title={A Deep Learning-Based Approach for Glomeruli Instance Segmentation from Multistained Renal Biopsy Pathologic Images},
  author={Jiang, Lei and Chen, Wenkai and Dong, Bao and Mei, Ke and Zhu, Chuang and Liu, Jun and Cai, Meishun and Yan, Yu and Wang, Gongwei and Zuo, Li and others},
  journal={The American Journal of Pathology},
  volume={191},
  number={8},
  pages={1431--1441},
  year={2021},
  publisher={Elsevier}
}
```

## Contact
Wenkai Chen
- email: wkchen@bupt.edu.cn, czhu@bupt.edu.cn
- wechat: cwkyiyi

If you have any questions, you can contact me directly.


