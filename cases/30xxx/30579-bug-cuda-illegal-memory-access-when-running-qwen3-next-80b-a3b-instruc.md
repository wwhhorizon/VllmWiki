# vllm-project/vllm#30579: [Bug]: CUDA Illegal Memory Access when running Qwen3-Next-80B-A3B-Instruct on 4xB200 GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#30579](https://github.com/vllm-project/vllm/issues/30579) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;kernel;moe;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA Illegal Memory Access when running Qwen3-Next-80B-A3B-Instruct on 4xB200 GPUs

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When setting the environment variable `VLLM_USE_FLASHINFER_MOE_FP16=1` when serving the Qwen3-Next-80B-A3B-Instruct model, an illegal memory access error occurs; without this environment variable, the command completes successfully. Command: `VLLM_USE_FLASHINFER_MOE_FP16=1 VLLM_ATTENTION_BACKEND=FLASHINFER vllm serve Qwen/Qwen3-Next-80B-A3B-Instruct -tp 4 --enable-expert-parallel --no-enable-prefix-caching --async-scheduling --compilation_config.max_cudagraph_capture_size 2048` Error message: ``` (Worker_TP1_EP1 pid=293528) INFO 12-12 11:53:05 [scheduler.py:228] Chunked prefill is enabled with max_num_batched_tokens=2048. Capturing CUDA graphs (decode, FULL): 99%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ | 82/83 [00:15 , std::allocator >) + 0x80 (0x115a100d1b80 in /home...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: ### 🐛 Describe the bug When setting the environment variable `VLLM_USE_FLASHINFER_MOE_FP16=1` when serving the Qwen3-Next-80B-A3B-Instruct model, an illegal memory access error occurs; without this environment variable,...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: emory Access when running Qwen3-Next-80B-A3B-Instruct on 4xB200 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug When setting the environment variable `VLLM_USE_FLASHINFER_MOE_FP16=1` when serving the...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CUDA Illegal Memory Access when running Qwen3-Next-80B-A3B-Instruct on 4xB200 GPUs bug;stale ### Your current environment ### 🐛 Describe the bug When setting the environment variable `VLLM_USE_FLASHINFER_MOE_FP16...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: ribe the bug When setting the environment variable `VLLM_USE_FLASHINFER_MOE_FP16=1` when serving the Qwen3-Next-80B-A3B-Instruct model, an illegal memory access error occurs; without this environment variable, the comma...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculativ...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | u/.venv/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | /.venv/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xecdb4 (0xf1218ed4db4 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown f… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | 0xecdb4 (0xf1218ed4db4 in /lib/x86_64-linux-gnu/libstdc++.so.6) frame #7: <unknown function> + 0x9caa4 (0xf1219c06aa4 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown functi… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
