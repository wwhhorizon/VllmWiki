# vllm-project/vllm#19575: [Bug]: Extremely Low Throughput for google/gemma-3-1b-it with vLLM (Only ~80 tokens/sec)

| 字段 | 值 |
| --- | --- |
| Issue | [#19575](https://github.com/vllm-project/vllm/issues/19575) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;fp8 |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Extremely Low Throughput for google/gemma-3-1b-it with vLLM (Only ~80 tokens/sec)

### Issue 正文摘录

### Your current environment # Low Throughput Issue with `google/gemma-3-1b-it` on vLLM ## Issue Description We're observing **significantly low throughput** when serving the `google/gemma-3-1b-it` model using **vLLM** with the OpenAI-compatible API interface. Despite using capable hardware and optimal settings, the model underperforms with throughput far below expectations. --- ## Environment | Component | Specification | |---------------------|----------------------------------------------| | **Model** | `google/gemma-3-1b-it` | | **vLLM Image** | `vllm/vllm-openai:latest` | | **Deployment** | Docker + NVIDIA runtime | | **GPU** | 1x NVIDIA L40S (45GB VRAM) | | **CPU** | AMD EPYC 9655 (192 cores total) | | **CUDA Version** | 12.8 | | **Driver Version** | 570.86.10 | | **Python** | 3.12.3 | --- ## Docker Command ```yaml command: [ "--model", "google/gemma-3-1b-it", "--dtype", "float16", "--kv-cache-dtype", "fp8", "--max-model-len", "2048", "--tensor-parallel-size", "1", "--gpu-memory-utilization", "0.9", "--tokenizer-mode", "auto" ] ``` --- ### Describe the bug ## Benchmark Results **Benchmark Tool**: [`vllm-benchmark`](https://github.com/backprop-ai/vllm-benchmark) **Command Use...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: far below expectations. --- ## Environment | Component | Specification | |---------------------|----------------------------------------------| | **Model** | `google/gemma-3-1b-it` | | **vLLM Image** | `vllm/vllm
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: er Command ```yaml command: [ "--model", "google/gemma-3-1b-it", "--dtype", "float16", "--kv-cache-dtype", "fp8", "--max-model-len", "2048", "--tensor-parallel-size", "1", "--gpu-memory-utilization", "0.9", "--tokenizer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Extremely Low Throughput for google/gemma-3-1b-it with vLLM (Only ~80 tokens/sec) bug;stale ### Your current environment # Low Throughput Issue with `google/gemma-3-1b-it` on vLLM ## Issue Description We're obser...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Extremely Low Throughput for google/gemma-3-1b-it with vLLM (Only ~80 tokens/sec) bug;stale ### Your current environment # Low Throughput Issue with `google/gemma-3-1b-it` on vLLM ## Issue Description We're obser...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: **CPU** | AMD EPYC 9655 (192 cores total) | | **CUDA Version** | 12.8 | | **Driver Version** | 570.86.10 | | **Python** | 3.12.3 | --- ## D

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
