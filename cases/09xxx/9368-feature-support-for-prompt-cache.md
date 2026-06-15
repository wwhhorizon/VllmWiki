# vllm-project/vllm#9368: [Feature]: support for prompt cache

| 字段 | 值 |
| --- | --- |
| Issue | [#9368](https://github.com/vllm-project/vllm/issues/9368) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: support for prompt cache

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Is it possible to somehow fix some of the KV cache for common instruction + specific part of the prompt so that it is reused across multiple inferences of the model? it can be done in [transformers](https://huggingface.co/) and i think it is a common feature in some discussion [https://discuss.huggingface.co/t/how-to-cache-common-instruction-prompt/101419](https://discuss.huggingface.co/t/how-to-cache-common-instruction-prompt/101419) ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: art of the prompt so that it is reused across multiple inferences of the model? it can be done in [transformers](https://huggingface.co/) and i think it is a common feature in some discussion [https://discuss.huggingfac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: support for prompt cache feature request;stale ### 🚀 The feature, motivation and pitch Is it possible to somehow fix some of the KV cache for common instruction + specific part of the prompt so that it is reu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: possible to somehow fix some of the KV cache for common instruction + specific part of the prompt so that it is reused across multiple inferences of the model? it can be done in [transformers](https://huggingface.co/) a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: feature, motivation and pitch Is it possible to somehow fix some of the KV cache for common instruction + specific part of the prompt so that it is reused across multiple inferences of the model? it can be done in [tran...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
