# vllm-project/vllm#16394: [Bug]: AMD Instinct MI210 + vllm fail to run the official deepseek-r1 model: ValueError("type fp8e4b8 not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)")

| 字段 | 值 |
| --- | --- |
| Issue | [#16394](https://github.com/vllm-project/vllm/issues/16394) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AMD Instinct MI210 + vllm fail to run the official deepseek-r1 model: ValueError("type fp8e4b8 not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)")

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the deepseek-r1 model on two node with docker+vllm+ray with each node having 8 AMD MI210 gpu cards. My commands are: 1. Start a ray cluster on head node: `bash run_cluster2.sh vllm-dsr1:v1 $my_ip_head --head /root -e VLLM_HOST_IP=$my_ip_head --privileged -e NCCL_IB_HCA=mlx5 -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 -e NCCL_P2P_DISABLE=1` 2. Join the ray cluster on worker node: `bash run_cluster2.sh vllm-dsr1:v1 $my_ip_head --worker /root -e VLLM_HOST_IP=$my_ip_worker --privileged -e NCCL_IB_HCA=mlx5 -e CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7 -e NCCL_P2P_DISABLE=1` 3. Enter the container via either node: `docker exec -it node2 /bin/bash` 4. Run deepseek-r1 model: `python -m vllm.entrypoints.openai.api_server --model /models/DeepSeek-R1 --tensor-parallel-size 8 --port 1001 --enforce_eager --distributed-executor-backend ray --pipeline-parallel-size 2 --max-model-len 1024 --max-num-batched-tokens 1024 --trust-remote-code --enable-prefix-caching` After loading all the 163 .safetensors models, it raises the error: `ValueError("type fp8e4b8 not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)")`. How to solve thi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: AMD Instinct MI210 + vllm fail to run the official deepseek-r1 model: ValueError("type fp8e4b8 not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)") bug;stale ### Your current environment...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: I210 + vllm fail to run the official deepseek-r1 model: ValueError("type fp8e4b8 not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)") bug;stale ### Your current environment ### 🐛 Describe the bu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ensor-parallel-size 8 --port 1001 --enforce_eager --distributed-executor-backend ray --pipeline-parallel-size 2 --max-model-len 1024 --max-num-batched-tokens 1024 --trust-remote-code --enable-prefix-caching` After loadi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ficial deepseek-r1 model: ValueError("type fp8e4b8 not supported in this architecture. The supported fp8 dtypes are ('fp8e5',)") bug;stale ### Your current environment ### 🐛 Describe the bug I run the deepseek-r1 model...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: rted in this architecture. The supported fp8 dtypes are ('fp8e5',)") bug;stale ### Your current environment ### 🐛 Describe the bug I run the deepseek-r1 model on two node with docker+vllm+ray with each node having 8 AMD...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
