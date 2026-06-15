# vllm-project/vllm#28667: [Bug]: Poor Performance: ~40 t/s for Qwen3-80B-AWQ on Single RTX 6000

| 字段 | 值 |
| --- | --- |
| Issue | [#28667](https://github.com/vllm-project/vllm/issues/28667) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | kernel;moe;quantization |
| 症状 | slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Poor Performance: ~40 t/s for Qwen3-80B-AWQ on Single RTX 6000

### Issue 正文摘录

### Your current environment ## 🚀 Low generation throughput (\~40 tokens/s) for Qwen3-Next-80B-A3B-Instruct-AWQ-4bit (MoE) on a single GPU ### Describe the Issue I am observing unexpectedly low generation throughput when running the **Qwen3-Next-80B-A3B-Instruct-AWQ-4bit** model (an AWQ-quantized Mixture of Experts architecture) on a single, high-end NVIDIA GPU. The throughput is significantly lower than anticipated for this type of hardware and optimization. ### Environment Details * **Model:** `cpatonn/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit` (80B MoE, AWQ-4bit quantized) * **Hardware (Single GPU used):** NVIDIA RTX Pro 6000 Blackwell (96GB VRAM) * **vLLM Image:** `vllm/vllm-openai:latest` (or specify your actual vLLM version if known) * **Tensor Parallelism:** `TP=1` (Single GPU) ### Steps to Reproduce 1. **Launch the vLLM Server** using the following Docker command (targeting a single GPU): ```bash docker run -d --name vllm-qwen-80b \ --gpus '"device=2"' --ipc=host \ -p 6000:6000 \ -v ./hf_hub/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit:/models:ro \ vllm/vllm-openai:latest \ --model /models \ --served-model-name Qwen3-Next-80B-A3B-Instruct-AWQ-4bit \ --tensor-parallel-size 1 \ --max-mod...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: le, high-end NVIDIA GPU. The throughput is significantly lower than anticipated for this type of hardware and optimization. ### Environment Details * **Model:** `cpatonn/Qwen3-Next-80B-A3B-Instruct-AWQ-4bit` (80B MoE, A...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Poor Performance: ~40 t/s for Qwen3-80B-AWQ on Single RTX 6000 bug;stale ### Your current environment ## 🚀 Low generation throughput (\~40 tokens/s) for Qwen3-Next-80B-A3B-Instruct-AWQ-4bit (MoE) on a single GPU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Poor Performance: ~40 t/s for Qwen3-80B-AWQ on Single RTX 6000 bug;stale ### Your current environment ## 🚀 Low generation throughput (\~40 tokens/s) for Qwen3-Next-80B-A3B-Instruct-AWQ-4bit (MoE) on a single GPU...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: ion throughput (\~40 tokens/s) for Qwen3-Next-80B-A3B-Instruct-AWQ-4bit (MoE) on a single GPU ### Describe the Issue I am observing unexpectedly low generation throughput when running the **Qwen3-Next-80B-A3B-Instruct-A...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Bug]: Poor Performance: ~40 t/s for Qwen3-80B-AWQ on Single RTX 6000 bug;stale ### Your current environment ## 🚀 Low generation throughput (\~40 tokens/s) for Qwen3-Next-80B-A3B-Instruct-AWQ-4bit (MoE) on a single GPU #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
