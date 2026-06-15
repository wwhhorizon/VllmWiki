# vllm-project/vllm#36408: [Bug]: Qwen3.5-9B (BF16/AWQ) Illegal Memory Access in vLLM v0.17.0 (WSL2/RTX3090 Ti)

| 字段 | 值 |
| --- | --- |
| Issue | [#36408](https://github.com/vllm-project/vllm/issues/36408) |
| 状态 | open |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-9B (BF16/AWQ) Illegal Memory Access in vLLM v0.17.0 (WSL2/RTX3090 Ti)

### Issue 正文摘录

### Your current environment Environment - GPU: NVIDIA GeForce RTX 3090 Ti (24GB) - WSL2: Ubuntu 24.04.4 LTS - vLLM: 0.17.0 - PyTorch: 2.10.0 - CUDA: 12.8 (Driver 591.74) - Python: 3.12.3 ### 🐛 Describe the bug I am encountering a torch.AcceleratorError: CUDA error: an illegal memory access was encountered (cudaErrorIllegalAddress) when initializing the Qwen/Qwen3.5-9B-AWQ model on vLLM v0.17.0. Unlike previous reports suggesting this is limited to quantized models, I have confirmed that both Qwen/Qwen3.5-9B and cyankiwi/Qwen3.5-9B-AWQ-4bit models crash with the same error. python3 -m vllm.entrypoints.openai.api_server \ --model ./Qwen/Qwen3.5-9B-AWQ \ --port 8000 \ --max-model-len 8192 \ --gpu-memory-utilization 0.9 \ --quantization compressed-tensors \ --performance-mode throughput **Crash logs** : https://gist.github.com/d-etu/8f406bf8c994737024194f1453e2ae7b ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3.5-9B (BF16/AWQ) Illegal Memory Access in vLLM v0.17.0 (WSL2/RTX3090 Ti) bug ### Your current environment Environment - GPU: NVIDIA GeForce RTX 3090 Ti (24GB) - WSL2: Ubuntu 24.04.4 LTS - vLLM: 0.17.0 - PyTo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3.5-9B (BF16/AWQ) Illegal Memory Access in vLLM v0.17.0 (WSL2/RTX3090 Ti) bug ### Your current environment Environment - GPU: NVIDIA GeForce RTX 3090 Ti (24GB) - WSL2: Ubuntu 24.04.4 LTS - vLLM: 0.17.0 - PyTo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-9B (BF16/AWQ) Illegal Memory Access in vLLM v0.17.0 (WSL2/RTX3090 Ti) bug ### Your current environment Environment - GPU: NVIDIA GeForce RTX 3090 Ti (24GB) - WSL2: Ubuntu 24.04.4 LTS - vLLM: 0.17.0 - PyTo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ion 0.9 \ --quantization compressed-tensors \ --performance-mode throughput **Crash logs** : https://gist.github.com/d-etu/8f406bf8c994737024194f1453e2ae7b ### Before submitting a new issue... - [x] Make sure you alread...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ce model_support;quantization cuda;quantization crash;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
