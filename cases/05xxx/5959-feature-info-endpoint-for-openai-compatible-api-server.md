# vllm-project/vllm#5959: [Feature]: `/info` endpoint for OpenAI-compatible API Server 

| 字段 | 值 |
| --- | --- |
| Issue | [#5959](https://github.com/vllm-project/vllm/issues/5959) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: `/info` endpoint for OpenAI-compatible API Server 

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When consuming models served via vLLM into other services, e.g. via [continue](https://github.com/continuedev), it's vital to know not only the name of the model available, but also it's configuration, especially the max input size. both 🤗TGI and Ollama already support this in their /info endpoint, allowing for automatic configuration of continue. ### Alternatives Might make even more sense to just add this information into the `/v1/models` endpoint ### Additional context [HF TGI /info](https://huggingface.github.io/text-generation-inference/#/Text%20Generation%20Inference/get_model_info) [auto-configure continue using HF TGI](https://github.com/continuedev/continue/pull/755) [auto-configure in continue using Ollama](https://github.com/continuedev/continue/pull/502/files) (old branch)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: feature request ### 🚀 The feature, motivation and pitch When consuming models served via vLLM into other services, e.g. via [continue](https://github.com/continuedev), it's vital to know not only the name of the model a...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t only the name of the model available, but also it's configuration, especially the max input size. both 🤗TGI and Ollama already support this in their /info endpoint, allowing for automatic configuration of continue. ##...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: `/info` endpoint for OpenAI-compatible API Server feature request ### 🚀 The feature, motivation and pitch When consuming models served via vLLM into other services, e.g. via [continue](https://github.com/cont...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
