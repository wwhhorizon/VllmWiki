# vllm-project/vllm#26028: [Bug]: The number of required GPUs exceeds the total number of available GPUs in the placement group. For multi-node multi-GPU inference.

| 字段 | 值 |
| --- | --- |
| Issue | [#26028](https://github.com/vllm-project/vllm/issues/26028) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: The number of required GPUs exceeds the total number of available GPUs in the placement group. For multi-node multi-GPU inference.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I have tried looking through relevant docs/ issues but am still struggling to get my multi-node multi-gpu inference running with vllm. I am running on HPC using A100 80GB GPUs. Here is my slurm script: ``` #!/bin/bash # vim: et:ts=4:sts=4:sw=4 #SBATCH --time 0:30:0 #SBATCH --nodes 2 #SBATCH --gpus-per-node 4 #SBATCH --ntasks-per-node 4 #SBATCH --job-name test_multi_node #SBATCH --output test_multi_node.log #SBATCH --constraint=a100_80 echo "--------------------------------------" echo echo echo "New job: ${SLURM_JOB_ID}" echo "--------------------------------------" module purge module load baskerville module load Python NCCL export NCCL_SOCKET_IFNAME=ib0 # or the IB interface on Baskerville export NCCL_IB_DISABLE=0 export NCCL_P2P_DISABLE=0 export NCCL_IB_HCA=mlx5 export NCCL_DEBUG=INFO # optional, for debugging # for the python script export MASTER_PORT=$((16384 + $SLURM_JOB_ID % 16384)) export MASTER_ADDR=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1) # for vllm run export PRIMARY_PORT=$MASTER_PORT export PRIMARY_HOST=$MASTER_ADDR #export PRIMARY_IP=$(getent hosts $PRIMARY_HOST | awk '{print $1}') export PRIMARY_...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: # test nccl works srun -N2 -n8 --ntasks-per-node=4 bash -c "NCCL_DEBUG=VERSION python nccl_test.py" # run vllm srun -N2 -n2 --ntasks-per-node=1 -l ./vllm_run.sh wait ``` Here is my vllm_run.sh script: ``` #!/bin/bash so...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: our firewall settings and network configuration. 1: 1: 0: ======== Autoscaler status: 2025-10-01 14:34:02.613693 ======== 0: Node status 0: --------------------------------------------------------------- 0: Active: 0: 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: y 0: 0B/294.99GiB object_store_memory 0: 0: Total Constraints: 0: (no request_resources() constraints) 0: Total Demands: 0: (no resource demands) 0: 0: ======== List: 2025-10-01 14:34:08.349556 ======== 0: Stats: 0: ---...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: echo "Running vLLM benchmark..." vllm bench throughput \ --model Qwen/Qwen3-30B-A3B-Instruct-2507 \ --input-len 512 \ --output-len 1024 \ -tp 4 -pp ${SLURM_NNODES} --distributed-executor-backend ray fi ``` Here are outp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 1024 \ -tp 4 -pp ${SLURM_NNODES} --distributed-executor-backend ray fi ``` Here are output logs: ``` -------------------------------------- New job: 1112356 -------------------------------------- GCCcore/12.3.0 zlib/1.2...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
