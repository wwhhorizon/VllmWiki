# vllm-project/vllm#25915: [Performance]: Limited improvements when compared Qwen3 / Qwen3-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#25915](https://github.com/vllm-project/vllm/issues/25915) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | fp8;kernel |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Limited improvements when compared Qwen3 / Qwen3-FP8

### Issue 正文摘录

### Proposal to improve performance On the latest `vllm/vllm-openai:v0.8.5` with h100 hardware ### Report of performance regression `vllm bench throughput --model Qwen/Qwen3-8B --input-len 1024 --output-len 2048` bf16 **2375.11 toks/s, output: 4481.69 toks/s** `vllm bench throughput --model Qwen/Qwen3-8B-FP8 --input-len 1024 --output-len 2048` fp8 **speed input: 2783.16 toks/s, output: 4868.31 toks/s** ### Misc discussion on performance ## vllm/vllm-openai:v0.10.2 `CUDA_VISIBLE_DEVICES=0 vllm bench throughput --model Qwen/Qwen3-8B --input-len 1024 --output-len 2048` bf16 **speed input: 2697.18 toks/s, output: 5408.88 toks/s** `CUDA_VISIBLE_DEVICES=7 vllm bench throughput --model Qwen/Qwen3-8B-FP8 --input-len 1024 --output-len 2048` fp8 **speed input: 2794.50 toks/s, output: 5304.03 toks/s** ### Your current environment (if you think it is necessary) usually fp8 kernels should brings 1.4 to 1.7x improvements when single-user serving case and also have 1.2 to 1.4x improvement when dealing batched queries. But in the vllm benchmark I did not observe such a improvement ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Performance]: Limited improvements when compared Qwen3 / Qwen3-FP8 performance;stale ### Proposal to improve performance On the latest `vllm/vllm-openai:v0.8.5` with h100 hardware ### Report of performance regression `...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: wen3-FP8 performance;stale ### Proposal to improve performance On the latest `vllm/vllm-openai:v0.8.5` with h100 hardware ### Report of performance regression `vllm bench throughput --model Qwen/Qwen3-8B --input-len 102...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: sal to improve performance On the latest `vllm/vllm-openai:v0.8.5` with h100 hardware ### Report of performance regression `vllm bench throughput --model Qwen/Qwen3-8B --input-len 1024 --output-len 2048` bf16 **2375.11...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Limited improvements when compared Qwen3 / Qwen3-FP8 performance;stale ### Proposal to improve performance On the latest `vllm/vllm-openai:v0.8.5` with h100 hardware ### Report of performance regression `...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: mance]: Limited improvements when compared Qwen3 / Qwen3-FP8 performance;stale ### Proposal to improve performance On the latest `vllm/vllm-openai:v0.8.5` with h100 hardware ### Report of performance regression `vllm be...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
