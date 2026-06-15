# vllm-project/vllm#18362: [Bug]: Inference fails on Apple silicon due to (distributed) networking error?

| 字段 | 值 |
| --- | --- |
| Issue | [#18362](https://github.com/vllm-project/vllm/issues/18362) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Inference fails on Apple silicon due to (distributed) networking error?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am trying to run vllm on a MacBook Pro with a M4 Pro chip. I set up everything [according to the provided instructions](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html?device=apple). Everything seems to install without any issues, however, when I try to start the server with e.g. TinyLlama/TinyLlama-1.1B-Chat-v1.0 (or use it directly via python, doesn't really matter), I get some weird errors. The server basically seems to alternate between the "recvValue failed on SocketImpl" / "[c10d] TCP client failed to connect/validate to host" errors indefinitely. I haven't found much about those errors, but to my understanding, they seem to be related to pytorch's distributed networking. For the record, using the same environment, I can run models via transformers without any issues, e.g: ```python from transformers import AutoTokenizer, AutoModelForCausalLM tok = AutoTokenizer.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0") model = AutoModelForCausalLM.from_pretrained("TinyLlama/TinyLlama-1.1B-Chat-v1.0") model = model.to("mps") inputs = tok("hello world", return_tensors="pt").to("mps") out = model.generate(**...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: he provided instructions](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html?device=apple). Everything seems to install without any issues, however, when I try to start the server with e.g. TinyLlama/T...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: _support;quantization;scheduler_memory cuda;kernel;operator;quantization;triton build_error dtype;env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Suppo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: escribe the bug I am trying to run vllm on a MacBook Pro with a M4 Pro chip. I set up everything [according to the provided instructions](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html?device=apple...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ithout any issues, however, when I try to start the server with e.g. TinyLlama/TinyLlama-1.1B-Chat-v1.0 (or use it directly via python, doesn't really matter), I get some weird errors. The server basically seems to alte...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: erence fails on Apple silicon due to (distributed) networking error? bug;stale ### Your current environment ### 🐛 Describe the bug I am trying to run vllm on a MacBook Pro with a M4 Pro chip. I set up everything [accord...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | 10d::tcpstore::ping() + 200 (0x116b4e68c in libtorch_cpu.dylib) frame #4: c10d::tcpstore::tcpstore(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<ch… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | :tcpstoreoptions&) + 168 (0x1055ba3d4 in libtorch_python.dylib) frame #6: std::__1::enable_if<std::is_void<pybind11::class_<c10d::tcpstore, c10::intrusive_ptr<c10d::tcpstore, c10:… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | l<int>, bool)&) && + 176 (0x1055b9f48 in libtorch_python.dylib) frame #7: void pybind11::cpp_function::initialize<void pybind11::detail::initimpl::factory<torch::distributed::c10d… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | frame #11: method_vectorcall + 296 (0x102230244 in python3.12) frame #12: _pyvectorcall_call + 132 (0x10222c630 in python3.12) frame #13: slot_tp_init + 404 (0x1022b6e3c in python… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | pybind11_meta_call + 40 (0x104b14d20 in libtorch_python.dylib) frame #16: _pyobject_maketpcall + 312 (0x10222bc58 in python3.12) frame #17: _pyeval_evalframedefault + 52128 (0x102… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | n3.12) frame #19: gen_iternext + 52 (0x10224c258 in python3.12) frame #20: builtin_next + 148 (0x1023569a0 in python3.12) frame #21: cfunction_vectorcall_fastcall + 248 (0x10228eb… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | 3.12) frame #20: builtin_next + 148 (0x1023569a0 in python3.12) frame #21: cfunction_vectorcall_fastcall + 248 (0x10228ebc8 in python3.12) frame #22: pyobject_vectorcall + 88 (0x1… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | frame #26: method_vectorcall + 188 (0x1022301d8 in python3.12) frame #27: _pyvectorcall_call + 132 (0x10222c630 in python3.12) frame #28: _pyeval_evalframedefault + 59672 (0x10236… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 8: _pyeval_evalframedefault + 59672 (0x10236857c in python3.12) frame #29: _pyobject_fastcalldicttstate + 160 (0x10222c068 in python3.12) frame #30: slot_tp_init + 320 (0x1022b6de… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | hon3.12) frame #31: type_call + 524 (0x1022ad98c in python3.12) frame #32: _pyobject_maketpcall + 312 (0x10222bc58 in python3.12) frame #33: _pyeval_evalframedefault + 52128 (0x10… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
