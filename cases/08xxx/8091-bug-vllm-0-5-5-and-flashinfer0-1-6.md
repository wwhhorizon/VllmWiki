# vllm-project/vllm#8091: [Bug]: vLLM 0.5.5 and FlashInfer0.1.6

| 字段 | 值 |
| --- | --- |
| Issue | [#8091](https://github.com/vllm-project/vllm/issues/8091) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vLLM 0.5.5 and FlashInfer0.1.6

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when i use vLLm0.5.5 and FlashInfer0.1.6 to run Gemma-2-2b in T4. FlashInfer0.1.6 support T4: https://github.com/flashinfer-ai/flashinfer/releases but i see： ```python INFO 09-02 16:07:55 model_runner.py:890] Loading model weights took 4.8999 GB Process SpawnProcess-1: Traceback (most recent call last): File "/opt/conda/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/opt/conda/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/openai/rpc/server.py", line 230, in run_rpc_server server = AsyncEngineRPCServer(async_engine_args, usage_context, rpc_path) File "/opt/conda/lib/python3.10/site-packages/vllm/entrypoints/openai/rpc/server.py", line 31, in __init__ self.engine = AsyncLLMEngine.from_engine_args( File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 740, in from_engine_args engine = cls( File "/opt/conda/lib/python3.10/site-packages/vllm/engine/async_llm_engine.py", line 636, in __init__ self.engine = self._init_engine(*args, **kwargs) File "/op...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: vLLM 0.5.5 and FlashInfer0.1.6 bug;stale ### Your current environment ### 🐛 Describe the bug when i use vLLm0.5.5 and FlashInfer0.1.6 to run Gemma-2-2b in T4. FlashInfer0.1.6 support T4: https://github.com/flashi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: out, q, k, v, out_padded, softmax_lse, S_dmask, rng_state = flash_attn_cuda.varlen_fwd( RuntimeError: FlashAttention only supports Ampere GPUs or newer. ``` I'm not sure if it's a problem with vLLM's integration with Fl...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: in _initialize_kv_caches self.model_executor.determine_num_available_blocks()) File "/opt/conda/lib/python3.10/site-packages/vllm/executor/gpu_executor.py", line 113, in determine_num_available_blocks return self.driver...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ### 🐛 Describe the bug when i use vLLm0.5.5 and FlashInfer0.1.6 to run Gemma-2-2b in T4. FlashInfer0.1.6 support T4: https://github.com/flashinfer-ai/flashinfer/releases but i see： ```python INFO 09-02 16:07:55 model_ru...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: r.py", line 222, in determine_num_available_blocks self.model_runner.profile_run() File "/opt/conda/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) Fi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
