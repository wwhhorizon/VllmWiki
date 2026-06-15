# vllm-project/vllm#6669: [Bug]: The num_generation_tokens in stats is incorrect with speculative decoding

| 字段 | 值 |
| --- | --- |
| Issue | [#6669](https://github.com/vllm-project/vllm/issues/6669) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: The num_generation_tokens in stats is incorrect with speculative decoding

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug The current implementation of `_get_stats` assumes each sequence will get one new token at each iteration, which doesn't hold with speculative decoding: https://github.com/vllm-project/vllm/blob/c5e8330997dc3969818c6696a79820bcee44a702/vllm/engine/llm_engine.py#L1075-L1084 @cadedaniel I would like to submit a PR to fix it, before starting the work, I would like to how do you think about it? I would like to track the accepted new tokens by tracking the output of multi-step output processors's outputs in https://github.com/vllm-project/vllm/blob/c5e8330997dc3969818c6696a79820bcee44a702/vllm/engine/llm_engine.py#L821-L824

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: The num_generation_tokens in stats is incorrect with speculative decoding bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug The current implementation...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
