# vllm-project/vllm#23430: [Bug]: Reasoning parser enabled by default and cannot be disabled

| 字段 | 值 |
| --- | --- |
| Issue | [#23430](https://github.com/vllm-project/vllm/issues/23430) |
| 状态 | closed |
| 标签 | bug;stale;gpt-oss |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Reasoning parser enabled by default and cannot be disabled

### Issue 正文摘录

I run vllm on an offline environment with `vllm serve`, and since the new 0.10.1 release, the reasoning parser is enabled and I can't disable it. I tried only with gpt-oss model. Maybe add a parameter to disable it like `--no-reasoning-parser` or `--reasoning-parser=false`

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: g]: Reasoning parser enabled by default and cannot be disabled bug;stale;gpt-oss I run vllm on an offline environment with `vllm serve`, and since the new 0.10.1 release, the reasoning parser is enabled and I can't disa...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: eter to disable it like `--no-reasoning-parser` or `--reasoning-parser=false`
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Reasoning parser enabled by default and cannot be disabled bug;stale;gpt-oss I run vllm on an offline environment with `vllm serve`, and since the new 0.10.1 release, the reasoning parser is enabled and I can't d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
