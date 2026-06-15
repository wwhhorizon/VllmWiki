# vllm-project/vllm#4879: [Bug]: single lora request error make all processing requests error

| 字段 | 值 |
| --- | --- |
| Issue | [#4879](https://github.com/vllm-project/vllm/issues/4879) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: single lora request error make all processing requests error

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Vllm load lora checkpoints when executing model https://github.com/vllm-project/vllm/blob/v0.4.2/vllm/worker/model_runner.py#L789-L790 https://github.com/vllm-project/vllm/blob/v0.4.2/vllm/lora/worker_manager.py#L138-L172 Then when we get an error when loading lora checkpoint (e.g. lora rank > max_lora_rank), all processing requests would fail (no matter whether other requests use lora).

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: single lora request error make all processing requests error bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Vllm load lora checkpoints when executi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ` ``` ### 🐛 Describe the bug Vllm load lora checkpoints when executing model https://github.com/vllm-project/vllm/blob/v0.4.2/vllm/worker/model_runner.py#L789-L790 https://github.com/vllm-project/vllm/blob/v0.4.2/vllm/l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
