# vllm-project/vllm#42390: [Bug]: Gemma-4 MoE Initialization Hang and Segfault

| 字段 | 值 |
| --- | --- |
| Issue | [#42390](https://github.com/vllm-project/vllm/issues/42390) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;hardware_porting;model_support;moe;multimodal_vlm;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;gemm;moe;quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-4 MoE Initialization Hang and Segfault

### Issue 正文摘录

### Your current environment **Environment**: vLLM Version: 0.20.x (or current latest) Model: google/gemma-4-26B-A4B-it Hardware: 2x NVIDIA GeForce RTX 3090 (24GB) Topology: PCIe Gen 4 (No NVLink) OS: Linux (Ubuntu 22.04/24.04) CUDA Version: 13.0 Python Version: 3.11+ ### 🐛 Describe the bug ### **Describe the bug** The `google/gemma-4-26B-A4B-it` (MoE) model fails to initialize in a Tensor Parallel (TP=2) configuration on Ampere hardware (RTX 3090). The failure occurs in two distinct stages: 1. **Configuration Error:** A `ValueError` is raised because the vision encoder produces 2,496 tokens, which exceeds the default `max_num_batched_tokens` of 2,048. 2. **Runtime Initialization Hang:** After resolving the token budget, the engine hangs during the "Wait for engine startup" phase. Logs indicate a `shm_broadcast.py` timeout: `No available shared memory broadcast block found in 60 seconds`. 3. **Segfault:** Attempting to terminate the hanging process leads to a Segfault in `libc_sigaction.c`, likely due to corrupted shared memory segments or leaked semaphore objects. ### **Steps to Reproduce** Attempt to serve the model on a dual-GPU system without NVLink using the following command...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: t latest) Model: google/gemma-4-26B-A4B-it Hardware: 2x NVIDIA GeForce RTX 3090 (24GB) Topology: PCIe Gen 4 (No NVLink) OS: Linux (Ubuntu 22.04/24.04) CUDA Version: 13.0 Python Version: 3.11+ ### 🐛 Describe the bug ###...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma-4 MoE Initialization Hang and Segfault bug ### Your current environment **Environment**: vLLM Version: 0.20.x (or current latest) Model: google/gemma-4-26B-A4B-it Hardware: 2x NVIDIA GeForce RTX 3090 (24GB)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ng and Segfault bug ### Your current environment **Environment**: vLLM Version: 0.20.x (or current latest) Model: google/gemma-4-26B-A4B-it Hardware: 2x NVIDIA GeForce RTX 3090 (24GB) Topology: PCIe Gen 4 (No NVLink) OS...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: m serve google/gemma-4-26B-A4B-it \ --tensor-parallel-size 2 \ --quantization fp8 \ --max-model-len 8192 \ --trust-remote-code ``` ### **Error Logs / Traceback** **Multimodal Budget Error:** ```text ValueError: Chunked...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: [Bug]: Gemma-4 MoE Initialization Hang and Segfault bug ### Your current environment **Environment**: vLLM Version: 0.20.x (or current latest) Model: google/gemma-4-26B-A4B-it Hardware: 2x NVIDIA GeForce RTX 3090 (24GB)...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
