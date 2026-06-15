# vllm-project/vllm#3717: [Feature]: Distribute sets of default chat template for models do not provide one

| 字段 | 值 |
| --- | --- |
| Issue | [#3717](https://github.com/vllm-project/vllm/issues/3717) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Distribute sets of default chat template for models do not provide one

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Thanks to our amazing community, we have gathered a set of good chat template for models. These template are useful when the original model's `tokenizer_config.json` doesn't provide the chat/instruction template the model is tuned with. ```shell ~/vllm/examples$ ls | rg jinja template_alpaca.jinja template_baichuan.jinja template_chatglm.jinja template_chatglm2.jinja template_chatml.jinja template_falcon.jinja template_falcon_180b.jinja template_inkbot.jinja ``` Concretely, given a model being served in OpenAI interface under chat endpoint, if the chat template is not found, try load up the ones which we can distribute with package data. Some pointers: * https://github.com/vllm-project/vllm/blob/f342153b4892789616a9bf58b6b9348dcb2329c3/vllm/entrypoints/openai/serving_chat.py#L316 * https://github.com/vllm-project/vllm/blob/f342153b4892789616a9bf58b6b9348dcb2329c3/vllm/model_executor/model_loader.py#L28 ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Distribute sets of default chat template for models do not provide one feature request;stale ### 🚀 The feature, motivation and pitch Thanks to our amazing community, we have gathered a set of good chat templa...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: bute sets of default chat template for models do not provide one feature request;stale ### 🚀 The feature, motivation and pitch Thanks to our amazing community, we have gathered a set of good chat template for models. Th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
