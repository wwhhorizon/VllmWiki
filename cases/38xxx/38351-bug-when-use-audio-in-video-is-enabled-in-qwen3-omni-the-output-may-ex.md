# vllm-project/vllm#38351: [Bug]: When use_audio_in_video is enabled in qwen3-omni, the output may exhibit issues such as empty or repetitive output.

| 字段 | 值 |
| --- | --- |
| Issue | [#38351](https://github.com/vllm-project/vllm/issues/38351) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When use_audio_in_video is enabled in qwen3-omni, the output may exhibit issues such as empty or repetitive output.

### Issue 正文摘录

### Your current environment My VLLM version: 0.12.0 When using `use_audio_in_video=true`, the output is abnormal. When this feature is disabled, the output is normal. How to solve it？ ### 🐛 Describe the bug ·· ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: as empty or repetitive output. bug ### Your current environment My VLLM version: 0.12.0 When using `use_audio_in_video=true`, the output is abnormal. When this feature is disabled, the output is normal. How to solve it？...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ·· ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: When use_audio_in_video is enabled in qwen3-omni, the output may exhibit issues such as empty or repetitive output. bug ### Your current environment My VLLM version: 0.12.0 When using `use_audio_in_video=true`, t...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
