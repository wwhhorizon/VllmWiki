# vllm-project/vllm#18055: [Bug]: Accuracy degradation in vLLM when prefix‑cache is enabled for recomputation workloads

| 字段 | 值 |
| --- | --- |
| Issue | [#18055](https://github.com/vllm-project/vllm/issues/18055) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Accuracy degradation in vLLM when prefix‑cache is enabled for recomputation workloads

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug In vLLM, enabling the prefix‑cache feature in scenarios that trigger recomputation consistently leads to accuracy degradation on GPUs, and the same drops in model accuracy is observed when running the vllm‑ascend fork on NPUs. On GPUs, I launched the vLLM service with the following script, which does not trigger recomputation in this configuration: ```python python -m vllm.entrypoints.openai.api_server \ --model=/path/to/QwQ-32B \ --trust-remote-code \ --max-model-len 8192 \ -tp 2 \ --port 8006 \ --block-size 128 \ --enable-prefix-caching ``` By contrast, On GPUs, I launched the vLLM service with the following script, which does trigger recomputation by lowering GPU memory utilization to 0.5: ```python python -m vllm.entrypoints.openai.api_server \ --model=/path/to/QwQ-32B \ --trust-remote-code \ --max-model-len 8192 \ -tp 2 \ --port 8006 \ --block-size 128 \ --enable-prefix-caching \ --gpu-memory-utilization 0.5 ``` With SamplingParams = {"max_tokens": 3072, "temperature": 0}, I measured accuracy on the GSM8K dataset: No recomputation path → 77.79 %, essentially matching the out‑of‑the‑box baseline of 78.39 %. Recomputation path...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ms = {"max_tokens": 3072, "temperature": 0}, I measured accuracy on the GSM8K dataset: No recomputation path → 77.79 %, essentially matching the out‑of‑the‑box baseline of 78.39 %. Recomputation path → 60.12 %, nearly 2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: onsistently leads to accuracy degradation on GPUs, and the same drops in model accuracy is observed when running the vllm‑ascend fork on NPUs. On GPUs, I launched the vLLM service with the following script, which does n...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ion in vLLM when prefix‑cache is enabled for recomputation workloads bug;stale ### Your current environment ### 🐛 Describe the bug In vLLM, enabling the prefix‑cache feature in scenarios that trigger recomputation consi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: Accuracy degradation in vLLM when prefix‑cache is enabled for recomputation workloads bug;stale ### Your current environment ### 🐛 Describe the bug In vLLM, enabling the prefix‑cache feature in scenarios that tri...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Accuracy degradation in vLLM when prefix‑cache is enabled for recomputation workloads bug;stale ### Your current environment ### 🐛 Describe the bug In vLLM, enabling the prefix‑cache feature in scenarios that tri...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
