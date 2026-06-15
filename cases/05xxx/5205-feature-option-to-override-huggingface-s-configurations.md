# vllm-project/vllm#5205: [Feature]: Option to override HuggingFace's configurations

| 字段 | 值 |
| --- | --- |
| Issue | [#5205](https://github.com/vllm-project/vllm/issues/5205) |
| 状态 | closed |
| 标签 | good first issue;feature request;unstale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Option to override HuggingFace's configurations

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The configuration files on HuggingFace may have missing information (e.g. #2051) or contain bugs (e.g. #4008). In such cases, it may be necessary to provide/override the configuration files to enable the model to be loaded correctly. However, apart from chat templates, there is currently no method of doing so; we have to update the source HuggingFace repository directly. It may take time for the authors of those repositories to respond, especially if they are unofficial ones which are not as well-maintained. It would be great if we could provide our own `config.json`, `tokenizer_config.json`, etc., through the vLLM CLI to apply patches as necessary. ### Related work #1756 lets us specify alternative chat templates or provide a chat template when it is missing from `tokenizer_config.json`. However, it currently only applies to the OpenAI API-compatible server. #5049 will add chat method to the main LLM entrypoint, but does not provide a built-in way to load the chat template automatically like in #1756. Some vLLM models have already hardcoded patches to HuggingFace `config.json`; these can be found under `vllm/transformers_utils/configs`.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Feature]: Option to override HuggingFace's configurations good first issue;feature request;unstale ### 🚀 The feature, motivation and pitch The configuration files on HuggingFace may have missing information (e.g. #2051...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Option to override HuggingFace's configurations good first issue;feature request;unstale ### 🚀 The feature, motivation and pitch The configuration files on HuggingFace may have missing information (e.g. #2051) or contai...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . It may take time for the authors of those repositories to respond, especially if they are unofficial ones which are not as well-maintained. It would be great if we could provide our own `config.json`, `tokenizer_confi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
