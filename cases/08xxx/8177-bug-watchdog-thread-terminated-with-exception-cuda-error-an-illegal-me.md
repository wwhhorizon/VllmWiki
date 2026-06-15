# vllm-project/vllm#8177: [Bug]: watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#8177](https://github.com/vllm-project/vllm/issues/8177) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered

### Issue 正文摘录

### Your current environment Environemnt summary: **vLLM 0.5.5** docker on **4xH100 SXM** Model summary: Llama 3 70B in fp8 using AutoFP8 Runtime summary: ``` --gpu-memory-utilization=0.95 --tensor-parallel-size=4 --disable-log-requests --enable-chunked-prefill --max-num-batched-tokens=8192 ``` ``` INFO 09-03 19:10:35 config.py:813] Defaulting to use mp for distributed inference INFO 09-03 19:10:35 config.py:911] Chunked prefill is enabled with max_num_batched_tokens=8192. INFO 09-03 19:10:35 llm_engine.py:184] Initializing an LLM engine (v0.5.5) with config: model='/model', speculative_config=None, tokenizer='/model', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=8192, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=4, pipeline_parallel_size=1, disable_custom_all_reduce=False, quantization=fp8, enforce_eager=False, kv_cache_dtype=auto, quantization_param_path=None, device_config=cuda, decoding_config=DecodingConfig(guided_decoding_backend='outlines'), observability_config=ObservabilityConfig(otlp_traces_endpoint=None, collec...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: y: **vLLM 0.5.5** docker on **4xH100 SXM** Model summary: Llama 3 70B in fp8 using AutoFP8 Runtime summary: ``` --gpu-memory-utilization=0.95 --tensor-parallel-size=4 --disable-log-requests --enable-chunked-prefill --ma...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: with exception: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment Environemnt summary: **vLLM 0.5.5** docker on **4xH100 SXM** Model summary: Llama 3 70B in fp8 using AutoFP8 Ru...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ale ### Your current environment Environemnt summary: **vLLM 0.5.5** docker on **4xH100 SXM** Model summary: Llama 3 70B in fp8 using AutoFP8 Runtime summary: ``` --gpu-memory-utilization=0.95 --tensor-parallel-size=4 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered bug;stale ### Your current environment Environemnt summary: **vLLM 0.5.5** docker on **4xH100 SXM** Model summary: L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ronment Environemnt summary: **vLLM 0.5.5** docker on **4xH100 SXM** Model summary: Llama 3 70B in fp8 using AutoFP8 Runtime summary: ``` --gpu-memory-utilization=0.95 --tensor-parallel-size=4 --disable-log-requests --e...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | (0x7f8d66005609 in /usr/lib/x86_64-linux-gnu/libpthread.so.0) frame #4: clone + 0x43 (0x7f8d6613f353 in /usr/lib/x86_64-linux-gnu/libc.so.6) [rank2]:[e904 19:47:16.699524824 pro |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #6: c10d::processgroupnccl::ncclcommwatchdog() + 0x10c (0x7f8d160936fc in /usr/local/lib/python3.10/dist-packa… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #7: <unknown function> + 0xd6df4 (0x7f8d6381fdf4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #8: <unknow |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
