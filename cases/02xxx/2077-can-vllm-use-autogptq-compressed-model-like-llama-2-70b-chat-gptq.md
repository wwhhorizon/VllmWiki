# vllm-project/vllm#2077: can vllm use autogptq compressed model like llama-2-70b-chat-gptq

| 字段 | 值 |
| --- | --- |
| Issue | [#2077](https://github.com/vllm-project/vllm/issues/2077) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> can vllm use autogptq compressed model like llama-2-70b-chat-gptq

### Issue 正文摘录

I want to use [llama-2-70b-chat-gptq](https://huggingface.co/TheBloke/Llama-2-70B-Chat-GPTQ). Can it be used in vllm?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: can vllm use autogptq compressed model like llama-2-70b-chat-gptq I want to use [llama-2-70b-chat-gptq](https://huggingface.co/TheBloke/Llama-2-70B-Chat-GPTQ). Can it be used in vllm?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
