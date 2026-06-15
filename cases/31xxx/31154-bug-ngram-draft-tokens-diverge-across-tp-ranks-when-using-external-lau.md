# vllm-project/vllm#31154: [Bug]:  Ngram draft tokens diverge across TP ranks when using external_launcher.

| 字段 | 值 |
| --- | --- |
| Issue | [#31154](https://github.com/vllm-project/vllm/issues/31154) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Ngram draft tokens diverge across TP ranks when using external_launcher.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using **external launcher + tensor parallel + n-gram speculative decoding**, I occasionally observe that the proposed draft tokens differ across tensor-parallel (TP) ranks with a very low probability. The initial symptom is that vLLM hangs due to an NCCL operation getting stuck. After locating the bug and manually printing `draft_token_ids` on different TP ranks, I found that the root cause is that the draft tokens diverge across TP ranks. This leads to different `num_tokens` values on each rank, which then causes the NCCL collective to hang. This behavior is surprising, because the random seed is explicitly set to be the same across all TP ranks. Nonetheless, the issue does occur, though with very low frequency. My current guess is that some part of the rejection sampling or draft proposing logic is non-deterministic. Anyway, as a temporary fix, I broadcast the draft_token_ids from the first rank: ```python def propose_ngram_draft_token_ids( self, sampled_token_ids: list[list[int]], ) -> list[list[int]]: # TODO(woosuk): Optimize. tp_group = get_tp_group() if tp_group.is_first_rank: draft_token_ids = xxx # original logic els...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Ngram draft tokens diverge across TP ranks when using external_launcher. bug;stale ### Your current environment ### 🐛 Describe the bug When using **external launcher + tensor parallel + n-gram speculative decodin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: is that some part of the rejection sampling or draft proposing logic is non-deterministic. Anyway, as a temporary fix, I broadcast the draft_token_ids from the first rank: ```python def propose_ngram_draft_token_ids( se...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: that some part of the rejection sampling or draft proposing logic is non-deterministic. Anyway, as a temporary fix, I broadcast the draft_token_ids from the first rank: ```python def propose_ngram_draft_token_ids( self,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e to hang. This behavior is surprising, because the random seed is explicitly set to be the same across all TP ranks. Nonetheless, the issue does occur, though with very low frequency. My current guess is that some part...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
