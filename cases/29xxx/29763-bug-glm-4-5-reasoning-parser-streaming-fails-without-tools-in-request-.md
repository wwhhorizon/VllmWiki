# vllm-project/vllm#29763: [Bug]: GLM-4.5 reasoning parser streaming fails without tools in request - missing as_list() conversion

| 字段 | 值 |
| --- | --- |
| Issue | [#29763](https://github.com/vllm-project/vllm/issues/29763) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | operator;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5 reasoning parser streaming fails without tools in request - missing as_list() conversion

### Issue 正文摘录

### Your current environment vLLM version: 0.9.1 (built from source) Model: GLM-4.5-Air (AWQ 4-bit quantized) Hardware: NVIDIA GB10 Flags: --reasoning-parser glm45 --enable-reasoning ### 🐛 Describe the bug ## Bug Description The GLM-4.5 reasoning parser (`--reasoning-parser glm45`) fails to extract `reasoning_content` during **streaming** chat completions when **no tools are included in the request**. The ` ` tags leak into the `content` field while `reasoning_content` remains `null`. ### Observed Behavior | Scenario | `reasoning_content` | `content` | |----------|---------------------|-----------| | WITH tools in request | ✅ Correctly populated | ✅ Clean | | WITHOUT tools in request | ❌ `null` | ❌ Contains ` ... ` tags | ### Expected Behavior Both scenarios should correctly populate `reasoning_content` with thinking text and `content` with the final response. ## Root Cause In `vllm/entrypoints/openai/serving_chat.py`, line 1034 passes `output.token_ids` directly to the reasoning parser without converting it using `as_list()`. **Line 1034 (BUG):** ```python elif self.reasoning_parser: delta_message = reasoning_parser.extract_reasoning_content_streaming( previous_text, current_text...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: g parser streaming fails without tools in request - missing as_list() conversion bug;stale ### Your current environment vLLM version: 0.9.1 (built from source) Model: GLM-4.5-Air (AWQ 4-bit quantized) Hardware: NVIDIA G...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GLM-4.5 reasoning parser streaming fails without tools in request - missing as_list() conversion bug;stale ### Your current environment vLLM version: 0.9.1 (built from source) Model: GLM-4.5-Air (AWQ 4-bit quanti...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t vLLM version: 0.9.1 (built from source) Model: GLM-4.5-Air (AWQ 4-bit quantized) Hardware: NVIDIA GB10 Flags: --reasoning-parser glm45 --enable-reasoning ### 🐛 Describe the bug ## Bug Description The GLM-4.5 reasoning...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: le ### Your current environment vLLM version: 0.9.1 (built from source) Model: GLM-4.5-Air (AWQ 4-bit quantized) Hardware: NVIDIA GB10 Flags: --reasoning-parser glm45 --enable-reasoning ### 🐛 Describe the bug ## Bug Des...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
