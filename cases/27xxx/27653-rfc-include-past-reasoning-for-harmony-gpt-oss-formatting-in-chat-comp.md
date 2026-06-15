# vllm-project/vllm#27653: [RFC]: include past-reasoning for harmony(gpt-oss) formatting in chat completions API

| 字段 | 值 |
| --- | --- |
| Issue | [#27653](https://github.com/vllm-project/vllm/issues/27653) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: include past-reasoning for harmony(gpt-oss) formatting in chat completions API

### Issue 正文摘录

### Motivation. With current implementation of https://github.com/vllm-project/vllm/blob/f58d9b64044e465b85e9280882c738e11b59b2d6/vllm/entrypoints/harmony_utils.py#L234 when gpt-oss is used with chat completions past reasoning is not included which breaks the model behaviour and (tools calls within chain of though), with current implementation model starts reasoning with every turn in complex scenarios which makes it quite unusable for multi turn multi tool call scenarios. ### Proposed Change. If user sends an assistant message with reasoning(or other field whatever you prefer) let's extend a conversation with another harmony `Message` with channel set to analysis inside this function which is already perfectly designed to do so https://github.com/vllm-project/vllm/blob/f58d9b64044e465b85e9280882c738e11b59b2d6/vllm/entrypoints/harmony_utils.py#L234 Obviously according to open-ai harmony formatting guide the previous analysis channels would be dropped. This will significantly increase gpt-oss usability ### Feedback Period. Would be nice if i can get feedback on that asap so i can start implementing that ### CC List. _No response_ ### Any Other Things. _No response_ ### Before submi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [RFC]: include past-reasoning for harmony(gpt-oss) formatting in chat completions API RFC;stale ### Motivation. With current implementation of https://github.com/vllm-project/vllm/blob/f58d9b64044e465b85e9280882c738e11b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: st-reasoning for harmony(gpt-oss) formatting in chat completions API RFC;stale ### Motivation. With current implementation of https://github.com/vllm-project/vllm/blob/f58d9b64044e465b85e9280882c738e11b59b2d6/vllm/entry...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
