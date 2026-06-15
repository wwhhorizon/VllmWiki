# vllm-project/vllm#29408: [Bug]:Reasoning parser work wrong with Qwen3-VL-Thinking-30B-A3B-FP8

| 字段 | 值 |
| --- | --- |
| Issue | [#29408](https://github.com/vllm-project/vllm/issues/29408) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Reasoning parser work wrong with Qwen3-VL-Thinking-30B-A3B-FP8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Reasoning Parser Work Wrong On Qwen3 VL Thinking reasoning_parser:deepseek-r1 VLLM Start Command ```bash vllm serve \ --model Qwen/Qwen3-VL-30B-A3B-Thinking-FP8 \ --served-model-name qwen3-thinking --pipeline-parallel-size 3 \ --max-num-seqs 16 \ --gpu-memory-utilization 0.9 \ --reasoning-parser deepseek_r1\ --tool-call-parser hermes \ --enable_auto_tool_choice ``` With Curl ```bash curl -X POST 'http://abcdefg/v1/chat/completions' \ -H 'Authorization: Bearer sk-' \ -H 'Content-Type: application/json' \ -d '{ "model": "qwen3-thinking", "stream": true, "messages": [ { "role": "user", "content": "请告诉我北京的天气情况" }, { "role": "assistant", "content": "天气", "reasoning":"天气", "tool_calls": [ { "id": "call_26884d11-ff6b-48fb-ada7-734f3fd0dfcc", "type": "function", "function": { "name": "get_weather", "arguments": "{\"city\": \"Beijing\"}" } } ] }, { "role": "tool", "tool_call_id": "call_26884d11-ff6b-48fb-ada7-734f3fd0dfcc", "content": "{\"city\": \"Beijing\", \"temperature\": \"18°C\", \"condition\": \"多云\", \"humidity\": \"55%\"}" } ], "tools": [ { "type": "function", "function": { "name": "get_weather", "description": "Get weather infor...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]:Reasoning parser work wrong with Qwen3-VL-Thinking-30B-A3B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug Reasoning Parser Work Wrong On Qwen3 VL Thinking reasoning_parser:deepseek-r1 VLLM Start...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]:Reasoning parser work wrong with Qwen3-VL-Thinking-30B-A3B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug Reasoning Parser Work Wrong On Qwen3 VL Thinking reasoning_parser:deepseek-r1 VLLM Start...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: "name": "get_weather", "arguments": "{\"city\": \"Beijing\"}" } } ] }, { "role": "tool", "tool_call_id": "call_26884d11-ff6b-48fb-ada7-734f3fd0d
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]:Reasoning parser work wrong with Qwen3-VL-Thinking-30B-A3B-FP8 bug;stale ### Your current environment ### 🐛 Describe the bug Reasoning Parser Work Wrong On Qwen3 VL Thinking reasoning_parser:deepseek-r1 VLLM Start...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
