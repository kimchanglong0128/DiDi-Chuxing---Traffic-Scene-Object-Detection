import os

config_path = "C:\\Users\\31393\\Desktop\\result\\faster_rcnn_r50_fpn_1x_didi(train)\\faster_rcnn_r50_fpn_1x_didi.py"
checkpoint_dir = "C:\\Users\\31393\\Desktop\\result\\faster_rcnn_r50_fpn_1x_didi(train)"

checkpoints = os.listdir(checkpoint_dir)
checkpoints = [file for file in checkpoints if file.endswith('.pth')]

for checkpoint in checkpoints:
    checkpoint_path = os.path.join(checkpoint_dir, checkpoint)
    os.system(f"python tools/test.py {config_path} {checkpoint_path}")
