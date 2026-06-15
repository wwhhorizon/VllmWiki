# vllm-project/vllm#24846: [Bug]: AttributeError: 'Gemma3Config' object has no attribute 'sliding_window'

| 字段 | 值 |
| --- | --- |
| Issue | [#24846](https://github.com/vllm-project/vllm/issues/24846) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'Gemma3Config' object has no attribute 'sliding_window'

### Issue 正文摘录

transformers version 4.55.0 ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3_mm.py#L691 In the following logic: if (sliding_window := self.config.sliding_window) is not None: If the attribute sliding_window does not exist in the config object (and it doesn't exist for Gemma3Config see https://github.com/huggingface/transformers/blob/main/src/transformers/models/gemma3/configuration_gemma3.py#L246), this will raise an AttributeError. Suggested fix : Replace the line with a safer getattr() call that handles missing attributes gracefully: self.sliding_window = getattr(self.config, "sliding_window", None) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: AttributeError: 'Gemma3Config' object has no attribute 'sliding_window' bug transformers version 4.55.0 ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3_mm.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 'Gemma3Config' object has no attribute 'sliding_window' bug transformers version 4.55.0 ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3_mm.py#L691 In the following...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ne) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: AttributeError: 'Gemma3Config' object has no attribute 'sliding_window' bug transformers version 4.55.0 ### 🐛 Describe the bug https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/models/gemma3_mm.p...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
