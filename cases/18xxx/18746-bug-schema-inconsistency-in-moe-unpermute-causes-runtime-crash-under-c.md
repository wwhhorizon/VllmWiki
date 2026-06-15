# vllm-project/vllm#18746: [Bug]:  Schema inconsistency in moe_unpermute causes runtime crash under CUDA 11.8

| 字段 | 值 |
| --- | --- |
| Issue | [#18746](https://github.com/vllm-project/vllm/issues/18746) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;moe;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;moe;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]:  Schema inconsistency in moe_unpermute causes runtime crash under CUDA 11.8

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug After successfully compiling and building with cuda11.8, I run " vllm" command, then it crashed with the following output ```bash INFO 05-26 23:11:48 [__init__.py:248] Automatically detected platform cuda. terminate called after throwing an instance of 'c10::Error' what(): Inferred operator schema for a C++ kernel function doesn't match the expected function schema. operator: _moe_C::moe_unpermute expected schema: _moe_C::moe_unpermute(Tensor permuted_hidden_states, Tensor topk_weights, Tensor topk_ids, Tensor src_row_id2dst_row_id_map, Tensor expert_first_token_offset, int n_expert, int n_local_expert, int topk, Tensor($0! -> ) hidden_states) -> () registered at /home/a001/02-projects/model-deploy/vllm/csrc/moe/torch_bindings.cpp:4 inferred schema: (Tensor _0, Tensor _1, Tensor _2, Tensor _3, Tensor? _4, int _5, int _6, int _7, int? _8, Tensor _9, Tensor _10, Tensor _11, Tensor _12) -> () registered at /home/a001/02-projects/model-deploy/vllm/csrc/moe/moe_permute_unpermute_op.cu:171 reason: The number of arguments is different. 9 vs 13. Exception raised from checkSchema at /pytorch/aten/src/ATen/core/dispatch/OperatorEntry.cpp:4...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: environment ### 🐛 Describe the bug After successfully compiling and building with cuda11.8, I run " vllm" command, then it crashed with the following output ```bash INFO 05-26 23:11:48 [__init__.py:248] Automatically de...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 5: [Bug]: Schema inconsistency in moe_unpermute causes runtime crash under CUDA 11.8 bug;stale ### Your current environment ### 🐛 Describe the bug After successfully compiling and building with cuda11.8, I run " vllm" comm...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: vs 13. Exception raised from checkSchema at /pytorch/aten/src/ATen/core/dispatch/OperatorEntry.cpp:45 (most recent call first): frame #0: c10::Error::Error(c10::SourceLocation, std::__cxx11::basic_string , std::allocato...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: inconsistency in moe_unpermute causes runtime crash under CUDA 11.8 bug;stale ### Your current environment ### 🐛 Describe the bug After successfully compiling and building with cuda11.8, I run " vllm" command, then it c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 284d17f4733 in /home/a001/.conda/envs/vllm/bin/python3.10) frame #21: _PyEval_EvalFrameDefault + 0x588c (0x6284d17e985c in /home/a001/.conda/envs/vllm/bin/python3.10) frame #22: _PyFunction_Vectorcall + 0x6c (0x6284d17f...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | vs/vllm/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10::dispatcher::registerimpl(c10::operatorname, std::optional<c10::dispatchkey>, c10::kernelfunction, st… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | vs/vllm/lib/python3.10/site-packages/torch/lib/libtorch_cpu.so) frame #6: <unknown function> + 0x2b6f6 (0x7ff5bde2b6f6 in /home/a001/02-projects/model-deploy/vllm/vllm/_moe_c.abi3… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | n /home/a001/02-projects/model-deploy/vllm/vllm/_moe_c.abi3.so) frame #7: <unknown function> + 0x647e (0x7ff6cee9647e in /lib64/ld-linux-x86-64.so.2) frame #8: <unknown function>… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | tion + 0x88 (0x7ff6ceb74a98 in /lib/x86_64-linux-gnu/libc.so.6) frame #12: <unknown function> + 0xe34e (0x7ff6cee9e34e in /lib64/ld-linux-x86-64.so.2) frame #13: <unknown function… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | rror + 0x33 (0x7ff6ceb74b63 in /lib/x86_64-linux-gnu/libc.so.6) frame #16: <unknown function> + 0x9012e (0x7ff6cea9012e in /lib/x86_64-linux-gnu/libc.so.6) frame #17: dlopen + 0x4… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | (0x6284d18bdf4e in /home/a001/.conda/envs/vllm/bin/python3.10) frame #20: <unknown function> + 0x13d733 (0x6284d17f4733 in /home/a001/.conda/envs/vllm/bin/python3.10) frame #21: _… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | (0x6284d17f4733 in /home/a001/.conda/envs/vllm/bin/python3.10) frame #21: _pyeval_evalframedefault + 0x588c (0x6284d17e985c in /home/a001/.conda/envs/vllm/bin/python3.10) frame #2… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | (0x6284d17f456c in /home/a001/.conda/envs/vllm/bin/python3.10) frame #27: _pyeval_evalframedefault + 0x30c (0x6284d17e42dc in /home/a001/.conda/envs/vllm/bin/python3.10) frame #28… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | (0x6284d17f456c in /home/a001/.conda/envs/vllm/bin/python3.10) frame #29: _pyeval_evalframedefault + 0x30c (0x6284d17e42dc in /home/a001/.conda/envs/vllm/bin/python3.10) frame #30… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | (0x6284d17e42dc in /home/a001/.conda/envs/vllm/bin/python3.10) frame #32: _pyfunction_vectorcall + 0x6c (0x6284d17f456c in /home/a001/.conda/envs/vllm/bin/python3.10) frame #33: <… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | (0x6284d18025db in /home/a001/.conda/envs/vllm/bin/python3.10) frame #53: pyimport_importmodulelevelobject + 0x84b (0x6284d1801efb in /home/a001/.conda/envs/vllm/bin/python3.10) f… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
