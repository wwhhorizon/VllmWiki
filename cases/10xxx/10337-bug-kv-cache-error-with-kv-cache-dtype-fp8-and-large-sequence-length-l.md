# vllm-project/vllm#10337: [Bug]: KV Cache Error with KV_cache_dtype=FP8 and Large Sequence Length: Losing Context Length of Model

| 字段 | 值 |
| --- | --- |
| Issue | [#10337](https://github.com/vllm-project/vllm/issues/10337) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KV Cache Error with KV_cache_dtype=FP8 and Large Sequence Length: Losing Context Length of Model

### Issue 正文摘录

### 🐛 Describe the bug When I serve llama3.1-70B quantized w4a16, with the following parameters: 1. --max-model-len: 127728 2. --enable-prefix-caching: True 3. --enable-chunked-prefill: False 4. --kv-cache-dtype: fp8_e4m3 5. VLLM_ATTENTION_BACKEND: FLASHINFER I have the following error: ``` Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/usr/lib/python3.12/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 388, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 138, in from_engine_args return cls( ^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/multiprocessing/engine.py", line 78, in __init__ self.engine = LLMEngine(*args, ^^^^^^^^^^^^^^^^ File "/usr/local/lib/python3.12/dist-packages/vllm/engine/llm_engine.py", line 339, in __init__ self._initialize_kv_caches() F...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e-chunked-prefill: False 4. --kv-cache-dtype: fp8_e4m3 5. VLLM_ATTENTION_BACKEND: FLASHINFER I have the following error: ``` Process SpawnProcess-1: Traceback (most recent call last): File "/usr/lib/python3.12/multiproc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: KV Cache Error with KV_cache_dtype=FP8 and Large Sequence Length: Losing Context Length of Model bug;stale ### 🐛 Describe the bug When I serve llama3.1-70B quantized w4a16, with the following parameters: 1. --max...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Bug]: KV Cache Error with KV_cache_dtype=FP8 and Large Sequence Length: Losing Context Length of Model bug;stale ### 🐛 Describe the bug When I serve llama3.1-70B quantized w4a16, with the following parameters: 1. --max...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: : 127728 2. --enable-prefix-caching: True 3. --enable-chunked-prefill: False 4. --kv-cache-dtype: fp8_e4m3 5. VLLM_ATTENTION_BACKEND: FLASHINFER I have the following error: ``` Process SpawnProcess-1: Traceback (most re...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: h KV_cache_dtype=FP8 and Large Sequence Length: Losing Context Length of Model bug;stale ### 🐛 Describe the bug When I serve llama3.1-70B quantized w4a16, with the following parameters: 1. --max-model-len: 127728 2. --e...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
