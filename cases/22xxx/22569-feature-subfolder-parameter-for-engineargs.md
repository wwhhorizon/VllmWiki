# vllm-project/vllm#22569: [Feature]: subfolder parameter for EngineArgs

| 字段 | 值 |
| --- | --- |
| Issue | [#22569](https://github.com/vllm-project/vllm/issues/22569) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: subfolder parameter for EngineArgs

### Issue 正文摘录

### 🚀 The feature, motivation and pitch HuggingFace supports downloading model from a subfolder of a HF repo as follows: ```python3 >>> import transformers >>> transformers.AutoModel.from_pretrained('tiiuae/dense-500m-arch1', revision='main', subfolder='iter_0002000') ``` However, there seems to be no way to do the same with vLLM, as a result of which I cannot use the model at all without first downloading it. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ngineArgs feature request;stale ### 🚀 The feature, motivation and pitch HuggingFace supports downloading model from a subfolder of a HF repo as follows: ```python3 >>> import transformers >>> transformers.AutoModel.from...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: subfolder parameter for EngineArgs feature request;stale ### 🚀 The feature, motivation and pitch HuggingFace supports downloading model from a subfolder of a HF repo as follows: ```python3 >>> import transfor...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: nloading model from a subfolder of a HF repo as follows: ```python3 >>> import transformers >>> transformers.AutoModel.from_pretrained('tiiuae/dense-500m-arch1', revision='main', subfolder='iter_0002000') ``` However, t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ansformers >>> transformers.AutoModel.from_pretrained('tiiuae/dense-500m-arch1', revision='main', subfolder='iter_0002000') ``` However, there seems to be no way to do the same with vLLM, as a result of which I cannot u...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
