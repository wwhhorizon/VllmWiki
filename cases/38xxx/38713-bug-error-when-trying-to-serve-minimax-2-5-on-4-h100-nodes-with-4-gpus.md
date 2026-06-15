# vllm-project/vllm#38713: [Bug]: Error when trying to serve MiniMax 2.5 on 4 H100 nodes with 4 GPUS

| 字段 | 值 |
| --- | --- |
| Issue | [#38713](https://github.com/vllm-project/vllm/issues/38713) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;fp8;kernel;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error when trying to serve MiniMax 2.5 on 4 H100 nodes with 4 GPUS

### Issue 正文摘录

### Your current environment Hi i am trying to serve Minimax on 4 H100 nodes with 4 Gpus per node. My singularity image is this: ```bash Bootstrap: docker From: vllm/vllm-openai:latest %post # 1) Install Ray for multi-node serving pip install --no-cache-dir "ray[default]" # 2) (Optional but recommended) install extra dependencies vLLM may need pip install --no-cache-dir \ aiohttp \ uvloop \ triton-kernels>=2.0.0 # 3) CUDA-aware tools # (optional) NVIDIA tools useful for serving & NCCL / Ray pip install --no-cache-dir \ psutil \ setproctitle # 4) Ensure vLLM latest pip install --upgrade --no-cache-dir vllm %labels Author YourName Version vLLM-MultiNode %runscript # Default entrypoint exec /bin/bash "$@" ``` And vllm version is 0.18. Could anyone help me with that ? ### 🐛 Describe the bug Here is my job: ```bash #!/bin/bash #SBATCH --job-name=VLLM-Ray #SBATCH --nodes=4 #SBATCH --ntasks-per-node=1 #SBATCH --gres=gpu:4 #SBATCH --cpus-per-task=96 #SBATCH --hint=nomultithread #SBATCH --time=00:15:00 #SBATCH --output=ray_vllm_%j.out #SBATCH --error=ray_vllm_%j.err #SBATCH --exclusive ############################################ # Global configuration #####################################...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: with 4 Gpus per node. My singularity image is this: ```bash Bootstrap: docker From: vllm/vllm-openai:latest %post # 1) Install Ray for multi-node serving pip install --no-cache-dir "ray[default]" # 2) (Optional but reco...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: PORT}" \ --num-gpus=4 \ --block & echo "Waiting for all 16 GPUs to join Ray..." while true; do gpu_count=$(singularity exec "${CONTAINER}" python3 -c "import ray; ray.init(address='auto'); print(int(ray.cluster_resource...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: pip install --no-cache-dir \ aiohttp \ uvloop \ triton-kernels>=2.0.0 # 3) CUDA-aware tools # (optional) NVIDIA tools useful for serving & NCCL / Ray pip install --no-cache-dir \ psutil \ setproctitle # 4) Ensure vLLM l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: IServer pid=88185) INFO 04-01 11:22:01 [model.py:1917] Downcasting torch.float32 to torch.bfloat16. (APIServer pid=88185) INFO 04-01 11:22:01 [model.py:1582] Using max model len 8192 (APIServer pid=88185) INFO 04-01 11:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: arity image is this: ```bash Bootstrap: docker From: vllm/vllm-openai:latest %post # 1) Install Ray for multi-node serving pip install --no-cache-dir "ray[default]" # 2) (Optional but recommended) install extra dependen...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
