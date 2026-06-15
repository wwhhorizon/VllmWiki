# vllm-project/vllm#2402: Yi-34B-200K have empty output under default config (max_position_embedding=20000)

| 字段 | 值 |
| --- | --- |
| Issue | [#2402](https://github.com/vllm-project/vllm/issues/2402) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Yi-34B-200K have empty output under default config (max_position_embedding=20000)

### Issue 正文摘录

In Samsum benchmark, the Yi-34B-200K with max_position_embedding=20000 only output empty token (eos token) or 2-3 "\n" even when the context length is really small (around 1k). However, if I change the max_position_embedding from default to 32000 in model's config.json, the model output the summarization correctly. There is definitely something wrong, the setting of max_position_embedding should not effect the performance of short-context samples greatly.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Yi-34B-200K have empty output under default config (max_position_embedding=20000) stale In Samsum benchmark, the Yi-34B-200K with max_position_embedding=20000 only output empty token (eos token) or 2-3 "\n" even when th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pty token (eos token) or 2-3 "\n" even when the context length is really small (around 1k). However, if I change the max_position_embedding from default to 32000 in model's config.json, the model output the summarizatio...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 0K have empty output under default config (max_position_embedding=20000) stale In Samsum benchmark, the Yi-34B-200K with max_position_embedding=20000 only output empty token (eos token) or 2-3 "\n" even when the context...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: tput under default config (max_position_embedding=20000) stale In Samsum benchmark, the Yi-34B-200K with max_position_embedding=20000 only output empty token (eos token) or 2-3 "\n" even when the context length is reall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
