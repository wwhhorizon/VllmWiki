# vllm-project/vllm#2649: Getting `logprobs` from Mistral / Mixtral?

| 字段 | 值 |
| --- | --- |
| Issue | [#2649](https://github.com/vllm-project/vllm/issues/2649) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Getting `logprobs` from Mistral / Mixtral?

### Issue 正文摘录

I am looking at the code for these models and would like to return the raw output of scores, as well as the softmax probabilities? Is there a parameter for this when calling the vLLM instance? As I am looking at the: https://github.com/vllm-project/vllm/blob/main/vllm/engine/llm_engine.py and https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/mixtral.py respectively as the areas where I would look to: 1) either fine the logprobs parameter or 2) code it myself, as I was using this in HuggingFace I would look to adapt the model.generate function to obtain these? I know this links to other examples, but I would appreciate your help on this specifically?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: look to adapt the model.generate function to obtain these? I know this links to other examples, but I would appreciate your help on this specifically?
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ng `logprobs` from Mistral / Mixtral? I am looking at the code for these models and would like to return the raw output of scores, as well as the softmax probabilities? Is there a parameter for this when calling the vLL...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
