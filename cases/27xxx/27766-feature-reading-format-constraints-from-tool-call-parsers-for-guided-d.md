# vllm-project/vllm#27766: [Feature]: Reading format constraints from tool call parsers for guided decoding.

| 字段 | 值 |
| --- | --- |
| Issue | [#27766](https://github.com/vllm-project/vllm/issues/27766) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Reading format constraints from tool call parsers for guided decoding.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch If I understand it correctly, in vllm, the code that enforces guided decoding is here: https://github.com/vllm-project/vllm/blob/fcb1d570bb8f95f5b7ded716a52fec902c535f0e/vllm/entrypoints/openai/serving_engine.py#L1106 It always calls the `adjust_request` function in the abstract tool parser. This function enforces `json` grammar for the tool calls. https://github.com/vllm-project/vllm/blob/fcb1d570bb8f95f5b7ded716a52fec902c535f0e/vllm/entrypoints/openai/tool_parsers/abstract_tool_parser.py#L47-L63 However, suppose a model with different tool call parsing behavior (e.g., Qwen3-Coder expects XML-format of tool calls). When setting the tool_choice to `required`, vllm will still enforce the `json` grammar instead of the XML grammar. It harms models' performance. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Reading format constraints from tool call parsers for guided decoding. feature request;stale ### 🚀 The feature, motivation and pitch If I understand it correctly, in vllm, the code that enforces guided decodi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g format constraints from tool call parsers for guided decoding. feature request;stale ### 🚀 The feature, motivation and pitch If I understand it correctly, in vllm, the code that enforces guided decoding is here: https...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
