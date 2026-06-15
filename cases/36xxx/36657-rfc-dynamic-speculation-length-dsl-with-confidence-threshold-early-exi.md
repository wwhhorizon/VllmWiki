# vllm-project/vllm#36657: [RFC]: Dynamic Speculation Length (DSL) with Confidence-Threshold Early Exit for vLLM Speculative Decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#36657](https://github.com/vllm-project/vllm/issues/36657) |
| 状态 | open |
| 标签 | RFC |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | attention |
| 症状 | slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Dynamic Speculation Length (DSL) with Confidence-Threshold Early Exit for vLLM Speculative Decoding

### Issue 正文摘录

### Motivation. Standard speculative decoding always runs the draft model for exactly `num_speculative_tokens` steps per decode iteration. When the draft model is uncertain early in the speculation chain, every additional step wastes compute: the low-confidence tokens are almost certainly rejected by the target model, and the draft forward passes are lost work. Setting `num_speculative_tokens` conservatively (e.g., 5) leaves throughput on the table during high-confidence sequences. Setting it aggressively (e.g., 20) wastes compute during low-confidence sequences. DSL resolves this tension by adapting the draft length at runtime, inspired by [DISCO (Mamou et al., 2024)](https://arxiv.org/abs/2405.04304). ### Proposed Change. **PR:** https://github.com/vllm-project/vllm/pull/35301 Add a `draft_confidence_threshold` field (default `0.0`, disabled) to `SpeculativeConfig`. When enabled, the `DraftModelProposer` evaluates a batch-level mean exit condition at each draft step $i$: $$\frac{1}{B} \sum_j \max_v \text{softmax}(z_{i,j}) < \tau$$ If the condition holds, drafting stops early and the tokens generated so far are returned. The output tensor is zero-padded to the full `num_speculati...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: c Speculation Length (DSL) with Confidence-Threshold Early Exit for vLLM Speculative Decoding RFC ### Motivation. Standard speculative decoding always runs the draft model for exactly `num_speculative_tokens` steps per...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: work. Setting `num_speculative_tokens` conservatively (e.g., 5) leaves throughput on the table during high-confidence sequences. Setting it aggressively (e.g., 20) wastes compute during low-confidence sequences. DSL res...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 0 \ --draft-confidence-threshold 0.6 ``` ### Benchmark highlights (1× A100 80 GB PCIe) | Model pair | Dataset | Config | vs. target | vs. SD/5 | |---|---|---|---|---| | Llama-3.1-8B + Llama-3.2-1B | mt-bench c=1 | DSL/2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: RFC ### Motivation. Standard speculative decoding always runs the draft model for exactly `num_speculative_tokens` steps per decode iteration. When the draft model is uncertain early in the speculation chain, every addi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: e minimum, so a single uncertain request in a mixed batch does not short-circuit drafting for the whole batch. - **No interface change**: `propose()` always returns shape `[batch_size, num_speculative_tokens]`. - **New...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
