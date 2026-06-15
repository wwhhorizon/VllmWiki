# vllm-project/vllm#19846: [Bug]: When "tool_choice": "auto" is set, there is a reasoning_content process in the output, but this process is missing when "tool_choice": "required" is used.

| 字段 | 值 |
| --- | --- |
| Issue | [#19846](https://github.com/vllm-project/vllm/issues/19846) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When "tool_choice": "auto" is set, there is a reasoning_content process in the output, but this process is missing when "tool_choice": "required" is used.

### Issue 正文摘录

### Your current environment version 0.9.1 vllm serve qwen3 --port 8002 --trust-remote-code --served-model-name qwen32 --max-model-len 32000 --gpu-memory-utilization 0.9 --dtype auto --enable-auto-tool-choice --tool-call-parser hermes ### 🐛 Describe the bug When "tool_choice": "auto" is set, there is a reasoning_content process in the output, but this process is missing when "tool_choice": "required" is used. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: s used. bug;stale ### Your current environment version 0.9.1 vllm serve qwen3 --port 8002 --trust-remote-code --served-model-name qwen32 --max-model-len 32000 --gpu-memory-utilization 0.9 --dtype auto --enable-auto-tool...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ool_choice": "required" is used. bug;stale ### Your current environment version 0.9.1 vllm serve qwen3 --port 8002 --trust-remote-code --served-model-name qwen32 --max-model-len 32000 --gpu-memory-utilization 0.9 --dtyp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: l-name qwen32 --max-model-len 32000 --gpu-memory-utilization 0.9 --dtype auto --enable-auto-tool-choice --tool-call-parser hermes ### 🐛 Describe the bug When "tool_choice": "auto" is set, there is a reasoning_content pr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: d. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: but this process is missing when "tool_choice": "required" is used. bug;stale ### Your current environment version 0.9.1 vllm serve qwen3 --port 8002 --trust-remote-code --served-model-name qwen32 --max-model-len 32000...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
