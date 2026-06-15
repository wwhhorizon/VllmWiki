# vllm-project/vllm#28028: [Bug]: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.

| 字段 | 值 |
| --- | --- |
| Issue | [#28028](https://github.com/vllm-project/vllm/issues/28028) |
| 状态 | open |
| 标签 | bug;unstale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;kernel;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.

### Issue 正文摘录

### Your current environment server.log ``` [rank1]:[E1103 23:14:03.342459398 ProcessGroupNCCL.cpp:2068] [PG ID 4 PG GUID 19 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was encountered CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAException.cpp:42 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::allocator >) + 0x80 (0x7f35d56d9eb0 in /opt/venv/lib/python3.12/site-packages/torch/lib/libc10.so) frame #1: + 0x111c7 (0x7f35d576c1c7 in /opt/venv/lib/python3.12/site-packages/torch/lib/libc10_cuda.so) frame #2: c10d::ProcessGroupNCCL::WorkNCCL::finishedGPUExecutionInternal() const + 0x50 (0x7f3578cc4640 in /opt/venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #3: c10d::ProcessGroupNCCL::WorkNCCL::isCompleted() + 0x68 (0x7f3578cd3e28 in /opt/venv/lib/python3.12/site-packages/torch/lib/l...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 8: t some other API call, so the stacktrace below might be incorrect. bug;unstale ### Your current environment server.log ``` [rank1]:[E1103 23:14:03.342459398 ProcessGroupNCCL.cpp:2068] [PG ID 4 PG GUID 19 Rank 1] Process...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ight be incorrect. For debugging consider passing CUDA_LAUNCH_BLOCKING=1 Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. Exception raised from c10_cuda_check_implementation at /pytorch/c10/cuda/CUDAE...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: e=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=65536, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=4, data_parallel_size...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 4 [dump_input.py:69] Dumping input data for V1 LLM engine (v0.11.0) with config: model='Llama-3.1-Nemotron-70B-Instruct-HF', speculative_config=None, tokenizer='Llama-3.1-Nemotron-70B-Instruct-HF', skip_tokenizer_init=F...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: gnu/libc.so.6) terminate called after throwing an instance of 'c10::DistBackendError' what(): [PG ID 4 PG GUID 19 Rank 1] Process group watchdog thread terminated with exception: CUDA error: an illegal memory access was...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | b4 (0x7f355c601db4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #4: <unknown function> + 0x9caa4 (0x7f35d668caa4 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #5: <unknown f… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | t/venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xecdb4 (0x7f355c601db4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unkn… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | b4 (0x7f355c601db4 in /usr/lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x9caa4 (0x7f35d668caa4 in /usr/lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
