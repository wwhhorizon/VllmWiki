# vllm-project/vllm#931: With OpenAI-Compatible Server, if stream output, some of the Chinese output are garbled text

| 字段 | 值 |
| --- | --- |
| Issue | [#931](https://github.com/vllm-project/vllm/issues/931) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> With OpenAI-Compatible Server, if stream output, some of the Chinese output are garbled text

### Issue 正文摘录

With the OpenAI-Compatible Server start curl like this: ``` shell curl http://localhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "WizardLM/WizardCoder", "prompt": "你是谁？", "max_tokens": 200, "temperature": 0 }' ``` The output all in Chinese and perform well, but when add the {"stream": "true"} param, output will be look like this: ```json {"id": "cmpl-1dab266887b14793b7a0d7031444c000", "object": "chat.completion.chunk", "created": 1693565963, "model": "WizardLM/WizardCoder-15B-V1.0", "choices": [{"index": 0, "delta": {"role": null, "content": "你好，我是一个人工智能助手，我可以��助你完成��种任务，比如查��信息、������会������、发送��件、提��事件等。你可以"}, "finish_reason": "stop"}]} ``` Some of the Chinese are garbled

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: lhost:8000/v1/completions \ -H "Content-Type: application/json" \ -d '{ "model": "WizardLM/WizardCoder", "prompt": "你是谁？", "max_tokens": 200, "temperature": 0 }' ``` The output all in Chinese and perform well, but when...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
