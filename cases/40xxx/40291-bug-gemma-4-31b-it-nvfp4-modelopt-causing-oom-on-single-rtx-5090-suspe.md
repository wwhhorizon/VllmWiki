# vllm-project/vllm#40291: [Bug]:  Gemma-4-31B-IT-NVFP4  (modelopt) causing OOM on single RTX 5090, suspect full BF16 weights during init

| 字段 | 值 |
| --- | --- |
| Issue | [#40291](https://github.com/vllm-project/vllm/issues/40291) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;gemm;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  Gemma-4-31B-IT-NVFP4  (modelopt) causing OOM on single RTX 5090, suspect full BF16 weights during init

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When trying to run ```python vllm run --model nvidia/Gemma-4-31B-IT-NVFP4 --quantization modelopt --max-model-len 8192 ``` I get an OOM error during create_weights() initialization. At the time of crash, PyTorch has already allocated 29,39 GiB, far exceeding what a 31B model at true NVFP4 should require (~15-16 GiB). The weights appear to be allocated at a much higher precision (maybe BF16?, I'm however not experienced enough to say this with certainty) rather than at their quantized size. **Crash location** linear.py:201 create_weights() → torch.empty(...) ← OOM here ← RowParallelLinear.__init__ (linear.py:1436) [o_proj] ← Gemma4Attention.__init__ (gemma4.py:309) ← Gemma4DecoderLayer.__init__ (gemma4.py:472) ← Gemma4Model.__init__ / make_layers (gemma4.py:931) **Key error** torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 84.00 MiB. GPU 0 has a total capacity of 31.35 GiB of which 93.06 MiB is free. Including non-PyTorch memory, this process has 30.33 GiB memory in use. Of the allocated memory 29.39 GiB is allocated by PyTorch. **Expected behavior** The 31B NVFP4 model should allocate approximately 15-16 GiB of weig...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 8: [Bug]: Gemma-4-31B-IT-NVFP4 (modelopt) causing OOM on single RTX 5090, suspect full BF16 weights during init bug ### Your current environment ### 🐛 Describe the bug When trying to run ```python vllm run --model nvidia/G...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ire (~15-16 GiB). The weights appear to be allocated at a much higher precision (maybe BF16?, I'm however not experienced enough to say this with certainty) rather than at their quantized size. **Crash location**
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: rectly identifies the quantization as modelopt_fp4 and selects vFp4LinearBackend.FLASHINFER_CUTLASS for NVFP4 GEMM — the OOM happens in weight allocation before any inference * tensor_parallel_size=1 (single GPU)
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 6: equire (~15-16 GiB). The weights appear to be allocated at a much higher precision (maybe BF16?, I'm however not experienced enough to say this with certainty) rather than at their quantized size. **Crash location**
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma-4-31B-IT-NVFP4 (modelopt) causing OOM on single RTX 5090, suspect full BF16 weights during init bug ### Your current environment ### 🐛 Describe the bug When trying to run ```python vllm run --model nvidia/Ge

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
