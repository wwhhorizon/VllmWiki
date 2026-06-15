# vllm-project/vllm#23240: [Feature]: qwen2.5 omni doesn't support bnb quantification.

| 字段 | 值 |
| --- | --- |
| Issue | [#23240](https://github.com/vllm-project/vllm/issues/23240) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: qwen2.5 omni doesn't support bnb quantification.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I'm trying to deploy qwen2.5-omni-3B on my laptop but found that it doesn't support bnb quantization. It seems that there is no other quantization version of qwen2.5-omni-3B that vllm can support now. Will bnb quantization for qwen2.5-omni be supported in the furture? ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: t support bnb quantization. It seems that there is no other quantization version of qwen2.5-omni-3B that vllm can support now. Will bnb quantization for qwen2.5-omni be supported in the furture? ### Alternatives _No res...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature]: qwen2.5 omni doesn't support bnb quantification. feature request ### 🚀 The feature, motivation and pitch I'm trying to deploy qwen2.5-omni-3B on my laptop but found that it doesn't support bnb quantization. I...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Feature]: qwen2.5 omni doesn't support bnb quantification. feature request ### 🚀 The feature, motivation and pitch I'm trying to deploy qwen2.5-omni-3B on my laptop but found that it doesn't support bnb quantization. I...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: qwen2.5 omni doesn't support bnb quantification. feature request ### 🚀 The feature, motivation and pitch I'm trying to deploy qwen2.5-omni-3B on my laptop but found that it doesn't support bnb quantization. I...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
