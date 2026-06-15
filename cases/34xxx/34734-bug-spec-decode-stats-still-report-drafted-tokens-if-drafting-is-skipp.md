# vllm-project/vllm#34734: [Bug]: Spec Decode Stats still report drafted tokens if drafting is skipped

| 字段 | 值 |
| --- | --- |
| Issue | [#34734](https://github.com/vllm-project/vllm/issues/34734) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Spec Decode Stats still report drafted tokens if drafting is skipped

### Issue 正文摘录

### Your current environment omitted ### 🐛 Describe the bug When `input_fits_in_drafter` is triggered, drafting is skipped. But the stats still increase `drafts` and the number of draft tokens, so the stats show AR of 0.00 when the ISL is too long. When using the default EAGLE3 checkpoints ([see config here](https://huggingface.co/yuhuili/EAGLE3-LLaMA3.1-Instruct-8B/blob/main/config.json#L11)) any sequence beyond 2000 tokens will not use the drafter and will therefore show 0 acceptance rate. The stats in the log and also in `vllm bench serve` should respect input_fits_in_drafter or any other case when drafting is skipped. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: Spec Decode Stats still report drafted tokens if drafting is skipped bug;stale ### Your current environment omitted ### 🐛 Describe the bug When `input_fits_in_drafter` is triggered, drafting is skipped. But the s...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: hen the ISL is too long. When using the default EAGLE3 checkpoints ([see config here](https://huggingface.co/yuhuili/EAGLE3-LLaMA3.1-Instruct-8B/blob/main/config.json#L11)) any sequence beyond 2000 tokens will not use t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ed. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
