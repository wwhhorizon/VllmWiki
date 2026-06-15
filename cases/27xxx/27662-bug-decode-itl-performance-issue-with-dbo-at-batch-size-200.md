# vllm-project/vllm#27662: [Bug]: Decode ITL performance issue with DBO at batch size ~200

| 字段 | 值 |
| --- | --- |
| Issue | [#27662](https://github.com/vllm-project/vllm/issues/27662) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Decode ITL performance issue with DBO at batch size ~200

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When analyzing the performance of Qwen3-235B-A22B-Instruct-2507-FP8 in a disaggregated setup with DeepEP backends, I noticed a significant outlier in ITL at load concurrency ~200-250. I was able to reproduce this with `vllm bench serve` directly against the decode worker, with 1 input token. With DBO enabled I see: **max-concurrency 225:** ``` ... ---------------Inter-token Latency---------------- Mean ITL (ms): 127.08 Median ITL (ms): 139.10 P99 ITL (ms): 157.00 ================================================== ``` **max-concurrency 300:** ``` ... ---------------Inter-token Latency---------------- Mean ITL (ms): 69.09 Median ITL (ms): 55.56 P99 ITL (ms): 151.23 ================================================== ``` With DBO disabled I see mean ITL of ~30 ms at batch size 225 and 300. Since DBO is meant to "overlap the sparse all-to-all communication in the MoE layer with the surrounding computation", it's not surprising that it doesn't improve performance in this case where decode is happening on a single node, but I was surprised by the significant negative performance impact at certain batch sizes. ### Before submitting a new...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Decode ITL performance issue with DBO at batch size ~200 bug;stale ### Your current environment ### 🐛 Describe the bug When analyzing the performance of Qwen3-235B-A22B-Instruct-2507-FP8 in a disaggregated setup...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: the bug When analyzing the performance of Qwen3-235B-A22B-Instruct-2507-FP8 in a disaggregated setup with DeepEP backends, I noticed a significant outlier in ITL at load concurrency ~200-250. I was able to reproduce thi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: f Qwen3-235B-A22B-Instruct-2507-FP8 in a disaggregated setup with DeepEP backends, I noticed a significant outlier in ITL at load concurrency ~200-250. I was able to reproduce this with `vllm bench serve` directly again...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
