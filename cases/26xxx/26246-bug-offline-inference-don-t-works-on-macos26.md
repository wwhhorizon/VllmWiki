# vllm-project/vllm#26246: [Bug]: offline inference don't works on macOS26

| 字段 | 值 |
| --- | --- |
| Issue | [#26246](https://github.com/vllm-project/vllm/issues/26246) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 |  |
| Operator 关键词 | cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: offline inference don't works on macOS26

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug follow https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#apple-silicon to install vllm, i run `python examples/offline_inference/basic/basic.py` but don't works. ```text INFO 10-05 18:07:04 [__init__.py:215] Automatically detected platform cpu. INFO 10-05 18:07:05 [utils.py:233] non-default args: {'disable_log_stats': True, 'model': 'facebook/opt-125m'} INFO 10-05 18:07:07 [model.py:553] Resolved architecture: OPTForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! INFO 10-05 18:07:07 [model.py:1547] Using max model len 2048 WARNING 10-05 18:07:08 [cpu.py:120] Environment variable VLLM_CPU_KVCACHE_SPACE (GiB) for CPU backend is not set, using 4 by default. INFO 10-05 18:07:08 [arg_utils.py:1170] Chunked prefill is not supported for ARM and POWER, S390X and RISC-V CPUs; disabling it for V1 backend. INFO 10-05 18:07:10 [__init__.py:215] Automatically detected platform cpu. (EngineCore_DP0 pid=48190) INFO 10-05 18:07:11 [core.py:648] Waiting for init message from front-end. (EngineCore_DP0 pid=48190) INFO 10-05 18:07:11 [core.py:78] Initializing a V1 LLM engine (v0.11.0rc2.dev213+ga964e5e6c) with config:...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: Describe the bug follow https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#apple-silicon to install vllm, i run `python examples/offline_inference/basic/basic.py` but don't works. ```text INFO 10-05 18...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 6: 8 [cpu.py:120] Environment variable VLLM_CPU_KVCACHE_SPACE (GiB) for CPU backend is not set, using 4 by default. INFO 10-05 18:07:08 [arg_utils.py:1170] Chunked prefill is not supported for ARM and POWER, S390X and RISC...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: offline inference don't works on macOS26 bug;stale ### Your current environment ### 🐛 Describe the bug follow https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#apple-silicon to install vllm, i...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: lative_config=None, tokenizer='facebook/opt-125m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=Non...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: -05 18:07:07 [model.py:553] Resolved architecture: OPTForCausalLM `torch_dtype` is deprecated! Use `dtype` instead! INFO 10-05 18:07:07 [model.py:1547] Using max model len 2048 WARNING 10-05 18:07:08 [cpu.py:120] Enviro...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 10d::tcpstore::ping() + 200 (0x11a8a5aa8 in libtorch_cpu.dylib) frame #4: c10d::tcpstore::tcpstore(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<ch… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | :tcpstoreoptions&) + 168 (0x107ea2710 in libtorch_python.dylib) frame #6: std::__1::enable_if<std::is_void<pybind11::class_<c10d::tcpstore, c10::intrusive_ptr<c10d::tcpstore, c10:… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | l<int>, bool)&) && + 176 (0x107ea2284 in libtorch_python.dylib) frame #7: void pybind11::cpp_function::initialize<void pybind11::detail::initimpl::factory<torch::distributed::c10d… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | hon) frame #11: method_vectorcall + 964 (0x100ca1250 in python) frame #12: _pyvectorcall_call + 152 (0x100c9e668 in python) frame #13: slot_tp_init + 480 (0x100d14ea0 in python) f… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | pybind11_meta_call + 40 (0x107397bbc in libtorch_python.dylib) frame #16: _pyobject_maketpcall + 124 (0x100c9dec0 in python) frame #17: _pyeval_evalframedefault + 23416 (0x100d913… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | in python) frame #19: gen_iternext + 36 (0x100cb6440 in python) frame #20: builtin_next + 72 (0x100d890d0 in python) frame #21: cfunction_vectorcall_fastcall + 96 (0x100cef520 in… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | in python) frame #20: builtin_next + 72 (0x100d890d0 in python) frame #21: cfunction_vectorcall_fastcall + 96 (0x100cef520 in python) frame #22: _pyeval_evalframedefault + 11144 (… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | n python) frame #26: slot_tp_init + 212 (0x100d14d94 in python) frame #27: type_call + 148 (0x100d0c020 in python) frame #28: _pyobject_maketpcall + 124 (0x100c9dec0 in python) fr… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | ) frame #28: _pyobject_maketpcall + 124 (0x100c9dec0 in python) frame #29: _pyeval_evalframedefault + 23416 (0x100d913a4 in python) frame #30: _pyobject_fastcalldicttstate + 200 (… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | n python) frame #31: slot_tp_init + 212 (0x100d14d94 in python) frame #32: type_call + 148 (0x100d0c020 in python) frame #33: _pyobject_call + 124 (0x100c9ea00 in python) frame #3… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
