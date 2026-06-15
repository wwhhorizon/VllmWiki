# vllm-project/vllm#34237: [Bug]: Responses API with Harmony is broken for structured content inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#34237](https://github.com/vllm-project/vllm/issues/34237) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Responses API with Harmony is broken for structured content inputs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug As described by the Cursor bot [here](https://github.com/vllm-project/vllm/pull/31737#discussion_r2756219793), when the system message is passed as the structured content type instead of a string, the model identity ends up being the structured format `[{"type": "input_text", "text": " "}]`, which breaks building the input in Harmony ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: essage is passed as the structured content type instead of a string, the model identity ends up being the structured format `[{"type": "input_text", "text": " "}]`, which breaks building the input in Harmony ### Before...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: structured format `[{"type": "input_text", "text": " "}]`, which breaks building the input in Harmony ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ony ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
