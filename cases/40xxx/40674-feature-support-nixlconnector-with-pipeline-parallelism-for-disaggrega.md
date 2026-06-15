# vllm-project/vllm#40674: [Feature]:  Support NixlConnector with Pipeline Parallelism for disaggregated serving

| 字段 | 值 |
| --- | --- |
| Issue | [#40674](https://github.com/vllm-project/vllm/issues/40674) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]:  Support NixlConnector with Pipeline Parallelism for disaggregated serving

### Issue 正文摘录

### 🚀 The feature, motivation and pitch On the prefill side of high-throughput long-context disaggregated serving, Pipeline Parallelism (PP) is an important scaling axis: it compresses the prefill pool (fewer prefill GPUs feeding the same number of decode GPUs) and, when combined with chunked-pipeline techniques, helps hide the long-context attention bubble. today this path is blocked in vLLM because **`NixlConnector` does not support `pipeline-parallel-size > 1`**. Any disaggregated deployment that wants PP on the prefill workers cannot use vLLM's KV-transfer layer. This forces us (and other users building long-context / disagg stacks) to either: - drop PP on prefill entire (losing the prefill-pool compression benefit), or - fork or patch `NixlConnector` internally, which is not sustainable. Reference comparison: SGLang already supports PP + NIXL in disaggregated mode and reports sizable long-context prefill gains from PP when combined with their chunked-PP path ([SGLang blog, 2026-01-15](https://www.lmsys.org/blog/2026-01-15-chunked-pipeline/)). vLLM currently has no equivalent path. ### Alternatives ### Proposed feature Add first-class support for `NixlConnector` when `pipeline...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ixlConnector with Pipeline Parallelism for disaggregated serving feature request ### 🚀 The feature, motivation and pitch On the prefill side of high-throughput long-context disaggregated serving, Pipeline Parallelism (P...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Feature]: Support NixlConnector with Pipeline Parallelism for disaggregated serving feature request ### 🚀 The feature, motivation and pitch On the prefill side of high-throughput long-context disaggregated serving, Pip...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: hput long-context disaggregated serving, Pipeline Parallelism (PP) is an important scaling axis: it compresses the prefill pool (fewer prefill GPUs feeding the same number of decode GPUs) and, when combined with chunked...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: est ### 🚀 The feature, motivation and pitch On the prefill side of high-throughput long-context disaggregated serving, Pipeline Parallelism (PP) is an important scaling axis: it compresses the prefill pool (fewer prefil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ation with TP and DP/EP on both ends ### context - Model: DeepSeek-R1 (FP4) on Blackwell (GB300), 128K/8K, disaggregated serving. - Goal: shrink the prefill pool via PP on prefill workers while keeping decode on TP/DP+E...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
