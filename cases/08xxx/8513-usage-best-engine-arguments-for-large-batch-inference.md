# vllm-project/vllm#8513: [Usage]: Best engine arguments for large batch inference

| 字段 | 值 |
| --- | --- |
| Issue | [#8513](https://github.com/vllm-project/vllm/issues/8513) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | fp8 |
| 症状 | slowdown |
| 根因提示 | dtype;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Best engine arguments for large batch inference

### Issue 正文摘录

### Your current environment irrelevant ### How would you like to use vllm What would be the arguments that would maximize overall throughput for large batch offline inference? More specifically, I'm looking to generate 405B FP8 outputs for millions of inputs with 8x80 H100 SXM. Thus far, I've been using the following arguments, but I womder if there are any others that would optimize this usecase, where per-request throughput and TTFT don't matter? ```bash --max-model-len 8192 \ --disable-log-requests \ --gpu_memory_utilization 0.93 \ --use-v2-block-manager \ --block-size 32 \ --max-num-seqs 512 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: batch offline inference? More specifically, I'm looking to generate 405B FP8 outputs for millions of inputs with 8x80 H100 SXM. Thus far, I've been using the following arguments, but I womder if there are any others tha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Usage]: Best engine arguments for large batch inference usage;stale ### Your current environment irrelevant ### How would you like to use vllm What would be the arguments that would maximize overall throughput for larg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 'm looking to generate 405B FP8 outputs for millions of inputs with 8x80 H100 SXM. Thus far, I've been using the following arguments, but I womder if there are any others that would optimize this usecase, where per-requ...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: -disable-log-requests \ --gpu_memory_utilization 0.93 \ --use-v2-block-manager \ --block-size 32 \ --max-num-seqs 512 ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, an...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ike to use vllm What would be the arguments that would maximize overall throughput for large batch offline inference? More specifically, I'm looking to generate 405B FP8 outputs for millions of inputs with 8x80 H100 SXM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
