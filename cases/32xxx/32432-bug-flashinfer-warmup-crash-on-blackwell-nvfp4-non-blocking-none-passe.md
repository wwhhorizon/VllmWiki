# vllm-project/vllm#32432: [Bug]: FlashInfer warmup crash on Blackwell NVFP4: non_blocking=None passed to Tensor.to()

| 字段 | 值 |
| --- | --- |
| Issue | [#32432](https://github.com/vllm-project/vllm/issues/32432) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: FlashInfer warmup crash on Blackwell NVFP4: non_blocking=None passed to Tensor.to()

### Issue 正文摘录

Summary: vLLM crashes during FlashInfer warmup on Blackwell (SM120) with NVFP4 models. The crash is caused by passing non_blocking=None to Tensor.to() under PyTorch 2.11+. Environment: - vLLM: 0.14.0rc2.dev85+g8c11001ba - PyTorch: 2.11+ - GPU: Blackwell (SM120), 32GB - Quantization: ModelOpt NVFP4 - Attention backend: FlashInfer - OS: Linux (WSL2) Command: python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8081 \ --model ~/.../Qwen3-Coder-30B-NVFP4 \ --served-model-name qwen3-coder-30b-nvfp4 \ --quantization modelopt \ --kv-cache-dtype fp8 \ --enable-expert-parallel \ --gpu-memory-utilization 0.85 \ --max-model-len 32768 \ --enable-prefix-caching \ --enforce-eager Error: TypeError: to() received an invalid combination of arguments - got (torch.device, non_blocking=NoneType) Stack trace: flashinfer/decode.py:948 vllm/v1/attention/backends/flashinfer.py Notes: - Model loads successfully. - Crash occurs during FlashInfer warmup. - VLLM_USE_V1=0 ignored on Blackwell NVFP4. - Not a memory issue. - Fully reproducible.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [Bug]: FlashInfer warmup crash on Blackwell NVFP4: non_blocking=None passed to Tensor.to() bug;stale Summary: vLLM crashes during FlashInfer warmup on Blackwell (SM120) with NVFP4 models. The crash is caused by passing...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [Bug]: FlashInfer warmup crash on Blackwell NVFP4: non_blocking=None passed to Tensor.to() bug;stale Summary: vLLM crashes during FlashInfer warmup on Blackwell (SM120) with NVFP4 models. The crash is caused by passing...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: FlashInfer warmup crash on Blackwell NVFP4: non_blocking=None passed to Tensor.to() bug;stale Summary: vLLM crashes during FlashInfer warmup on Blackwell (SM120) with NVFP4 models. The crash is caused by passing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: y: vLLM crashes during FlashInfer warmup on Blackwell (SM120) with NVFP4 models. The crash is caused by passing non_blocking=None to Tensor.to() under PyTorch 2.11+. Environment: - vLLM: 0.14.0rc2.dev85+g8c11001ba - PyT...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: up crash on Blackwell NVFP4: non_blocking=None passed to Tensor.to() bug;stale Summary: vLLM crashes during FlashInfer warmup on Blackwell (SM120) with NVFP4 models. The crash is caused by passing non_blocking=None to T...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
