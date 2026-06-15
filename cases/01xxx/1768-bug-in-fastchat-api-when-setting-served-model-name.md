# vllm-project/vllm#1768: Bug in fastchat API when setting served-model-name

| 字段 | 值 |
| --- | --- |
| Issue | [#1768](https://github.com/vllm-project/vllm/issues/1768) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Bug in fastchat API when setting served-model-name

### Issue 正文摘录

I need my model name to match chatGPT's in order to integrate with an existing product. To accomplish this by setting the 'served-model-name' option show below:: python -m vllm.entrypoints.openai.api_server \ --served-model-name gpt-3.5-turbo \ --model Intel/neural-chat-7b-v3-1 This causes the following error when making an API call POST http://192.168.254.161:8000/v1/chat/completions { "model": "chatgpt-3.5-turbo", "messages": [...] } Error: File "/home/dredon/miniconda3/envs/vllm/lib/python3.10/enum.py", line 710, in __new__ raise ve_exc ValueError: None is not a valid SeparatorStyle

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Bug in fastchat API when setting served-model-name I need my model name to match chatGPT's in order to integrate with an existing product. To accomplish this by setting the 'served-model-name' option show below:: python...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
