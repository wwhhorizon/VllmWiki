# vllm-project/vllm#20871: [Bug]: ValueError: There is no module or parameter named 'base_model' in Qwen2ForCausalLM

| 字段 | 值 |
| --- | --- |
| Issue | [#20871](https://github.com/vllm-project/vllm/issues/20871) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: ValueError: There is no module or parameter named 'base_model' in Qwen2ForCausalLM

### Issue 正文摘录

I finetuned internvl 2.5 1b on custom dataset using Lora. The dataset had about 1800 samples. The task was to extract data from cheques. Below is the .sh file I ran ```` set -x GPUS=${GPUS:-1} BATCH_SIZE=${BATCH_SIZE:-4} PER_DEVICE_BATCH_SIZE=${PER_DEVICE_BATCH_SIZE:-4} GRADIENT_ACC=$((BATCH_SIZE / PER_DEVICE_BATCH_SIZE / GPUS)) export PYTHONPATH=/home/azim/internvl/InternVL/internvl_chat:$PYTHONPATH export MASTER_PORT=34229 export TF_CPP_MIN_LOG_LEVEL=3 export LAUNCHER=pytorch OUTPUT_DIR='/home/azim/internvl/InternVL/internvl_chat/shell/work_dirs/internvl_chat_v2_5/koresaimodel/' if [ ! -d "$OUTPUT_DIR" ]; then mkdir -p "$OUTPUT_DIR" fi torchrun \ --nnodes=1 \ --node_rank=0 \ --master_addr=127.0.0.1 \ --nproc_per_node=${GPUS} \ --master_port=${MASTER_PORT} \ InternVL/internvl_chat/internvl/train/internvl_chat_finetune.py \ --model_name_or_path "OpenGVLab/InternVL2_5-1B" \ --conv_style "internvl2_5" \ --use_fast_tokenizer False \ --output_dir ${OUTPUT_DIR} \ --meta_path "/home/azim/internvl/InternVL/internvl_chat/shell/data/batch1.json" \ --overwrite_output_dir True \ --max_dynamic_patch 6 \ --down_sample_ratio 0.5 \ --drop_path_rate 0.0 \ --freeze_llm False \ --freeze_mlp False \...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ora 16 \ --vision_select_layer -1 \ --dataloader_num_workers 4 \ --bf16 True \ --num_train_epochs 1 \ --per_device_train_batch_size ${PER_DEVICE_BATCH_SIZE} \ --gradient_accumulation_steps ${GRADIENT_ACC} \ --evaluation...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: ValueError: There is no module or parameter named 'base_model' in Qwen2ForCausalLM bug;stale I finetuned internvl 2.5 1b on custom dataset using Lora. The dataset had about 1800 samples. The task was to extract d...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: gth True \ --dynamic_image_size True \ --use_thumbnail True \ --ps_version 'v2' \ --deepspeed "/home/azim/internvl/InternVL/internvl_chat/zero_stage1_config.json" \ --report_to "tensorboard" \ 2>&1 | tee -a "${OUTPUT_DI...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ere is no module or parameter named 'base_model' in Qwen2ForCausalLM bug;stale I finetuned internvl 2.5 1b on custom dataset using Lora. The dataset had about 1800 samples. The task was to extract data from cheques. Bel...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nt id, transaction code, drawer names from this Indian cheque.The bottom numeric code region (highlighted in light red) contains:Cheque Number, MICR Code, Account ID, Transaction Code. The Date is in the top right corne...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
