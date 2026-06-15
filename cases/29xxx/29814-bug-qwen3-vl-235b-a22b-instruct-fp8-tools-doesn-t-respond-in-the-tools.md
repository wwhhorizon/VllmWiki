# vllm-project/vllm#29814: [Bug]: Qwen3-VL-235B-A22B-Instruct-FP8 tools doesn't respond in the tools but in content for hermes parswer

| 字段 | 值 |
| --- | --- |
| Issue | [#29814](https://github.com/vllm-project/vllm/issues/29814) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-235B-A22B-Instruct-FP8 tools doesn't respond in the tools but in content for hermes parswer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We are running 0.11.2 and getting this from the output of a tools call "choices": [ ```json { "index": 0, "message": { "role": "assistant", "content": " \n{\"name\": \"get_current_date\", \"arguments\": {\"timezone\": \"UTC\"}}\n ", "tool_calls": null, "function_call": null, "provider_specific_fields": null }, "finish_reason": "stop" } ] } ``` it seems for this Qwen3-VL-235B-A22B-Instruct-FP8 model the hermes parser is not working or something properly? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-VL-235B-A22B-Instruct-FP8 tools doesn't respond in the tools but in content for hermes parswer bug;stale ### Your current environment ### 🐛 Describe the bug We are running 0.11.2 and getting this from the o...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: "tool_calls": null, "function_call": null, "provider_specific_fields": null }, "finish_reason": "stop" } ] } ``` it seems for this Qwen3-VL-235B-A22B-Instruct-FP8 model the hermes parser is not working or something prop...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Bug]: Qwen3-VL-235B-A22B-Instruct-FP8 tools doesn't respond in the tools but in content for hermes parswer bug;stale ### Your current environment ### 🐛 Describe the bug We are running 0.11.2 and getting this from the o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ly? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: tools doesn't respond in the tools but in content for hermes parswer bug;stale ### Your current environment ### 🐛 Describe the bug We are running 0.11.2 and getting this from the output of a tools call "choices": [ ```j...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
