python v2_resource/v2_test.py \
  --ckpt_dir "$CKPT_DIR" \
  --test_data_path "$TEST_SET" \
  --gt_field "RTS" \
  --batch_size 8 \
  --max_length 512 \
  --load_in_8bit true
