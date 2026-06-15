# vllm-project/vllm#3333: What's difference between the seed in LLMEngine and seed in SamplingParams?

| 字段 | 值 |
| --- | --- |
| Issue | [#3333](https://github.com/vllm-project/vllm/issues/3333) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> What's difference between the seed in LLMEngine and seed in SamplingParams?

### Issue 正文摘录

I saw that vllm started to support per-request seed from 0.3.2. As far as I understand, we can set the seed both in [LLM engine](https://github.com/vllm-project/vllm/blob/654865e21df8ac6fe95de926625306e5756c2c0d/vllm/engine/llm_engine.py#L85) and in [SamplingParams](https://github.com/vllm-project/vllm/blob/654865e21df8ac6fe95de926625306e5756c2c0d/vllm/sampling_params.py#L107). Can anyone suggest the best practice of setting the random seed? For example, assuming I want only one seed, should I set it in the engine or in the sampling parameter? Does the seed in the sampling parameter override the other? Thanks!

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: t's difference between the seed in LLMEngine and seed in SamplingParams? stale I saw that vllm started to support per-request seed from 0.3.2. As far as I understand, we can set the seed both in [LLM engine](https://git...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
