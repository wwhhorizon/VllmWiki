# vllm-project/vllm#36835: [Bug] DGX Spark (sm_121): CUTLASS can_implement() rejects sm_120f binaries

| 字段 | 值 |
| --- | --- |
| Issue | [#36835](https://github.com/vllm-project/vllm/issues/36835) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug] DGX Spark (sm_121): CUTLASS can_implement() rejects sm_120f binaries

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug running the following test I get this error: ~/usr/vllm$ pytest tests/kernels/quantization/test_block_fp8.py::test_w8a8_block_fp8_cutlass_matmul -v -s 2>&1 | tee debug_shapes.log DEBUG 03-12 01:46:41 [plugins/__init__.py:36] No plugins for group vllm.platform_plugins found. DEBUG 03-12 01:46:41 [platforms/__init__.py:36] Checking if TPU platform is available. DEBUG 03-12 01:46:41 [platforms/__init__.py:55] TPU platform is not available because: No module named 'libtpu' DEBUG 03-12 01:46:41 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 03-12 01:46:41 [platforms/__init__.py:84] Confirmed CUDA platform is available. DEBUG 03-12 01:46:41 [platforms/__init__.py:112] Checking if ROCm platform is available. DEBUG 03-12 01:46:41 [platforms/__init__.py:126] ROCm platform is not available because: No module named 'amdsmi' DEBUG 03-12 01:46:41 [platforms/__init__.py:133] Checking if XPU platform is available. DEBUG 03-12 01:46:41 [platforms/__init__.py:155] Checking if CPU platform is available. DEBUG 03-12 01:46:41 [platforms/__init__.py:61] Checking if CUDA platform is available. DEBUG 03-12 01:46:41 [platforms/...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: g the following test I get this error: ~/usr/vllm$ pytest tests/kernels/quantization/test_block_fp8.py::test_w8a8_block_fp8_cutlass_matmul -v -s 2>&1 | tee debug_shapes.log DEBUG 03-12 01:46:41 [plugins/__init__.py:36]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: [Bug] DGX Spark (sm_121): CUTLASS can_implement() rejects sm_120f binaries bug ### Your current environment ### 🐛 Describe the bug running the following test I get this error: ~/usr/vllm$ pytest tests/kernels/quantizati...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: arning: `torch.jit.script_method` is deprecated. Please switch to `torch.compile` or `torch.export`. warnings.warn( -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html =========================== sho...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug] DGX Spark (sm_121): CUTLASS can_implement() rejects sm_120f binaries bug ### Your current environment ### 🐛 Describe the bug running the following test I get this error: ~/usr/vllm$ pytest tests/kernels/quantizati...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: sr/.venv/bin/python cachedir: .pytest_cache rootdir: /home/user/usr/vllm configfile: pyproject.toml plugins: anyio-4.12.1 collecting ... DEBUG 03-12 01:46:43 [utils/flashinfer.py:45] flashinfer-cubin package was not fou...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | (0xe8c1eceb4f38 in /home/user/usr/vllm/vllm/_c.abi3.so) e frame #4: <unknown function> + 0x55e5dc (0xe8c1ece9e5dc in /home/user/usr/vllm/vllm/_c.abi3.so) e frame #5: cutl |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | (0xe8c1ece9f3f8 in /home/user/usr/vllm/vllm/_c.abi3.so) e frame #6: cutlass_scaled_mm(at::tensor&, at::tensor const&, at::tensor const&, at::tensor const&, at::tensor const&, s |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | (0xe8c1ecdfe7b8 in /home/user/usr/vllm/vllm/_c.abi3.so) e frame #7: c10::impl::make_boxed_from_unboxed_functor<c10::impl::detail::wrapfunctionintoruntimefunctor_<void (*)(at::t |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | /python3.12/site-packages/torch/lib/libtorch_python.so) e frame #12: <unknown function> + 0xcc96b0 (0xe8c2293196b0 in /home/user/usr/.venv/lib/python3.12/site-packages/torch/lib |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | ll + 0x6c (0x4c633c in /home/user/usr/.venv/bin/python) e frame #16: _pyeval_evalframedefault + 0x3ea0 (0x568564 in /home/user/usr/.venv/bin/python) e frame #17: _pyobject |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | ll + 0x6c (0x4c633c in /home/user/usr/.venv/bin/python) e frame #20: _pyeval_evalframedefault + 0x3ea0 (0x568564 in /home/user/usr/.venv/bin/python) e frame #21: /home/use |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | + 0x3ea0 (0x568564 in /home/user/usr/.venv/bin/python) e frame #21: /home/user/usr/.venv/bin/python() [0x4c7f7c] e frame #22: pyobject_callmethod + 0x11c (0x4c533c in /ho |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | /python3.12/site-packages/torch/lib/libtorch_python.so) e frame #27: torch::jit::_get_operation_for_overload_or_packet(std::vector<std::shared_ptr<torch::jit::operator>, std::al |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | /python3.12/site-packages/torch/lib/libtorch_python.so) e frame #29: <unknown function> + 0x5d7dbc (0xe8c228c27dbc in /home/user/usr/.venv/lib/python3.12/site-packages/torch/lib |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | ll + 0x6c (0x4c633c in /home/user/usr/.venv/bin/python) e frame #32: _pyeval_evalframedefault + 0x3ea0 (0x568564 in /home/user/usr/.venv/bin/python) e frame #33: _pyobject |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | t + 0x8a0 (0x564f64 in /home/user/usr/.venv/bin/python) e frame #53: _pyobject_call_prepend + 0x1b4 (0x4c5a24 in /home/user/usr/.venv/bin/python) e frame #54: /home/user/u |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
