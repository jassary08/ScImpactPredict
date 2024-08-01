OMP_NUM_THREADS=1 accelerate launch train.py \
    --base_lr 1e-4 \
    --total_epochs 15 \
    --loss_func mse \
    --data_style 8 \
    --warmup_ratio 0.03 \
    --weight_decay -1 \
    --max_norm -1.0 \
    --seed -1 \
    --train_ratio 0.9 \
    --data_path /home/u1120220285/ScitePredict/NAID/NAID_full.csv \

python scancel.py