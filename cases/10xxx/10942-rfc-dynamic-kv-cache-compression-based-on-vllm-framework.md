# vllm-project/vllm#10942: [RFC]: Dynamic KV Cache compression based on  vLLM framework

| 字段 | 值 |
| --- | --- |
| Issue | [#10942](https://github.com/vllm-project/vllm/issues/10942) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;model_support;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | attention;cache;cuda;kernel |
| 症状 | slowdown |
| 根因提示 | memory_layout;race_condition;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Dynamic KV Cache compression based on  vLLM framework

### Issue 正文摘录

### Motivation. # KV Sparsity and Model Compression By reviewing recent academic papers from the past year in the field of KV sparsity (H2O, SnapKV, PyramidKV), we apply KV sparsity to different layers of the model. By employing a pruning strategy, we eliminate KV pairs with lower scores while retaining those with higher scores and closer proximity. This approach reduces memory usage, as well as computational and I/O overhead, ultimately leading to accelerated inference. ## Experiments ### Baselines and Settings We run all KV-Compress experiments using our vLLM integration forked from v0.6.2, running in CUDA graph mode with a block size of 16. For all RTX 4090 / Llama-3.1-8B-Instruct experiments, we use the default GPU memory utilization of 0.9 and set the `maxmodel-length` to 32k. We evaluate our compression on Llama-3.1-8B-Instruct, comparing performance against the following baseline methods introduced in prior work: - vLLM-0.6.2 - Novita AI, Pyramid KV Cache compression based on vLLM framework ### MMLU Pro and LongBench We control different KV Cache compression ratios by setting different sliding window lengths on different layers. In the experiment, we mainly set three differ...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: GPU memory utilization of 0.9 and set the `maxmodel-length` to 32k. We evaluate our compression on Llama-3.1-8B-Instruct, comparing performance against the following baseline methods introduced in prior work: - vLLM-0.6...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 45-84a043ea36ef) ### Proposed Change. Modified files mainly include： - Flash attention, sparse scoring based on Flash attention while ensuring that kernel performance loss is less than 1%. - Paged attention and reshape_...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ss experiments using our vLLM integration forked from v0.6.2, running in CUDA graph mode with a block size of 16. For all RTX 4090 / Llama-3.1-8B-Instruct experiments, we use the default GPU memory utilization of 0.9 an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [RFC]: Dynamic KV Cache compression based on vLLM framework RFC;stale ### Motivation. # KV Sparsity and Model Compression By reviewing recent academic papers from the past year in the field of KV sparsity (H2O, SnapKV,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: on based on vLLM framework RFC;stale ### Motivation. # KV Sparsity and Model Compression By reviewing recent academic papers from the past year in the field of KV sparsity (H2O, SnapKV, PyramidKV), we apply KV sparsity...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
