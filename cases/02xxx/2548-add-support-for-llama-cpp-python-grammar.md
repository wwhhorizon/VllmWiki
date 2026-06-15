# vllm-project/vllm#2548: Add Support for Llama-cpp-python Grammar

| 字段 | 值 |
| --- | --- |
| Issue | [#2548](https://github.com/vllm-project/vllm/issues/2548) |
| 状态 | closed |
| 标签 | structured-output |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Add Support for Llama-cpp-python Grammar

### Issue 正文摘录

Hi There, Love this server, super fast and really one of the few that utilises the GPUs I am using to their full capacity. The one problem I am having is that I use Grammar from Llama-cpp-python to control the output from the LLM and force it into a JSON format. Which I can parse. I have tried without it, and the formatting is just so poor that the remedial work required makes any time saving from the faster server a wash, bearing in mind I am dealing with thousands of requests not just one or two. It would be great if we could use grammar with vLLM and get back the responses we need. Appreciate the consideration.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Add Support for Llama-cpp-python Grammar structured-output Hi There, Love this server, super fast and really one of the few that utilises the GPUs I am using to their full capacity. The one problem I am having is that I...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: eally one of the few that utilises the GPUs I am using to their full capacity. The one problem I am having is that I use Grammar from Llama-cpp-python to control the output from the LLM and force it into a JSON format....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: the faster server a wash, bearing in mind I am dealing with thousands of requests not just one or two. It would be great if we could use grammar with vLLM and get back the responses we need. Appreciate the consideration.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
