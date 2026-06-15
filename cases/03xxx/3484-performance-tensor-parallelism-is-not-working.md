# vllm-project/vllm#3484: [Performance]: tensor parallelism is not working

| 字段 | 值 |
| --- | --- |
| Issue | [#3484](https://github.com/vllm-project/vllm/issues/3484) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: tensor parallelism is not working

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression When I use vllm to run Llama-chat-7b-hf without tensor_parallel, one A100 is almost fully occupied. However, when I use vllm to run Llama-chat-7b-hf with `tensor-parallel-size=2`, two A100s are almost fully occupied. It seems the tensor parallelism is not working at all. ### **No tensor parallelism** ``` python -m vllm.entrypoints.openai.api_server --model Llama-2-7b-chat-hf ``` ``` +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA A100 80GB PCIe On | 00000000:23:00.0 Off | 0 | | N/A 47C P0 74W / 250W | 73393MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+----------------------+----------------------+ | 1 NVID...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ----------------------------+ | NVIDIA-SMI 535.104.05 Driver Version: 535.104.05 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M |...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Performance]: tensor parallelism is not working performance ### Proposal to improve performance _No response_ ### Report of performance regression When I use vllm to run Llama-chat-7b-hf without tensor_parallel, one A1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: response_ ### Report of performance regression When I use vllm to run Llama-chat-7b-hf without tensor_parallel, one A100 is almost fully occupied. However, when I use vllm to run Llama-chat-7b-hf with `tensor-parallel-s...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| +--------------------------
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: roposal to improve performance _No response_ ### Report of performance regression When I use vllm to run Llama-chat-7b-hf without tensor_parallel, one A100 is almost fully occupied. However, when I use vllm to run Llama...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
