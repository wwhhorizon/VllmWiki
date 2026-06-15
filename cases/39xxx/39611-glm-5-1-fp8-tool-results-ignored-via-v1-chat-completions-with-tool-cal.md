# vllm-project/vllm#39611: GLM-5.1-FP8: Tool results ignored via /v1/chat/completions with --tool-call-parser glm47 but work correctly via /v1/completions

| 字段 | 值 |
| --- | --- |
| Issue | [#39611](https://github.com/vllm-project/vllm/issues/39611) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | attention;fp8 |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> GLM-5.1-FP8: Tool results ignored via /v1/chat/completions with --tool-call-parser glm47 but work correctly via /v1/completions

### Issue 正文摘录

# GLM-5.1-FP8: Tool results ignored via /v1/chat/completions but work perfectly via /v1/completions ## Environment - **vLLM version**: `0.19.1.dev1+g43a9b1afb` - **transformers version**: `5.4.0` - **Docker image**: `vllm/vllm-openai:glm51-cu130` - **Model**: `zai-org/GLM-5.1-FP8` - **Hardware**: NVIDIA B300 DGX, 8 GPUs - **Startup flags**: ``` --model zai-org/GLM-5.1-FP8 --tensor-parallel-size 8 --tool-call-parser glm47 --reasoning-parser glm45 --enable-auto-tool-choice --served-model-name glm-5.1-fp8 ``` ## Bug Description When using `/v1/chat/completions` with `--tool-call-parser glm47`, GLM-5.1-FP8 **ignores tool results in multi-turn conversations** (the inbound round-trip). The model always responds as if the tool returned no data / an error, even though the tool result content is clearly provided. When using `/v1/completions` with the *exact same conversation* formatted using the correct chat template, the model reads and correctly reports tool results. **This proves the bug is in vLLM's chat completions pipeline**, not the model. ## Reproduction ### Test 1 (Outbound tool call) — ✅ PASSES ```bash curl -s http://localhost:8000/v1/chat/completions \ -H "Content-Type: applicat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: letions but work perfectly via /v1/completions ## Environment - **vLLM version**: `0.19.1.dev1+g43a9b1afb` - **transformers version**: `5.4.0` - **Docker image**: `vllm/vllm-openai:glm51-cu130` - **Model**: `zai-org/GLM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: GLM-5.1-FP8: Tool results ignored via /v1/chat/completions with --tool-call-parser glm47 but work correctly via /v1/completions # GLM-5.1-FP8: Tool results ignored via /v1/chat/completions but work perfectly via /v1/com...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: "tool_choice":"auto", "chat_template_kwargs": {"enable_thinking": false} }' ``` **Expected and actual result**: Correctly returns `tool_calls: [{"name": "get_weather", "arguments": {"city": "Vancouver"}}]` ✅ --- ### Tes...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ersion**: `5.4.0` - **Docker image**: `vllm/vllm-openai:glm51-cu130` - **Model**: `zai-org/GLM-5.1-FP8` - **Hardware**: NVIDIA B300 DGX, 8 GPUs - **Startup flags**: ``` --model zai-org/GLM-5.1-FP8 --tensor-parallel-size...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Even with `chat_template_kwargs: {"enable_thinking": false}` in the API request, vLLM's pipeline produces a **different (173-token) prompt** compared to the manually-rendered 170-token version. **Additional finding**: T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
