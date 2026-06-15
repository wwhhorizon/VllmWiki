# vllm-project/vllm#31913: [Bug]: test_eagle_dp test is flaky

| 字段 | 值 |
| --- | --- |
| Issue | [#31913](https://github.com/vllm-project/vllm/issues/31913) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: test_eagle_dp test is flaky

### Issue 正文摘录

### Your current environment main ### 🐛 Describe the bug See https://github.com/pytorch/pytorch/issues/170563 for previous discussion. Repro: `TP_SIZE=2 DP_SIZE=2 pytest tests/v1/distributed/test_eagle_dp.py::test_run_eagle_dp` (you may need to adjust the number of tokens to something high, like 600+). For pytorch 2.9 I had to adjust to 600; for PyTorch 2.10 adjusting to 50 will cause a failure. The test is testing that a model that uses spec decoding produces identical tokens compared to a model without spec decoding at temperature=0 (greedy sampling). For this property to hold, we need batch invariance in vLLM. This is because the way spec decoding works is that the drafter produces a sequence of tokens [a, b', c', d', e'] and then the target model does a forward pass with all of the tokens and verifies that the token after `a` is actually `b'`, the token after `b'` is actually `c'`, and so on. Compare this to the model that doesn't use spec decoding: it does each model forward pass with just one single token instead of a batch of tokens in the usual autoregressive sense. My hypothesis is that something is either wrong with batch invariance (we turned on batch invariant mode for...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: at temperature=0 (greedy sampling). For this property to hold, we need batch invariance in vLLM. This is because the way spec decoding works is that the drafter produces a sequence of tokens [a, b', c', d', e'] and then...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rong with how our spec decoding is implemented that leads to nondeterminism. This can probably be tracked down by sitting down and trying to figure out exactly when the tensors diverge bitwise. cc @bwasti @PaulZhang12 @...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: iance (we turned on batch invariant mode for this test) or something is else wrong with how our spec decoding is implemented that leads to nondeterminism. This can probably be tracked down by sitting down and trying to...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: h 2.10 adjusting to 50 will cause a failure. The test is testing that a model that uses spec decoding produces identical tokens compared to a model without spec decoding at temperature=0 (greedy sampling). For this prop...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ariance in vLLM. This is because the way spec decoding works is that the drafter produces a sequence of tokens [a, b', c', d', e'] and then the target model does a forward pass with all of the tokens and verifies that t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
