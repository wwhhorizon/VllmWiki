# vllm-project/vllm#37175: [Usage]:wen3.5-35B-A3B (FP8) with vLLM 0.17.1 , the first request takes significantly longer than subsequent requests

| 字段 | 值 |
| --- | --- |
| Issue | [#37175](https://github.com/vllm-project/vllm/issues/37175) |
| 状态 | open |
| 标签 | usage |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;moe |
| 症状 | slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]:wen3.5-35B-A3B (FP8) with vLLM 0.17.1 , the first request takes significantly longer than subsequent requests

### Issue 正文摘录

### Your current environment ```text ``` ### How would you like to use vllm ## Description When serving **Qwen3.5-35B-A3B** (FP8) with vLLM 0.17.1 , the **first request** takes significantly longer than subsequent requests (e.g., 30+ seconds vs ~2 seconds). ## Reproduction **Launch command:** ```bash vllm serve /workspace/models \ --api-key xxx \ --served-model-name qwen3-35b \ --tensor-parallel-size 2 \ --enable-expert-parallel \ --gpu-memory-utilization 0.9 \ --max-num-seqs 16 \ --max-model-len 262144 \ --reasoning-parser qwen3 \ --default-chat-template-kwargs '{"enable_thinking": false}' Observation: First POST /v1/chat/completions request is very slow; later requests are normal. Question Is this expected (e.g., due to lazy CUDA graph capture on first inference)? Is there a recommended way to warmup or pre-capture during startup so the first user request is fast? Hardware GPU: e.g., 2× A100 40GB ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]:wen3.5-35B-A3B (FP8) with vLLM 0.17.1 , the first request takes significantly longer than subsequent requests usage ### Your current environment ```text ``` ### How would you like to use vllm ## Description When...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: later requests are normal. Question Is this expected (e.g., due to lazy CUDA graph capture on first inference)? Is there a recommended way to warmup or pre-capture during startup so the first user request is fast? Hardw...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ``` ### How would you like to use vllm ## Description When serving **Qwen3.5-35B-A3B** (FP8) with vLLM 0.17.1 , the **first request** takes significantly longer than subsequent requests (e.g., 30+ seconds vs ~2 seconds)...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: --served-model-name qwen3-35b \ --tensor-parallel-size 2 \ --enable-expert-parallel \ --gpu-memory-utilization 0.9 \ --max-num-seqs 16 \ --max-model-len 262144 \ --reasoning-parser qwen3 \ --default-chat-template-kwargs...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: g-parser qwen3 \ --default-chat-template-kwargs '{"enable_thinking": false}' Observation: First POST /v1/chat/completions request is very slow; later requests are normal. Question Is this expected (e.g., due to lazy CUD...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
