# vllm-project/vllm#25122: [Bug]: vLLM worker shows high CPU usage even when not running inference

| 字段 | 值 |
| --- | --- |
| Issue | [#25122](https://github.com/vllm-project/vllm/issues/25122) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM worker shows high CPU usage even when not running inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Description When no inference requests are being processed, vllm worker continues to consume high CPU resources. This behavior is unexpected and suggests that the worker may be stuck in a busy loop or not idling properly. Steps to Reproduce 1. Start a vLLM worker normally. 2. Ensure no inference requests are running. 3. Observe system resource usage via top, htop, or similar monitoring tool. # Actual Behavior The worker process maintains abnormally high CPU utilization, even without active inference. # Evidence • Screenshot attached showing vllm worker process consuming significant CPU while idle. # Environment • vLLM version: 0.10.2 • Deployment setup: 4 GPUs • OS / Kernel: Rocky 9.6 • Python version: 3.12 • vllm options --enable-expert-parallel --tensor-parallel-size 4 --kv-cache-dtype fp8 ## Not observed in single-GPU environments; only occurs in multi-GPU setups. ![Image](https://github.com/user-attachments/assets/b489bc6b-59a3-4d6a-b7db-7e25d778bfff) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation pa...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: llel --tensor-parallel-size 4 --kv-cache-dtype fp8 ## Not observed in single-GPU environments; only occurs in multi-GPU setups. ![Image](https://github.com/user-attachments/assets/b489bc6b-59a3-4d6a-b7db-7e25d778bfff) #...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: the worker may be stuck in a busy loop or not idling properly. Steps to Reproduce 1. Start a vLLM worker normally. 2. Ensure no inference requests are running. 3. Observe system resource usage via top, htop, or similar...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ker process consuming significant CPU while idle. # Environment • vLLM version: 0.10.2 • Deployment setup: 4 GPUs • OS / Kernel: Rocky 9.6 • Python version: 3.12 • vllm options --enable-expert-parallel --tensor-parallel...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ff) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: pert-parallel --tensor-parallel-size 4 --kv-cache-dtype fp8 ## Not observed in single-GPU environments; only occurs in multi-GPU setups. ![Image](https://github.com/user-attachments/assets/b489bc6b-59a3-4d6a-b7db-7e25d7...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
