# vllm-project/vllm#37285: [Bug]: PD disaggregation for SSM models requires `--no-async-scheduling` when TP>1

| 字段 | 值 |
| --- | --- |
| Issue | [#37285](https://github.com/vllm-project/vllm/issues/37285) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: PD disaggregation for SSM models requires `--no-async-scheduling` when TP>1

### Issue 正文摘录

### Your current environment latest main ### 🐛 Describe the bug As reported in https://github.com/vllm-project/vllm/pull/36687/, PD for SSM models (eg NemotronH, Qwen3.5..) with TP > 1 currently requires `--no-async-scheduling` to run without accuracy drops. @ZhanqiuHu and I identified a synchronization issue where states may be transferred in a corrupted form, leading to high variance in evaluations. Current diagnostics: - DTP1-PTP1 works great (also tested with --distributed-executor-backend=mp ) - DTP2-PTP2 accuracy jitters a lot - higher TP eg TP4 appear to jitter more - DTP2-PTP2 --no-async-scheduling works great - adding a `torch.synchronize` call after model execution in the runner also works, so my current guess is that we're moving bytes that haven't had their content fully written to. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: es `--no-async-scheduling` when TP>1 bug ### Your current environment latest main ### 🐛 Describe the bug As reported in https://github.com/vllm-project/vllm/pull/36687/, PD for SSM models (eg NemotronH, Qwen3.5..) with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: PD disaggregation for SSM models requires `--no-async-scheduling` when TP>1 bug ### Your current environment latest main ### 🐛 Describe the bug As reported in https://github.com/vllm-project/vllm/pull/36687/, PD...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: PD disaggregation for SSM models requires `--no-async-scheduling` when TP>1 bug ### Your current environment latest main ### 🐛 Describe the bug As reported in https://github.com/vllm-project/vllm/pull/36687/, PD...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: stics: - DTP1-PTP1 works great (also tested with --distributed-executor-backend=mp ) - DTP2-PTP2 accuracy jitters a lot - higher TP eg TP4 appear to jitter more - DTP2-PTP2 --no-async-scheduling works great - adding a `...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: .) with TP > 1 currently requires `--no-async-scheduling` to run without accuracy drops. @ZhanqiuHu and I identified a synchronization issue where states may be transferred in a corrupted form, leading to high variance...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
