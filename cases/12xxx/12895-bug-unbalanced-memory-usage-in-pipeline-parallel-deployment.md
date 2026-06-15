# vllm-project/vllm#12895: [Bug]: Unbalanced Memory Usage in Pipeline Parallel Deployment

| 字段 | 值 |
| --- | --- |
| Issue | [#12895](https://github.com/vllm-project/vllm/issues/12895) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;model_support;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unbalanced Memory Usage in Pipeline Parallel Deployment

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm deploying DeepSeek-R1 on a Ray cluster consisting of 3 nodes with 8x A100 GPUs each, using the command: ```bash vllm serve /models/unsloth-DeepSeek-R1-BF16/ -pp 3 -tp 8 --trust-remote-code --max-model-len 4096 --worker-use-ray --swap-space 16 --gpu-memory-utilization 0.95 ``` I've observed a significant memory imbalance issue in the pipeline parallel deployment: The last node in the Ray cluster consistently consumes more GPU memory for model preloading than other nodes. After the cluster serves requests for a period of time, the vLLM Ray worker terminates when the last node runs out of memory, while other nodes' GPU memory remains underutilized. - The last node in the Ray cluster consistently uses more GPU memory than other nodes - Model layer partitioning appears to be uneven across pipeline stages - The last node quickly runs out of memory due to KV-cache allocation during continuous inference requests - Other nodes still have available GPU memory when the last node is exhausted Below is the GPU memory usage across nodes after service initialization, which clearly shows the uneven memory preallocation: ```bash (base) root@s...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 550.120 Driver Version: 550.120 CUDA Version: 12.4 | |-----------------------------------------+------------------------+----------------------+ | GPU Name Persistence-M | Bus-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: I'm deploying DeepSeek-R1 on a Ray cluster consisting of 3 nodes with 8x A100 GPUs each, using the command: ```bash vllm serve /models/unsloth-DeepSeek-R1-BF16/ -pp 3 -tp 8 --trust-remote-code --max-model-len 4096 --wor...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 3: deployment: The last node in the Ray cluster consistently consumes more GPU memory for model preloading than other nodes. After the cluster serves requests for a period of time, the vLLM Ray worker terminates when the l...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: each, using the command: ```bash vllm serve /models/unsloth-DeepSeek-R1-BF16/ -pp 3 -tp 8 --trust-remote-code --max-model-len 4096 --worker-use-ray --swap-space 16 --gpu-memory-utilization 0.95 ``` I've observed a signi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: f 3 nodes with 8x A100 GPUs each, using the command: ```bash vllm serve /models/unsloth-DeepSeek-R1-BF16/ -pp 3 -tp 8 --trust-remote-code --max-model-len 4096 --worker-use-ray --swap-space 16 --gpu-memory-utilization 0....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
