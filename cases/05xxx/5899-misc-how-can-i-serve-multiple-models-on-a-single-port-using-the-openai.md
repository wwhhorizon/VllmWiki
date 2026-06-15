# vllm-project/vllm#5899: [Misc]: How can I serve multiple models on a single port using the OpenAI API?

| 字段 | 值 |
| --- | --- |
| Issue | [#5899](https://github.com/vllm-project/vllm/issues/5899) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: How can I serve multiple models on a single port using the OpenAI API?

### Issue 正文摘录

### Anything you want to discuss about vllm. I deployed a model on port 4400 using the OpenAI API. When I try to deploy another model on the same port, I get an error as follow. Is there any way I can deploy two models on the same port? command: python -m vllm.entrypoints.openai.api_server --served-model-name Invoke --model ./models/invoke_model --gpu-memory-utilization 0.35 --port 4400 python -m vllm.entrypoints.openai.api_server --served-model-name Emotion --model ./models/emotion_model --gpu-memory-utilization 0.35 --port 4400 ERROR: [Errno 98] error while attempting to bind on address ('0.0.0.0', 4400): address already in use

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Misc]: How can I serve multiple models on a single port using the OpenAI API? ### Anything you want to discuss about vllm. I deployed a model on port 4400 using the OpenAI API. When I try to deploy another model on the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
