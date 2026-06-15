# vllm-project/vllm#38194: [Performance]: Prefix cache hit lower on vLLM than on other inference stacks

| 字段 | 值 |
| --- | --- |
| Issue | [#38194](https://github.com/vllm-project/vllm/issues/38194) |
| 状态 | open |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Prefix cache hit lower on vLLM than on other inference stacks

### Issue 正文摘录

### Report of performance regression hi our prefix cache metric is only 60-80% on vLLM running DeepSeek v3.2 but is 95% consistently with DeepSeek API. There might be a problem with prefix caching? our workload is multi-turn conversation in an AI character app at high concurrency ### Your current environment (if you think it is necessary) ```text VLLM_USE_FLASHINFER_MOE_FP4=1 \ vllm serve nvidia/DeepSeek-V3.2-NVFP4 \ --tensor-parallel-size 8 \ --quantization modelopt_fp4 \ --host 0.0.0.0 \ --port 30000 \ --max-model-len 32768 \ --enable-prefix-caching ``` [env_info.txt](https://github.com/user-attachments/files/26261872/env_info.txt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ironment (if you think it is necessary) ```text VLLM_USE_FLASHINFER_MOE_FP4=1 \ vllm serve nvidia/DeepSeek-V3.2-NVFP4 \ --tensor-parallel-size 8 \ --quantization modelopt_fp4 \ --host 0.0.0.0 \ --port 30000 \ --max-mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: LLM than on other inference stacks performance ### Report of performance regression hi our prefix cache metric is only 60-80% on vLLM running DeepSeek v3.2 but is 95% consistently with DeepSeek API. There might be a pro...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: our current environment (if you think it is necessary) ```text VLLM_USE_FLASHINFER_MOE_FP4=1 \ vllm serve nvidia/DeepSeek-V3.2-NVFP4 \ --tensor-parallel-size 8 \ --quantization modelopt_fp4 \ --host 0.0.0.0 \ --port 300...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Performance]: Prefix cache hit lower on vLLM than on other inference stacks performance ### Report of performance regression hi our prefix cache metric is only 60-80% on vLLM running DeepSeek v3.2 but is 95% consistent...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: xt) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
