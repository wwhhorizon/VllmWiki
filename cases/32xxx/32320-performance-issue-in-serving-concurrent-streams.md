# vllm-project/vllm#32320: [Performance]: Issue in serving concurrent streams

| 字段 | 值 |
| --- | --- |
| Issue | [#32320](https://github.com/vllm-project/vllm/issues/32320) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: Issue in serving concurrent streams

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance I am serving a TTS model based on **Qwen 2.5** using **vLLM** and I am seeing very inconsistent behavior in how it handles concurrency and RTF. **Setup** * TTS model size: 500M * GPU: L40S * vLLM via Python API **Engine args** ```python engine_args = AsyncEngineArgs( model=outetts_cache, tokenizer=outetts_cache, tokenizer_mode="auto", tensor_parallel_size=1, max_model_len=2048, gpu_memory_utilization=0.9, disable_log_stats=True, max_num_batched_tokens=2048, dtype="float16", kv_cache_dtype="fp8_e4m3", enable_prefix_caching=True, enable_chunked_prefill=True, max_num_seqs=50, ) ``` **End-to-end TTS pipeline** The full serving pipeline is: * prompt preparation * vLLM inference * wav tokenizer to convert tokens into audio **What I observed** I started with 10 concurrent requests and increased by 10 up to 50. * 10 → OK * 20 → OK * 30 → OK * 40 → RTF 1 for ~60% of the requests After this point I was no longer able to reliably serve 40 concurrent requests even though it worked earlier with the same configuration. The concurrency handling becomes highly in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ========= OS : Ubuntu 22.04.3 LTS (x86_64) GCC version : (Ubuntu 11.4.0-1ubuntu1~22.04.2) 11.4.0 Clang version : 14.0.0-1ubuntu1.1 CMake version : Could not collect Libc version : glibc-2.35 ============
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: version : 2.8.0+cu128 Is debug build : False CUDA used to build PyTorch : 12.8 ROCM used to build PyTorch : N/A ============================== Python Environment ============================== Python version : 3.11.5 (m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: on=0.9, disable_log_stats=True, max_num_batched_tokens=2048, dtype="float16", kv_cache_dtype="fp8_e4m3", enable_prefix_caching=True, enable_chunked_prefill=True, max_num_seqs=50, ) ``` **End-to-end TTS pipeline** The fu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: n _No response_ ### Misc discussion on performance I am serving a TTS model based on **Qwen 2.5** using **vLLM** and I am seeing very inconsistent behavior in how it handles concurrency and RTF. **Setup** * TTS model si...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: === Versions of relevant libraries ============================== [pip3] flashinfer-python==0.6.0 [pip3] numpy==2.2.6 [pip3] nvidia-cublas-cu12==12.8.4.1 [pip3] nvidia-cuda-cupti-cu12==12.8.90 [pip3] nvidia-cuda-nvrtc-c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
