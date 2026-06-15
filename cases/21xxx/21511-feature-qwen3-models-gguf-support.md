# vllm-project/vllm#21511: [Feature]: Qwen3 Models GGUF Support

| 字段 | 值 |
| --- | --- |
| Issue | [#21511](https://github.com/vllm-project/vllm/issues/21511) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Qwen3 Models GGUF Support

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, GGUF versions of Qwen3 models raises "GGUF model with architecture qwen3 is not supported yet" error on vLLM. This error raised from Huggingface Transformers library, but they added support with this merged commit about 2 weeks ago (https://github.com/huggingface/transformers/pull/38645). I think just pulling the new version of transformers library would fix the error. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Qwen3 Models GGUF Support feature request;stale ### 🚀 The feature, motivation and pitch Currently, GGUF versions of Qwen3 models raises "GGUF model with architecture qwen3 is not supported yet" error on vLLM....
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Qwen3 Models GGUF Support feature request;stale ### 🚀 The feature, motivation and pitch Currently, GGUF versions of Qwen3 models raises "GGUF model with architecture qwen3 is not supported yet" error on vLLM....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e request;stale ### 🚀 The feature, motivation and pitch Currently, GGUF versions of Qwen3 models raises "GGUF model with architecture qwen3 is not supported yet" error on vLLM. This error raised from Huggingface Transfo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: pitch Currently, GGUF versions of Qwen3 models raises "GGUF model with architecture qwen3 is not supported yet" error on vLLM. This error raised from Huggingface Transformers library, but they added support with this me...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
