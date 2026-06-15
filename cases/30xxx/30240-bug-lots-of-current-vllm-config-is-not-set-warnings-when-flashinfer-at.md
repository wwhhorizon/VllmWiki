# vllm-project/vllm#30240: [Bug]: Lots of "Current vLLM config is not set." warnings when FlashInfer attention is used

| 字段 | 值 |
| --- | --- |
| Issue | [#30240](https://github.com/vllm-project/vllm/issues/30240) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Lots of "Current vLLM config is not set." warnings when FlashInfer attention is used

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Lots of "Current vLLM config is not set." warnings when FlashInfer attention is used. This is caused by https://github.com/vllm-project/vllm/pull/26315 my command on H200: ``` python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3-32B-FP8 --kv-cache-dtype auto --attention-config.backend FLASHINFER ``` Warnings: ``` (EngineCore_DP0 pid=3978) INFO 12-07 21:28:40 [kernel_warmup.py:65] Warming up FlashInfer attention. (EngineCore_DP0 pid=3978) WARNING 12-07 21:28:41 [vllm.py:1375] Current vLLM config is not set. (EngineCore_DP0 pid=3978) INFO 12-07 21:28:41 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. (EngineCore_DP0 pid=3978) WARNING 12-07 21:28:41 [attention.py:82] Using VLLM_ATTENTION_BACKEND environment variable is deprecated and will be removed in v0.14.0 or v1.0.0, whichever is soonest. Please use --atte ntion-config.backend command line argument or AttentionConfig(backend=...) config field instead. Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 51/51...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Lots of "Current vLLM config is not set." warnings when FlashInfer attention is used bug ### Your current environment ### 🐛 Describe the bug Lots of "Current vLLM config is not set." warnings when FlashInfer atte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: t vLLM config is not set. (EngineCore_DP0 pid=3978) INFO 12-07 21:28:41 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. (EngineCore_DP0 pid=3978) WARNING 12-07 21:28:41 [attention.py:82]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: Lots of "Current vLLM config is not set." warnings when FlashInfer attention is used bug ### Your current environment ### 🐛 Describe the bug Lots of "Current vLLM config is not set." warnings when FlashInfer atte...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ``` python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3-32B-FP8 --kv-cache-dtype auto --attention-config.backend FLASHINFER ``` Warnings: ``` (EngineCore_DP0 pid=3978) INFO 12-07 21:28:40 [kernel_warmup.py:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: argument or AttentionConfig(backend=...) config field instead. Capturing CUDA graphs (mixed prefill-decode, PIECEWISE): 100%|██████████████████████████████████████████████████████████████████████████████████████████████...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
