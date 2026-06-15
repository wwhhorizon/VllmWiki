# vllm-project/vllm#39426: [Bug]:  /v1/responses: Protocol drift and malformed tool aggregation breaking official OpenAI SDK compatibility

| 字段 | 值 |
| --- | --- |
| Issue | [#39426](https://github.com/vllm-project/vllm/issues/39426) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  /v1/responses: Protocol drift and malformed tool aggregation breaking official OpenAI SDK compatibility

### Issue 正文摘录

### Your current environment [compile_project_v2.py](https://github.com/user-attachments/files/26607925/compile_project_v2.py) ### 🐛 Describe the bug Here’s what appears to be some legitimate vLLM errors. I have a custom AI client using the Python openai library. Gemini 3 Flash (Preview) generated this after working with me on my client implementation. The context for finding this is that we are trying to make my client work with the official OpenAI library and vLLM’s /v1/responses endpoint. We currently have to use a lower-level manual SSE parser to handle the stream because vLLM’s output is incompatible with the SDK’s internal assertions. Bug Report: vLLM /v1/responses Protocol Violations Breaking Official OpenAI SDK Environment: * Server: vLLM version 0.19.1.dev0+g2a69949bd.d20260408 * Model: /models/qwen35-122b-hybrid (Reasoning enabled) * Client: official openai-python SDK (v 2.31.0, Python 3.14.2) * Primary Reference: https://community.openai.com/t/responses-api-streaming-the-simple-guide-to-events/1363122 (Referred to as the “OpenAI Field Guide” below) * vLLM Protocol Reference: https://docs.vllm.ai/en/latest/api/vllm/entrypoints/openai/responses/protocol/ * Supplementary R...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: v1/responses: Protocol drift and malformed tool aggregation breaking official OpenAI SDK compatibility bug ### Your current environment [compile_project_v2.py](https://github.com/user-attachments/files/26607925/compile_...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: [Bug]: /v1/responses: Protocol drift and malformed tool aggregation breaking official OpenAI SDK compatibility bug ### Your current environment [compile_project_v2.py](https://github.com/user-attachments/files/26607925/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: g assembly. Encountering concatenated objects causes an internal state mismatch and an immediate crash. 2. PERFORMANCE: Redundant Instruction Echoing (Token Waste) Issue: vLLM echoes the full instructions block (system...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: K Environment: * Server: vLLM version 0.19.1.dev0+g2a69949bd.d20260408 * Model: /models/qwen35-122b-hybrid (Reasoning enabled) * Client: official openai-python SDK (v 2.31.0, Python 3.14.2) * Primary Reference: https://...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vent names like reasoning_part cause drift from the official SDK’s event-dispatch registry and trigger internal assertions during stream parsing. Suggested Remediation: Fix Aggregator: Ensure function_call_arguments str...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
