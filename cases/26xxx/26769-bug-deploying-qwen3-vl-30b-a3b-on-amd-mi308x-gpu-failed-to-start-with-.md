# vllm-project/vllm#26769: [Bug]: deploying Qwen3-VL-30B-A3B on AMD MI308X GPU, failed to start with worker process dying unexpectedly after loading weights

| 字段 | 值 |
| --- | --- |
| Issue | [#26769](https://github.com/vllm-project/vllm/issues/26769) |
| 状态 | closed |
| 标签 | bug;rocm;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | cuda;gemm;kernel;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: deploying Qwen3-VL-30B-A3B on AMD MI308X GPU, failed to start with worker process dying unexpectedly after loading weights

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Before deploying Qwen3-VL-30B-A3B, we have successed to deploy the text-only QWen3-30B-A3B. We can successfully run inference with it on both single AMD-GPU and multi AMD-GPUs (tensor parallel) setups. **Script:** ```shell CUDA_VISIBLE_DEVICES=0,1,2,3 python3 -m vllm.entrypoints.openai.api_server \ --host localhost \ --port 6324 \ --tensor-parallel-size 4 \ --mm-encoder-tp-mode data \ --async-scheduling \ --limit-mm-per-prompt.video 0 \ --max-model-len 128000 \ --gpu-memory-utilization 0.6 \ --model /home/admin/HF/Qwen3-VL-30B-A3B \ --dtype bfloat16 ``` **Log:** ```text (APIServer pid=232103) DEBUG 10-14 13:41:48 [v1/engine/utils.py:862] Waiting for 1 local, 0 remote core engine proc(s) to start. Loading safetensors checkpoint shards: 92% Completed | 12/13 [00:18 , std::allocator >) + 0x88 (0x7fb9470fc6e8 in /home/admin/.local/lib/python3.10/site-packages/torch/lib/libc10.so) frame #1: + 0x5cdccbe (0x7fb9366dccbe in /home/admin/.local/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #2: + 0x5cddc20 (0x7fb9366ddc20 in /home/admin/.local/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #3: + 0x5cde399 (0x7...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: nst&, pybind11::args const&, pybind11::kwargs const&, std::optional[c10::DispatchKey](https://www.google.com/url?sa=E&q=c10%3A%3ADispatchKey)) + 0xef (0x7fb946169fef in /home/admin/.local/lib/python3.10/site-packages/to...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: o start with worker process dying unexpectedly after loading weights bug;rocm;stale ### Your current environment ### 🐛 Describe the bug Before deploying Qwen3-VL-30B-A3B, we have successed to deploy the text-only QWen3-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: deploying Qwen3-VL-30B-A3B on AMD MI308X GPU, failed to start with worker process dying unexpectedly after loading weights bug;rocm;stale ### Your current environment ### 🐛 Describe the bug Before deploying Qwen3...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: rt with worker process dying unexpectedly after loading weights bug;rocm;stale ### Your current environment ### 🐛 Describe the bug Before deploying Qwen3-VL-30B-A3B, we have successed to deploy the text-only QWen3-30B-A...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ", line 1930, in run_server_worker (APIServer pid=232103) async with build_async_engine_client( (APIServer pid=232103) File "/opt/conda/envs/python3.10/lib/python3.10/contextlib.py", line 199, in aenter (APIServer pid=2...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | /.local/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.local/lib/python3.10/site-packages/torch/lib/libtorch_hip.so) frame #6: <unknown function> + 0xdbbf4 (0x7f143e0dbbf4 in /opt/conda/envs/python3.10.13/bin/../lib/libstdc++.so.6)… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | bf4 in /opt/conda/envs/python3.10.13/bin/../lib/libstdc++.so.6) frame #7: <unknown function> + 0x93fb (0x7f149925b3fb in /lib64/libpthread.so.0) frame #8: clone + 0x43 (0x7f1498f5… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | /.local/lib/python3.10/site-packages/torch/lib/libtorch_hip.so) frame #12: c10d::processgroupnccl::initncclcomm(std::__cxx11::basic_string<char, std::char_traits<char>, std::alloc… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | /.local/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #16: <unknown function> + 0x5c9fd20 (0x7f027309fd20 in /home/admin/.local/lib/python3.10/site-packages/torch/… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | ib/libtorch_python.so) frame #19: vllm::worker_tp3() [0x4fc697] frame #20: _pyobject_maketpcall + 0x25b (0x4f614b in vllm::worker_tp3) frame #21: vllm::worker_tp3() [0x50819f] fra… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | 20: _pyobject_maketpcall + 0x25b (0x4f614b in vllm::worker_tp3) frame #21: vllm::worker_tp3() [0x50819f] frame #22: _pyeval_evalframedefault + 0x4b26 (0x4f1ac6 in vllm::worker_tp3… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 6: _pyfunction_vectorcall + 0x6f (0x4fcadf in vllm::worker_tp3) frame #27: _pyeval_evalframedefault + 0x13b3 (0x4ee353 in vllm::worker_tp3) frame #28: _pyfunction_vectorcall + 0x6… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 8: _pyfunction_vectorcall + 0x6f (0x4fcadf in vllm::worker_tp3) frame #29: _pyeval_evalframedefault + 0x731 (0x4ed6d1 in vllm::worker_tp3) frame #30: _pyfunction_vectorcall + 0x6f… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | _pyeval_evalframedefault + 0x731 (0x4ed6d1 in vllm::worker_tp3) frame #32: _pyfunction_vectorcall + 0x6f (0x4fcadf in vllm::worker_tp3) frame #33: <unknown function> + 0x8b986a (0… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | pyeval_evalframedefault + 0x13b3 (0x4ee353 in vllm::worker_tp3) frame #53: _pyfunction_vectorcall + 0x6f (0x4fcadf in vllm::worker_tp3) frame #54: _pyeval_evalframedefault + 0x13b… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
