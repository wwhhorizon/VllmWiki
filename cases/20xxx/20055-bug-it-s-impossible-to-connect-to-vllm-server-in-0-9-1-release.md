# vllm-project/vllm#20055: [Bug]: It's impossible to connect to vllm server in 0.9.1 release

| 字段 | 值 |
| --- | --- |
| Issue | [#20055](https://github.com/vllm-project/vllm/issues/20055) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: It's impossible to connect to vllm server in 0.9.1 release

### Issue 正文摘录

### 🐛 Describe the bug Simply as the title suggest, with 0.9.1 release, it is impossible to connect to vllm as a server. I am working with HuggingFace TRL library. I previously used vllm to run completions with for [grpo](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_trainer.py) training with not issues. But, things have changed since 0.9.1 release. The workflow is simply like this: first, start a dedicated node for vllm as the server. Then start the training and connect to the server. You can accomplish this by running this slurm script end-to-end: ``` #!/bin/bash #SBATCH --nodes=2 #SBATCH --ntasks-per-node=1 #SBATCH --exclusive #SBATCH --gres=gpu:8 #SBATCH --dependency=singleton TRAINING_SCRIPT="../src/open_r1/grpo.py" ACCELERATE_CONFIG_FILE="../recipes/accelerate_configs/zero2.yaml" CONFIG_FILE="../recipes/qwen2.5/grpo_qwen2.5_math_serv.yaml" MODEL=deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B LOGS_DIR="${SAVE_DIR}/${NAME}/" mkdir -p "${LOGS_DIR}" DATETIME=$(date +'%Y-%m-%d_%H-%M-%S') # ----------------- # 2) SLURM Node Info # ----------------- NODELIST=($(scontrol show hostnames $SLURM_JOB_NODELIST)) TOTAL_NODES=$SLURM_NNODES MASTER_NODE="${NODELIST[0]}" MASTER_ADD...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: se, it is impossible to connect to vllm as a server. I am working with HuggingFace TRL library. I previously used vllm to run completions with for [grpo](https://github.com/huggingface/trl/blob/main/trl/trainer/grpo_tra...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: H --ntasks-per-node=1 #SBATCH --exclusive #SBATCH --gres=gpu:8 #SBATCH --dependency=singleton TRAINING_SCRIPT="../src/open_r1/grpo.py" ACCELERATE_CONFIG_FILE="../recipes/accelerate_configs/zero2.yaml" CONFIG_FILE="../re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g" \ bash -c " echo \"[vLLM Node] Starting vLLM on \$(hostname -s)\" CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 \\ python -m trl.scripts.vllm_serve \ --model \"$MODEL\" \\ --tensor_parallel_size \"$TP\" \\ --data_parallel_siz...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: It's impossible to connect to vllm server in 0.9.1 release bug;stale ### 🐛 Describe the bug Simply as the title suggest, with 0.9.1 release, it is impossible to connect to vllm as a server. I am working with Hugg...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ess_port $MASTER_PORT \\ --machine_rank \$MACHINE_RANK \\ --rdzv_backend=c10d \\ --max_restarts 3 \\ --tee 3 \\ $TRAINING_SCRIPT \\ --config $CONFIG_FILE \\ --dataset-prompt-column problem \\ --vllm_server_host $VLLM_NO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
