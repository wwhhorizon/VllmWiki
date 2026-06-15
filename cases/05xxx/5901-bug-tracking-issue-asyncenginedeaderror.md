# vllm-project/vllm#5901: [Bug]: TRACKING ISSUE: `AsyncEngineDeadError`

| 字段 | 值 |
| --- | --- |
| Issue | [#5901](https://github.com/vllm-project/vllm/issues/5901) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 24; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TRACKING ISSUE: `AsyncEngineDeadError`

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Recently, we have seen reports of `AsyncEngineDeadError`, including: - [x] #5060 - [x] #2000 - [x] #3310 - [x] #3839 - [x] #4000 - [x] #4135 - [x] #4293 - [x] #5443 - [x] #5732 - [x] #5822 - [x] #6190 - [x] #6208 - [x] #6361 - [x] #6421 - [x] #6614 - [x] #6790 - [x] #6969 - [x] #7356 If you see something like the following, please report here: ```bash 2024-06-25 12:27:29.905 File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/api_server.py", line 84, in health 2024-06-25 12:27:29.905 await openai_serving_chat.engine.check_health() 2024-06-25 12:27:29.905 File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 839, in check_health 2024-06-25 12:27:29.905 raise AsyncEngineDeadError("Background loop is stopped.") 2024-06-25 12:27:29.905 vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop is stopped. ``` Key areas we are looking into include: - logprob usage - guided regex usage When reporting an issue, please include a sample request that causes the issue so we can reproduce on our side.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: TRACKING ISSUE: `AsyncEngineDeadError` bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug Recently, we have seen reports of `AsyncEngineDeadError`, inc...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: n issue, please include a sample request that causes the issue so we can reproduce on our side.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
