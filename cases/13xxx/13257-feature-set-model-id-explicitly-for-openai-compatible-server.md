# vllm-project/vllm#13257: [Feature]: Set Model ID Explicitly for OpenAI-Compatible Server

| 字段 | 值 |
| --- | --- |
| Issue | [#13257](https://github.com/vllm-project/vllm/issues/13257) |
| 状态 | closed |
| 标签 | good first issue;feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Set Model ID Explicitly for OpenAI-Compatible Server

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Right now, when we start the model with OpenAI-Compatible Server, the model id is always the value of `--model`. That means: - when we loading the model from huggingface hub,the model id is `usrname/model` - when we loading the model from local, the model id is the local path - when we load the model from s3, the model id is the s3 address I do not think this is reasonable, since the client should not(need not) to know how or where the model was loaded. There should be a unique model id for them to call the API. Therefore I think a new entry argument that can set model id explicitly is very needed. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Feature]: Set Model ID Explicitly for OpenAI-Compatible Server good first issue;feature request ### 🚀 The feature, motivation and pitch Right now, when we start the model with OpenAI-Compatible Server, the model id is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: Set Model ID Explicitly for OpenAI-Compatible Server good first issue;feature request ### 🚀 The feature, motivation and pitch Right now, when we start the model with OpenAI-Compatible Server, the model id is...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: odel ID Explicitly for OpenAI-Compatible Server good first issue;feature request ### 🚀 The feature, motivation and pitch Right now, when we start the model with OpenAI-Compatible Server, the model id is always the value...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
