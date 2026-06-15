# vllm-project/vllm#37250: [Bug]: QWEN 3.5-397B-A17B report "RPC call to sample_tokens timed out"

| 字段 | 值 |
| --- | --- |
| Issue | [#37250](https://github.com/vllm-project/vllm/issues/37250) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: QWEN 3.5-397B-A17B report "RPC call to sample_tokens timed out"

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran vllm on docker, and docker run command: ``` docker run --gpus '"device=0,1,2,3"' -d \ --name vllm-ray-test-4gpu-shm \ --ipc=host \ --network=host \ -v /home/test/vllm:/vllm/ \ --entrypoint /bin/bash \ vllm-qwen3.5:latest \ -c "while true; do sleep 30; done" ``` My vllm parameter (TP=4): ``` results = ds.map_batches( vLLMEngineActor, fn_constructor_kwargs={ "model": "/pfs/mahaocong/vllm/Qwen3.5-397B-A17B-FP8", "model_id": "Qwen3.5-397B-A17B-FP8", "column_name": "messages", "output_column": "text", "llm_kwargs": {"tensor_parallel_size": 4, "max_model_len": 2048, "load_format": "fastsafetensors", "enforce_eager": True}, "chat_template_kwargs": {"enable_thinking": False}, "sampling_params_kwargs": {}, }, compute=ray.data.ActorPoolStrategy(size=1), batch_size=1000, num_gpus=4, ) ``` I am trying to debug the problem by opening export CUDA_LAUNCH_BLOCKING=1, and the exception stack caught is as follows: py-spy WORKER stack: ``` Thread 896733 (active): "MainThread" gdn_prefill (flashinfer/gdn_prefill.py:63) chunk_gated_delta_rule (flashinfer/gdn_prefill.py:196) fi_chunk_gated_delta_rule (vllm/model_executor/models/qwen3_next.py:138...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: WORKER stack: ``` Thread 896733 (active): "MainThread" gdn_prefill (flashinfer/gdn_prefill.py:63) chunk_gated_delta_rule (flashinfer/gdn_prefill.py:196) fi_chunk_gated_delta_rule (vllm/model_executor/models/qwen3_next.p...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: ug ### Your current environment ### 🐛 Describe the bug I ran vllm on docker, and docker run command: ``` docker run --gpus '"device=0,1,2,3"' -d \ --name vllm-ray-test-4gpu-shm \ --ipc=host \ --network=host \ -v /home/t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: s: py-spy WORKER stack: ``` Thread 896733 (active): "MainThread" gdn_prefill (flashinfer/gdn_prefill.py:63) chunk_gated_delta_rule (flashinfer/gdn_prefill.py:196) fi_chunk_gated_delta_rule (vllm/model_executor/models/qw...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: tructor_kwargs={ "model": "/pfs/mahaocong/vllm/Qwen3.5-397B-A17B-FP8", "model_id": "Qwen3.5-397B-A17B-FP8", "column_name": "messages", "output_column": "text", "llm_kwargs": {"tensor_parallel_size": 4, "max_model_len":...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: num_gpus=4, ) ``` I am trying to debug the problem by opening export CUDA_LAUNCH_BLOCKING=1, and the exception stack caught is as follows: py-spy WORKER stack: ``` Thread 896733 (active): "MainThread" gdn_prefill (flash...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 00007f783bad2c04 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #4 0x00007f783b9e2ccc in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #5 0x00007f783ba08ce2 in ?? () from |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | 00007f783ba08ce2 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #6 0x00007f783ba145d5 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #7 0x00007f783c771b3d in ?? () from |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 00007f783ba145d5 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #7 0x00007f783c771b3d in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #8 0x00007f783b980ad5 in ?? () from |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | 00007f783bb60990 in ?? () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #12 0x00007f783bb54760 in culaunchkernelex () from /usr/lib/x86_64-linux-gnu/libcuda.so.1 #13 0x00007f787a414… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | s/flashinfer_jit_cache/jit_cache/gdn_prefill_sm90/gdn_prefill_sm90.so #16 0x00007f592c0a7003 in flashinfer::gdn_prefill_launcher(void*, void*, void*, void*, void*, void*, void*, v… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | rom /usr/local/lib/python3.12/dist-packages/tvm_ffi/lib/libtvm_ffi.so #20 0x00007f74ac44bfec in ?? () from /usr/local/lib/python3.12/dist-packages/tvm_ffi/lib/libtvm_ffi.so #21 0x… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | rom /usr/local/lib/python3.12/dist-packages/tvm_ffi/lib/libtvm_ffi.so #21 0x00007f76f0274914 in ?? () from /usr/local/lib/python3.12/dist-packages/tvm_ffi/core.abi3.so ``` this bl… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
