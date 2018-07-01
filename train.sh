#!/bin/bash
source activate root
cd /Users/gy12/Desktop/notebooks/multi/1/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/2/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/3/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/4/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/5/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/6/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/7/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/8/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/9/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/11/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/12/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &
cd /Users/gy12/Desktop/notebooks/multi/13/MemN2N-split-memory;python single_dialog.py --train True --task_id 1 &

#cd /Users/gy12/Desktop/notebooks/multi; /Users/gy12/anaconda/envs/py35/bin/python distributer.py