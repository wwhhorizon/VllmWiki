# vllm-project/vllm#39584: [Bug]:  AssertionError: Multiple tool calls in one delta is not supported - Responses API streaming crashes when model generates parallel tool calls

| 字段 | 值 |
| --- | --- |
| Issue | [#39584](https://github.com/vllm-project/vllm/issues/39584) |
| 状态 | open |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  AssertionError: Multiple tool calls in one delta is not supported - Responses API streaming crashes when model generates parallel tool calls

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description When using the vLLM Responses API with streaming enabled and multiple tools configured, the server crashes with an AssertionError when the model generates multiple tool calls that get bundled into a single SSE delta event. The assertion at vllm/entrypoints/openai/responses/serving.py:1761 assumes exactly one tool call per delta: assert len(pm.tool_calls) == 1, ( "Multiple tool calls in one delta is not supported" ) This violates the OpenAI Responses API specification, which explicitly states that multiple tool calls per turn are supported and should be emitted as separate events. Steps to Reproduce 1. Start vLLM Server docker run -d --name vllm-qwen35-v2 \ --gpus all \ --net=host \ --ipc=host \ -v ~/qwen-v2-project/models:/models \ vllm-qwen35-v2 \ serve /models/qwen35-122b-hybrid \ --served-model-name qwen \ --max-model-len 262144 \ --gpu-memory-utilization 0.90 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_xml \ --port 8000 \ --host 0.0.0.0 \ --load-format fastsafetensors \ --attention-backend FLASHINFER \ --speculative-config '{"method":"mtp","num_speculative_tokens":2}' \ --over...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: one delta is not supported" ) This violates the OpenAI Responses API specification, which explicitly states that multiple tool calls per turn are supported and should be emitted as separate events. Steps to Reproduce 1....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: 000 \ --host 0.0.0.0 \ --load-format fastsafetensors \ --attention-backend FLASHINFER \ --speculative-config '{"method":"mtp","num_speculative_tokens":2}' \ --override-generation-config '{ "temperature": 0.6, "top_p": 0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: lls in one delta is not supported - Responses API streaming crashes when model generates parallel tool calls bug ### Your current environment ### 🐛 Describe the bug Description When using the vLLM Responses API with str...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: --load-format fastsafetensors \ --attention-backend FLASHINFER \ --speculative-config '{"method":"mtp","num_speculative_tokens":2}' \ --override-generation-config '{ "temperature": 0.6, "top_p": 0.9, "top_k": 20, "repet...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: xml ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
