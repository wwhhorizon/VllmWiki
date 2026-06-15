# vllm-project/vllm#19051: [Bug]: 400 response when using Qwen3 + reasoning + tool calling + tool_choice "required"

| 字段 | 值 |
| --- | --- |
| Issue | [#19051](https://github.com/vllm-project/vllm/issues/19051) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: 400 response when using Qwen3 + reasoning + tool calling + tool_choice "required"

### Issue 正文摘录

### Your current environment docker container tagged `image: vllm/vllm-openai:v0.9.0.1` ### 🐛 Describe the bug I am launching vllm via docker with these args: ``` --model Qwen/Qwen3-30B-A3B-FP8 --reasoning-parser qwen3 --max-num-seqs 4 --tool-call-parser hermes --enable-auto-tool-choice --enable-reasoning --served-model-name model --max-model-len 32648 -tp 2 ``` Everything works great - reasoning is parsed, tool calls work (in most scenarios), etc. But there's one specific scenario where it consistently fails, and the service returns a 400: when I make a request with `"tool_choice": "required"`, it seems to conflict with the reasoning parsing. I get an error response like so ``` {'object': 'error', 'message': '1 validation error for list[function-wrap[__log_extra_fields__()]]\n Invalid JSON: expected value at line 1 column 1 [type=json_invalid, input_value=\' \\nOkay, the user ...ng set 2025"\\n }\\n}\\n]\', input_type=str]\n For further information visit https://errors.pydantic.dev/2.11/v/json_invalid', 'type': 'BadRequestError', 'param': None, 'code': 400} ``` I guess the relevant part from the above is: ``` Invalid JSON: expected value at line 1 column 1 [type=json_invalid, inp...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: 400 response when using Qwen3 + reasoning + tool calling + tool_choice "required" bug ### Your current environment docker container tagged `image: vllm/vllm-openai:v0.9.0.1` ### 🐛 Describe the bug I am launching...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: tool calling + tool_choice "required" bug ### Your current environment docker container tagged `image: vllm/vllm-openai:v0.9.0.1` ### 🐛 Describe the bug I am launching vllm via docker with these args: ``` --model Qwen/Q...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g vllm via docker with these args: ``` --model Qwen/Qwen3-30B-A3B-FP8 --reasoning-parser qwen3 --max-num-seqs 4 --tool-call-parser hermes --enable-auto-tool-choice --enable-reasoning --served-model-name model --max-mode...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ry. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ere it consistently fails, and the service returns a 400: when I make a request with `"tool_choice": "required"`, it seems to conflict with the reasoning parsing. I get an error response like so ``` {'object': 'error',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
