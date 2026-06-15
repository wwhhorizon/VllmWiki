# vllm-project/vllm#38738: [Bug]: Anthropic Messages API + Mistral model: "Invalid assistant message" on multi-turn tool calling

| 字段 | 值 |
| --- | --- |
| Issue | [#38738](https://github.com/vllm-project/vllm/issues/38738) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Anthropic Messages API + Mistral model: "Invalid assistant message" on multi-turn tool calling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## Current environment - vLLM version: 0.18.1 - Model: `mistralai/Ministral-3-14B-Instruct-2512` (official release) - Served model name: `ministral-3:14b` - Also reproduced with: `cyankiwi/Ministral-3-14B-Instruct-2512-AWQ-4bit` (AWQ 4-bit quantized) - Python: 3.12.10 - OS: Linux ## Describe the bug When using the Anthropic Messages API endpoint (`/v1/messages`) with a Mistral model and tool calling enabled, multi-turn conversations crash on the second turn with: ``` Invalid assistant message: role='assistant' content='' tool_calls=None prefix=False ``` The first turn works fine: model receives prompt, responds with tool calls, tools execute successfully. The error occurs when sending tool results back for the next model turn. The Anthropic adapter generates an empty assistant message internally during Anthropic-to-OpenAI format conversion that the Mistral renderer then rejects. ## Server command ```bash vllm serve mistralai/Ministral-3-14B-Instruct-2512 \ --host 0.0.0.0 \ --port 11434 \ --gpu-memory-utilization 0.95 \ --max-model-len 82000 \ --max-num-batched-tokens 8192 \ --tokenizer_mode auto \ --served-model-name ministral-3:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t environment ### 🐛 Describe the bug ## Current environment - vLLM version: 0.18.1 - Model: `mistralai/Ministral-3-14B-Instruct-2512` (official release) - Served model name: `ministral-3:14b` - Also reproduced with: `cy...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Anthropic Messages API + Mistral model: "Invalid assistant message" on multi-turn tool calling bug ### Your current environment ### 🐛 Describe the bug ## Current environment - vLLM version: 0.18.1 - Model: `mistr...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: x=False ``` Originating from: ``` File "vllm/entrypoints/anthropic/api_router.py", line 70, in create_messages generator = await handler.create_messages(request, raw_request) File "vllm/entrypoints/anthropic/serving.py"...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: tion_mistral_common.py", line 1510, in apply_chat_template tokenized_request = self.tokenizer.encode_chat_completion(chat_request) File "mistral_common/tokens/tokenizers/mistral.py", line 389, in encode_chat_completion...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
