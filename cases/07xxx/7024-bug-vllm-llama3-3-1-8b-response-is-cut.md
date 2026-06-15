# vllm-project/vllm#7024: [Bug]: vllm llama3/3.1-8b response is cut 

| 字段 | 值 |
| --- | --- |
| Issue | [#7024](https://github.com/vllm-project/vllm/issues/7024) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm llama3/3.1-8b response is cut 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug **problem is when I set max_tokens = any_size. then response is that much size instead of message context. so max_tokens are never enough** When calling llama3 using vllm message is always truncated Here is the response I have tried to play with different parameters but couldn't found any way to solve this issue. any suggestions?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: vllm llama3/3.1-8b response is cut bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug **problem is when I set max_tokens = any_size. then response is t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: vllm llama3/3.1-8b response is cut bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug **problem is when I set max_tokens = any_size. then response is t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
