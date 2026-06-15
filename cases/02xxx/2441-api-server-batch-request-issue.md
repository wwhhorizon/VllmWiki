# vllm-project/vllm#2441: API Server batch request issue

| 字段 | 值 |
| --- | --- |
| Issue | [#2441](https://github.com/vllm-project/vllm/issues/2441) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> API Server batch request issue

### Issue 正文摘录

Hi, I am new to vLLM usage and i want to load and serve mistral 7b model using vLLM. Here is my brief understanding about vLLM. 1. LLM Engine => could handle offline batching (i.e list of prompts) 2. Async LLM Engine => wrapped with LLM Engine and could server async calls individually but only through online serving (api_server.py) Now I need to process batch calls (i..e list of prompts) through API server batch request. prompts = ["Give me a haiku poem"] * 10 How can I achieve this through api request. Kindly help me with this. Thanks in advance.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: issue Hi, I am new to vLLM usage and i want to load and serve mistral 7b model using vLLM. Here is my brief understanding about vLLM. 1. LLM Engine => could handle offline batching (i.e list of prompts) 2. Async LLM Eng...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: API Server batch request issue Hi, I am new to vLLM usage and i want to load and serve mistral 7b model using vLLM. Here is my brief understanding about vLLM. 1. LLM Engine => could handle offline batching (i.e list of...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
