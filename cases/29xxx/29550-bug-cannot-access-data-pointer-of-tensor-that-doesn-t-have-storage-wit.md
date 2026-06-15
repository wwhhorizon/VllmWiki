# vllm-project/vllm#29550: [Bug]: "Cannot access data pointer of Tensor that doesn't have storage" with B200 and flashinfer

| 字段 | 值 |
| --- | --- |
| Issue | [#29550](https://github.com/vllm-project/vllm/issues/29550) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: "Cannot access data pointer of Tensor that doesn't have storage" with B200 and flashinfer

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi. On my local build of vllm with pytorch nightly and B200 machine (w/ flashinfer backend), I saw some weird tensor ptr failure. (driver 570.124.06 with cuda 12.9) repro ``` vllm serve Qwen/Qwen3-8b ``` Running immediately into the following error: ``` (EngineCore_DP0 pid=698138) Process EngineCore_DP0: (EngineCore_DP0 pid=698138) Traceback (most recent call last): (EngineCore_DP0 pid=698138) File "/home/zhxchen17/.conda/envs/pytorch-3.12/lib/python3.12/multiprocessing/process.py", line 314, in _bootstrap (EngineCore_DP0 pid=698138) self.run() (EngineCore_DP0 pid=698138) File "/home/zhxchen17/.conda/envs/pytorch-3.12/lib/python3.12/multiprocessing/process.py", line 108, in run (EngineCore_DP0 pid=698138) self._target(*self._args, **self._kwargs) (EngineCore_DP0 pid=698138) File "/data/users/zhxchen17/vllm/vllm/v1/engine/core.py", line 846, in run_engine_core (EngineCore_DP0 pid=698138) raise e (EngineCore_DP0 pid=698138) File "/data/users/zhxchen17/vllm/vllm/v1/engine/core.py", line 833, in run_engine_core (EngineCore_DP0 pid=698138) engine_core = EngineCoreProc(*args, **kwargs) (EngineCore_DP0 pid=698138) ^^^^^^^^^^^^^^^^^^^^^^...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: t access data pointer of Tensor that doesn't have storage" with B200 and flashinfer bug ### Your current environment ### 🐛 Describe the bug Hi. On my local build of vllm with pytorch nightly and B200 machine (w/ flashin...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ### Your current environment ### 🐛 Describe the bug Hi. On my local build of vllm with pytorch nightly and B200 machine (w/ flashinfer backend), I saw some weird tensor ptr failure. (driver 570.124.06 with cuda 12.9) re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ]: "Cannot access data pointer of Tensor that doesn't have storage" with B200 and flashinfer bug ### Your current environment ### 🐛 Describe the bug Hi. On my local build of vllm with pytorch nightly and B200 machine (w...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: or ptr failure. (driver 570.124.06 with cuda 12.9) repro ``` vllm serve Qwen/Qwen3-8b ``` Running immediately into the following error: ``` (EngineCore_DP0 pid=698138) Process EngineCore_DP0: (EngineCore_DP0 pid=698138)...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: (0x516d1b in VLLM::EngineCore) (EngineCore_DP0 pid=698138) frame #8: _PyEval_EvalFrameDefault + 0x6ce (0x52105e in VLLM::EngineCore) (EngineCore_DP0 pid=698138) frame #9: + 0xae9eef (0x7f6ff6ce9eef in /data/users/zhxche...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | ch_c_dlpack_addon_torch210-cuda.so) (enginecore_dp0 pid=698138) frame #4: torchdlpackexchangeapi::managedtensorfrompyobjectnosync(void*, dlmanagedtensorversioned**) + 0x55 (0x7f6e… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | site-packages/tvm_ffi/core.abi3.so) (enginecore_dp0 pid=698138) frame #6: <unknown function> + 0x51b32 (0x7f6ebbae6b32 in /home/zhxchen17/.conda/envs/pytorch-3.12/lib/python3.12/s… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | site-packages/tvm_ffi/core.abi3.so) (enginecore_dp0 pid=698138) frame #7: _pyobject_maketpcall + 0x30b (0x516d1b in vllm::enginecore) (enginecore_dp0 pid=698138) frame #8: _pyeval… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | /pytorch/torch/lib/libtorch_cpu.so) (enginecore_dp0 pid=698138) frame #12: <unknown function> + 0xbb5cbb (0x7f6ff6db5cbb in /data/users/zhxchen17/pytorch/torch/lib/libtorch_python… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | torch/torch/lib/libtorch_python.so) (enginecore_dp0 pid=698138) frame #16: <unknown function> + 0x45bfc9 (0x7f6ff665bfc9 in /data/users/zhxchen17/pytorch/torch/lib/libtorch_python… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | 51fc (0x525b8c in vllm::enginecore) (enginecore_dp0 pid=698138) frame #20: _pyobject_fastcalldicttstate + 0x1e7 (0x519647 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #2… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | x1e7 (0x519647 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #21: _pyobject_call_prepend + 0xe0 (0x551d40 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #22: vllm… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 51fc (0x525b8c in vllm::enginecore) (enginecore_dp0 pid=698138) frame #27: vllm::enginecore() [0x56aed7] (enginecore_dp0 pid=698138) frame #28: _pyeval_evalframedefault + 0x51fc (… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 51fc (0x525b8c in vllm::enginecore) (enginecore_dp0 pid=698138) frame #29: vllm::enginecore() [0x56aed7] (enginecore_dp0 pid=698138) frame #30: _pyeval_evalframedefault + 0x51fc (… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | x1e7 (0x519647 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #32: _pyobject_call_prepend + 0xe0 (0x551d40 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #33: vllm… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | x1e7 (0x519647 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #53: _pyobject_call_prepend + 0xe0 (0x551d40 in vllm::enginecore) (enginecore_dp0 pid=698138) frame #54: vllm… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
