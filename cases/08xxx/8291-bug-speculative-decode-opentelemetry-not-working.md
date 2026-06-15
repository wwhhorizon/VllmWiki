# vllm-project/vllm#8291: [Bug]: Speculative Decode + OpenTelemetry not working

| 字段 | 值 |
| --- | --- |
| Issue | [#8291](https://github.com/vllm-project/vllm/issues/8291) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Speculative Decode + OpenTelemetry not working

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Launch the server with otel option followed by https://github.com/vllm-project/vllm/blob/main/examples/production_monitoring/Otel.md **I confirm that the error occurred with the vllm main branch, as well as versions v0.5.4, v0.5.5, and v0.6.0. Furthermore, no error occured without speculative decoding when using otel tracing in these versions.** A minimal reproducible script ``` vllm serve facebook/opt-125m --speculative-model facebook/opt-125m --num-speculative-tokens 3 --use-v2-block-manager --otlp-traces-endpoint grpc://******* ``` Then test with script https://github.com/vllm-project/vllm/blob/main/examples/production_monitoring/dummy_client.py ``` python3 dummy_client.py ``` Highlight information should be ``` Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/openai/rpc/server.py", line 115, in generate async for request_output in results_generator: File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line 1073, in generate async for output in await self.add_request( File "/usr/local/lib/python3.10/dist-packages/vllm/engine/async_llm_engine.py", line...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: Speculative Decode + OpenTelemetry not working bug;stale ### Your current environment ### 🐛 Describe the bug Launch the server with otel option followed by https://github.com/vllm-project/vllm/blob/main/examples/...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: *I confirm that the error occurred with the vllm main branch, as well as versions v0.5.4, v0.5.5, and v0.6.0. Furthermore, no error occured without speculative decoding when using otel tracing in these versions.** A min...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nimal reproducible script ``` vllm serve facebook/opt-125m --speculative-model facebook/opt-125m --num-speculative-tokens 3 --use-v2-block-manager --otlp-traces-endpoint grpc://******* ``` Then test with script https://...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ` terminate called after throwing an instance of 'c10::Error' what(): CUDA error: device-side assert triggered Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_imp...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: er_memory;speculative_decoding cache;cuda;operator;quantization;sampling;triton build_error;crash;slowdown env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure K...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | local/lib/python3.10/dist-packages/torch/lib/libtorch_cuda.so) frame #4: <unknown function> + 0x1033f1d (0x7fc5fd233f1d in /usr/local/lib/python3.10/dist-packages/torch/lib/libtor… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | cal/lib/python3.10/dist-packages/torch/lib/libtorch_python.so) frame #6: <unknown function> + 0x6abdf (0x7fc6498afbdf in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.s… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n /usr/local/lib/python3.10/dist-packages/torch/lib/libc10.so) frame #7: c10::tensorimpl::~tensorimpl() + 0x21b (0x7fc6498a8c3b in /usr/local/lib/python3.10/dist-packages/torch/li… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | /libtorch_python.so) frame #11: /usr/bin/python3() [0x601db4] frame #12: /usr/bin/python3() [0x5e4183] frame #13: /usr/bin/python3() [0x601db4] frame #14: /usr/bin/python3() [0x5e |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | python3() [0x5e0e90] frame #15: /usr/bin/python3() [0x5842fe] frame #16: /usr/bin/python3() [0x6b1bee] frame #17: pygc_collect + 0x67 (0x6b1c87 in /usr/bin/python3) frame #18: py_ |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | hon3) frame #19: py_exit + 0xc (0x6c09fc in /usr/bin/python3) frame #20: /usr/bin/python3() [0x6c0a2f] frame #21: pyerr_printex + 0x16 (0x6c0a56 in /usr/bin/python3) frame #22: py |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | in /usr/bin/python3) frame #20: /usr/bin/python3() [0x6c0a2f] frame #21: pyerr_printex + 0x16 (0x6c0a56 in /usr/bin/python3) frame #22: pyrun_simplestringflags + 0x52 (0x6c0ac2 in |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
