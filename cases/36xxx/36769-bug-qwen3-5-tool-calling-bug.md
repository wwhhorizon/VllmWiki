# vllm-project/vllm#36769: [Bug]: Qwen3.5 tool calling bug

| 字段 | 值 |
| --- | --- |
| Issue | [#36769](https://github.com/vllm-project/vllm/issues/36769) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5 tool calling bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am currently using Qwen3.5 9b -> specifically this variant | https://huggingface.co/lovedheart/Qwen3.5-9B-FP8 I present a list of options in the prompt and ask the LLM to choose one of the options using a designated tool call The majority of prompts work just fine, but a portion of all my requests run into the error message shown below ``` (APIServer pid=66306) ERROR 03-11 08:34:27 [qwen3coder_tool_parser.py:338] Error in extracting tool call from response. (APIServer pid=66306) ERROR 03-11 08:34:27 [qwen3coder_tool_parser.py:338] Traceback (most recent call last): (APIServer pid=66306) ERROR 03-11 08:34:27 [qwen3coder_tool_parser.py:338] File "/root/.venv/lib/python3.12/site-packages/vllm/tool_parsers/qwen3coder_tool_parser.py", line 310, in extract_tool_calls (APIServer pid=66306) ERROR 03-11 08:34:27 [qwen3coder_tool_parser.py:338] self._parse_xml_function_call(function_call_str, request.tools) (APIServer pid=66306) ERROR 03-11 08:34:27 [qwen3coder_tool_parser.py:338] File "/root/.venv/lib/python3.12/site-packages/vllm/tool_parsers/qwen3coder_tool_parser.py", line 246, in _parse_xml_function_call (APIServer pid=66306) ERROR...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: onment ### 🐛 Describe the bug I am currently using Qwen3.5 9b -> specifically this variant | https://huggingface.co/lovedheart/Qwen3.5-9B-FP8 I present a list of options in the prompt and ask the LLM to choose one of th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: specifically this variant | https://huggingface.co/lovedheart/Qwen3.5-9B-FP8 I present a list of options in the prompt and ask the LLM to choose one of the options using a designated tool call The majority of prompts wo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3.5 tool calling bug bug;rocm ### Your current environment ### 🐛 Describe the bug I am currently using Qwen3.5 9b -> specifically this variant | https://huggingface.co/lovedheart/Qwen3.5-9B-FP8 I present a li...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5 tool calling bug bug;rocm ### Your current environment ### 🐛 Describe the bug I am currently using Qwen3.5 9b -> specifically this variant | https://huggingface.co/lovedheart/Qwen3.5-9B-FP8 I present a li...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ool call The majority of prompts work just fine, but a portion of all my requests run into the error message shown below ``` (APIServer pid=66306) ERROR 03-11 08:34:27 [qwen3coder_tool_parser.py:338] Error in extracting...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
