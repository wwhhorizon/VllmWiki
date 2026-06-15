# vllm-project/vllm#43395: [Bug]: Responses API does not surface reasoning output with `--reasoning-parser gemma4` (works with deepseek_r1)

| 字段 | 值 |
| --- | --- |
| Issue | [#43395](https://github.com/vllm-project/vllm/issues/43395) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Responses API does not surface reasoning output with `--reasoning-parser gemma4` (works with deepseek_r1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug With `--reasoning-parser gemma4` enabled on vLLM v0.21.0, the Chat Completions API correctly surfaces model reasoning in a `reasoning` field alongside tool calls. However, the Responses API (`/v1/responses`) does not surface reasoning output in any form — `reasoning_tokens` is always 0 and no `ResponseReasoningItem` output item appears — even when `reasoning: {"effort": "high"}` is passed in the request. This is specific to the `gemma4` reasoning parser — tested with Qwen3 + `deepseek_r1` which works correctly on the same image. **Server start command:** ```bash docker run -d \ --name vllm-gemma4 \ --gpus all \ --ipc=host \ -p 8000:8000 \ -e VLLM_ENABLE_RESPONSES_API_STORE=1 \ vllm/vllm-openai:v0.21.0 \ --model google/gemma-4-26B-A4B-it \ --tensor-parallel-size 4 \ --max-model-len 32768 \ --gpu-memory-utilization 0.9 \ --max-num-seqs 4 \ --max-num-batched-tokens 14336 \ --tool-call-parser functiongemma \ --enable-auto-tool-choice \ --reasoning-parser gemma4 ``` **Reproduction script:** ```python import requests, json BASE = "http://localhost:8000/v1" MODEL = "google/gemma-4-26B-A4B-it" tools = [ { "type": "function", "name": "get...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: en `reasoning: {"effort": "high"}` is passed in the request. This is specific to the `gemma4` reasoning parser — tested with Qwen3 + `deepseek_r1` which works correctly on the same image. **Server start command:** ```ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Responses API does not surface reasoning output with `--reasoning-parser gemma4` (works with deepseek_r1) ### Your current environment ### 🐛 Describe the bug With `--reasoning-parser gemma4` enabled on vLLM v0.21.0, the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ly. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ing_tokens: 0 output types: ['message'] has ResponseReasoningItem: False === Responses API with tools + reasoning === reasoning_tokens: 0 output types: ['function_call'] has ResponseReasoningItem: False ``` **Note:** Th...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: hy Qwen3 works fine. 4. **`reasoning_tokens` counting also fails**: The fallback at `serving.py:866` that tries to count reasoning tokens from accumulated token IDs doesn't trigger for the gemma4 parser context. ### Rel...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
