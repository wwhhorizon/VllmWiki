# vllm-project/vllm#24958: [Fatal Bug]: occasionally exhibits a "long output state" phenomenon (not repetitive output)

| 字段 | 值 |
| --- | --- |
| Issue | [#24958](https://github.com/vllm-project/vllm/issues/24958) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Fatal Bug]: occasionally exhibits a "long output state" phenomenon (not repetitive output)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When VLLM performs inference on certain models, it occasionally exhibits a "long output state" phenomenon (not repetitive output). The specific characteristics are as follows: 1. VLLM causes multiple requests to simultaneously enter a long output state, rather than a single request getting stuck. (In actual repetitive output scenarios, typically only one or two requests in a batch get stuck occasionally) This continues until the request's context reaches the maximum context limit. 2. This situation occurs sporadically. The same batch of requests usually has difficulty triggering this bug, and the same prompts do not exhibit this issue when accessed at another time. 3. Although the model is in a long output state, no actual long outputs are observed in the model's real output. (This is the most fundamental difference from model repetitive output) 4. For individual requests, processing time lasts several minutes, and the long output state causes massive KV-CACHE consumption, leading to decreased parallelism and increased latency. 5. When VLLM receives a large number of requests (dozens) within a short time frame (1s), these request...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hibits a "long output state" phenomenon (not repetitive output). The specific characteristics are as follows: 1. VLLM causes multiple requests to simultaneously enter a long output state, rather than a single request ge...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: state causes massive KV-CACHE consumption, leading to decreased parallelism and increased latency. 5. When VLLM receives a large number of requests (dozens) within a short time frame (1s), these requests in the long out...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ive KV-CACHE consumption, leading to decreased parallelism and increased latency. 5. When VLLM receives a large number of requests (dozens) within a short time frame (1s), these requests in the long output state can be...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ing time lasts several minutes, and the long output state causes massive KV-CACHE consumption, leading to decreased parallelism and increased latency. 5. When VLLM receives a large number of requests (dozens) within a s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ment ### 🐛 Describe the bug When VLLM performs inference on certain models, it occasionally exhibits a "long output state" phenomenon (not repetitive output). The specific characteristics are as follows: 1. VLLM causes...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
