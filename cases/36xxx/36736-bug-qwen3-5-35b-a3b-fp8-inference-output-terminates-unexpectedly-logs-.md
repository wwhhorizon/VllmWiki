# vllm-project/vllm#36736: [Bug]: Qwen3.5-35B-A3B-FP8 inference output terminates unexpectedly, logs show normal but request hangs

| 字段 | 值 |
| --- | --- |
| Issue | [#36736](https://github.com/vllm-project/vllm/issues/36736) |
| 状态 | open |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;quantization;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;fp8 |
| 症状 | crash;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-35B-A3B-FP8 inference output terminates unexpectedly, logs show normal but request hangs

### Issue 正文摘录

**Environment:** - vLLM version: 0.17+ (CUDA 130) - Model: Qwen/Qwen3.5-35B-A3B-FP8 - GPU: RTX 5090D × 2 - Open WebUI version: 0.8.10 - Launch command: ```bash python3 -m vllm.entrypoints.openai.api_server \ --model /home/ragnarokchan/models/Qwen3.5-35B-A3B-FP8 \ --served-model-name Qwen3.5-35B-A3B-FP8 \ --trust-remote-code \ --gpu-memory-utilization 0.85 \ --host 0.0.0.0 \ --port 8000 \ --tensor-parallel-size 2 \ --enable-chunked-prefill \ --max-num-seqs 16 \ --max-model-len 65536 \ --tool-call-parser qwen3_coder \ --enable-auto-tool-choice \ --calculate-kv-scales \ --reasoning-parser qwen3 ``` **Bug Description:** When using Open WebUI to call vLLM for inference, the output suddenly terminates during generation. Logs show everything is normal, request status shows 200 OK, but the client hangs and cannot get the complete output. The vLLM service itself does not crash. Re-sending the prompt (with priority) or opening a new chat can continue inference, but the same issue occurs again quickly. **Steps to Reproduce:** 1. Start vLLM service (configuration as above) 2. Send a chat request via Open WebUI 3. Model starts generating output, but stops mid-way 4. Client cannot get complete...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: Qwen3.5-35B-A3B-FP8 inference output terminates unexpectedly, logs show normal but request hangs **Environment:** - vLLM version: 0.17+ (CUDA 130) - Model: Qwen/Qwen3.5-35B-A3B-FP8 - GPU: RTX 5090D × 2 - Open Web...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: B-A3B-FP8 inference output terminates unexpectedly, logs show normal but request hangs **Environment:** - vLLM version: 0.17+ (CUDA 130) - Model: Qwen/Qwen3.5-35B-A3B-FP8 - GPU: RTX 5090D × 2 - Open WebUI version: 0.8.1...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3.5-35B-A3B-FP8 inference output terminates unexpectedly, logs show normal but request hangs **Environment:** - vLLM version: 0.17+ (CUDA 130) - Model: Qwen/Qwen3.5-35B-A3B-FP8 - GPU: RTX 5090D × 2 - Open Web...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: continue inference, but the same issue occurs again quickly. **Steps to Reproduce:** 1. Start vLLM service (configuration as above) 2. Send a chat request via Open WebUI 3. Model starts generating output, but stops mid-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: gs show normal but request hangs **Environment:** - vLLM version: 0.17+ (CUDA 130) - Model: Qwen/Qwen3.5-35B-A3B-FP8 - GPU: RTX 5090D × 2 - Open WebUI version: 0.8.10 - Launch command: ```bash python3 -m vllm.entrypoint...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
