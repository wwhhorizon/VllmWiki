# vllm-project/vllm#9738: [Bug]: offline inference with ray fails on multinode

| 字段 | 值 |
| --- | --- |
| Issue | [#9738](https://github.com/vllm-project/vllm/issues/9738) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: offline inference with ray fails on multinode

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running inference with Llama 3.1 405B instruct on 4 Nodes each with 4 A100 64 Gb, this are custom gpus for LEONARDO supercomputer in Italy, throws an error with all versions later than 0.5.4 while it does not error with that specific version, 0.5.4. @youkaichao Issue related to my message on slack, it is similar to one I had opened some time ago #8908, please let me know if some info about my environment is missing. ## Slurm script ```bash #!/bin/bash #SBATCH --nodes=4 #SBATCH --ntasks-per-node=1 #SBATCH --cpus-per-task=32 #SBATCH --gpus-per-task=4 #SBATCH --time=0-12:00:00 #SBATCH --partition=boost_usr_prod #SBATCH --account=myproject #SBATCH --job-name=generate_llama3.1_405b #SBATCH --output=slurm_logs/llm_llama3_sender-%j.out eval "$(conda shell.bash hook)" # init conda conda activate ./conda_venv_vllm module load gcc export CUDA_VISIBLE_DEVICES="0,1,2,3" nodes=$(scontrol show hostnames "$SLURM_JOB_NODELIST") # Getting the node names nodes_array=($nodes) node_1=${nodes_array[0]} ip=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1) port=6379 ip_head=$ip:$port export ip_head echo "I...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ustom gpus for LEONARDO supercomputer in Italy, throws an error with all versions later than 0.5.4 while it does not error with that specific version, 0.5.4. @youkaichao Issue related to my message on slack, it is simil...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g Running inference with Llama 3.1 405B instruct on 4 Nodes each with 4 A100 64 Gb, this are custom gpus for LEONARDO supercomputer in Italy, throws an error with all versions later than 0.5.4 while it does not error wi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ay fails on multinode bug;ray;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Running inference with Llama 3.1 405B instruct on 4 Nodes each with 4 A100 64 Gb, this are cust...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -w "$node_1" \ ray start --head --node-ip-address="$ip" --port=$port --block & sleep 10 worker_num=$(($SLURM_JOB_NUM_NODES - 1)) #number of nodes other than the head node for ((i = 1; i <= worker_num; i++)); do node_i=$...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: rate_llama3.1_405b #SBATCH --output=slurm_logs/llm_llama3_sender-%j.out eval "$(conda shell.bash hook)" # init conda conda activate ./conda_venv_vllm module load gcc export CUDA_VISIBLE_DEVICES="0,1,2,3" nodes=$(scontro...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
