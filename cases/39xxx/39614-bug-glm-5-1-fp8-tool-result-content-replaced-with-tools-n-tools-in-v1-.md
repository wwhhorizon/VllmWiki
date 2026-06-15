# vllm-project/vllm#39614: [Bug] GLM-5.1-FP8: tool result content replaced with `<tools>\n</tools>` in /v1/chat/completions when --chat-template-content-format is auto

| 字段 | 值 |
| --- | --- |
| Issue | [#39614](https://github.com/vllm-project/vllm/issues/39614) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;multimodal_vlm;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | fp8;moe |
| 症状 | mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] GLM-5.1-FP8: tool result content replaced with `<tools>\n</tools>` in /v1/chat/completions when --chat-template-content-format is auto

### Issue 正文摘录

# Bug: Tool Result Content Corrupted in `/v1/chat/completions` with `--tool-call-parser glm47` ## Summary When using `/v1/chat/completions` with `--tool-call-parser glm47` and `--chat-template-content-format auto` (the default), GLM-5.1-FP8 completely ignores tool results in multi-turn conversations. The model always responds as if the tool returned no data. Using vLLM's `/tokenize` + `/detokenize` endpoints, we confirmed that the **actual prompt sent to the model** contains: ``` \n ``` The tool result content (`"15°C, partly cloudy"`) is entirely absent. In its place is the literal string ` \n ` — the empty tools XML wrapper from the system prompt section. ## Environment | | | |---|---| | **vLLM** | `0.19.1.dev1+g43a9b1afb` | | **transformers** | `5.4.0` | | **Docker image** | `vllm/vllm-openai:glm51-cu130` | | **Model** | `zai-org/GLM-5.1-FP8` | | **Hardware** | 8× NVIDIA B300 GPUs | | **Startup flags** | `--tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice` | ## Reproduction ### Test 1: Outbound tool call — ✅ PASSES ```bash curl -s http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "glm-5.1-fp8", "messages":...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: **vLLM** | `0.19.1.dev1+g43a9b1afb` | | **transformers** | `5.4.0` | | **Docker image** | `vllm/vllm-openai:glm51-cu130` | | **Model** | `zai-org/GLM-5.1-FP8` | | **Hardware** | 8× NVIDIA B300 GPUs | | **Startup flags**...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: `<tools>\n</tools>` in /v1/chat/completions when --chat-template-content-format is auto # Bug: Tool Result Content Corrupted in `/v1/chat/completions` with `--tool-call-parser glm47` ## Summary When using `/v1/chat/comp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug] GLM-5.1-FP8: tool result content replaced with `<tools>\n</tools>` in /v1/chat/completions when --chat-template-content-format is auto # Bug: Tool Result Content Corrupted in `/v1/chat/completions` with `--tool-ca...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: eather in Vancouver is currently **15°C** and **partly cloudy**."` ✅ ## Smoking Gun: Token Count Mismatch Using `/tokenize` + `/detokenize` to inspect the actual prompt vLLM sends to the model: | Request type | `prompt_...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: + `/detokenize` to inspect the actual prompt vLLM sends to the model: | Request type | `prompt_tokens` | Decoded ` ` content | |---|---|---| | `/v1/chat/completions` (Test 2) | **173** | ` \n ` ❌ | | `/v1/completions` (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
