# vllm-project/vllm#27405: [Bug]: qwen3-vl-2b after ms-swift fine-tuning  lance errors

| 字段 | 值 |
| --- | --- |
| Issue | [#27405](https://github.com/vllm-project/vllm/issues/27405) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;scheduler_memory |
| 子分类 | race_cond |
| Operator 关键词 | attention;cuda;kernel;operator |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: qwen3-vl-2b after ms-swift fine-tuning  lance errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug (Worker_TP1 pid=43610) INFO 10-23 09:29:27 [gpu_model_runner.py:2602] Starting to load model /media/kwaishop-langbridge-kfs/chenjunjie/live-product-matcher-reject/sft_train/ms-swift/qwen3_vl_2b_1023_sft_afternoon_prompt_v6_merge... (Worker_TP1 pid=43610) INFO 10-23 09:29:27 [gpu_model_runner.py:2634] Loading model from scratch... (Worker_TP1 pid=43610) INFO 10-23 09:29:28 [cuda.py:366] Using Flash Attention backend on V1 engine. (Worker_TP0 pid=43609) INFO 10-23 09:29:28 [gpu_model_runner.py:2602] Starting to load model /media/kwaishop-langbridge-kfs/chenjunjie/live-product-matcher-reject/sft_train/ms-swift/qwen3_vl_2b_1023_sft_afternoon_prompt_v6_merge... (Worker_TP0 pid=43609) INFO 10-23 09:29:28 [gpu_model_runner.py:2634] Loading model from scratch... (Worker_TP0 pid=43609) INFO 10-23 09:29:29 [cuda.py:366] Using Flash Attention backend on V1 engine. Loading safetensors checkpoint shards: 0% Completed | 0/1 [00:00 , std::allocator >) + 0x80 (0x7f89ca37eeb0 in /root/miniconda3/envs/qwen3-vl/lib/python3.12/site-packages/torch/lib/libc10.so) frame #1: + 0x5d694d1 (0x7f89ae3ef4d1 in /root/miniconda3/envs/qwen3-vl/lib/python3.12/si...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency | #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: cratch... (Worker_TP1 pid=43610) INFO 10-23 09:29:28 [cuda.py:366] Using Flash Attention backend on V1 engine. (Worker_TP0 pid=43609) INFO 10-23 09:29:28 [gpu_model_runner.py:2602] Starting to load model /media/kwaishop...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: RuntimeError: Worker failed with error 'CUDA error: the provided PTX was compiled with an unsupported toolchain. (EngineCore_DP0 pid=43418) CUDA kernel errors might be asynchronously reported at some other API call, so...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: oading model from scratch... (Worker_TP1 pid=43610) INFO 10-23 09:29:28 [cuda.py:366] Using Flash Attention backend on V1 engine. (Worker_TP0 pid=43609) INFO 10-23 09:29:28 [gpu_model_runner.py:2602] Starting to load mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen3-vl-2b after ms-swift fine-tuning lance errors bug ### Your current environment ### 🐛 Describe the bug (Worker_TP1 pid=43610) INFO 10-23 09:29:27 [gpu_model_runner.py:2602] Starting to load model /media/kwai...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: PyObject_MakeTpCall + 0x2fc (0x51778c in VLLM::Worker_TP1) frame #21: _PyEval_EvalFrameDefault + 0x6d2 (0x521952 in VLLM::Worker_TP1) frame #22: + 0x85294a (0x7f89bd39094a in /root/miniconda3/envs/qwen3-vl/lib/python3.1...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | wen3-vl/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so) frame #4: c10d::tcpstore::check(std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | en3-vl/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #6: <unknown function> + 0xdbbf4 (0x7f895125abf4 in /root/miniconda3/envs/qwen3-vl/bin/../lib/libstdc++.so.6)… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | f4 in /root/miniconda3/envs/qwen3-vl/bin/../lib/libstdc++.so.6) frame #7: <unknown function> + 0x94ac3 (0x7f89cb1c4ac3 in /lib/x86_64-linux-gnu/libc.so.6) frame #8: <unknown funct… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | en3-vl/lib/python3.12/site-packages/torch/lib/libtorch_cuda.so) frame #12: c10d::processgroupnccl::initncclcomm(std::__cxx11::basic_string<char, std::char_traits<char>, std::alloc… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | wen3-vl/lib/python3.12/site-packages/torch/lib/libtorch_cpu.so) frame #16: <unknown function> + 0x5d2dd0b (0x7f89ae3b3d0b in /root/miniconda3/envs/qwen3-vl/lib/python3.12/site-pac… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | ib/libtorch_python.so) frame #19: vllm::worker_tp1() [0x543944] frame #20: _pyobject_maketpcall + 0x2fc (0x51778c in vllm::worker_tp1) frame #21: _pyeval_evalframedefault + 0x6d2… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | 20: _pyobject_maketpcall + 0x2fc (0x51778c in vllm::worker_tp1) frame #21: _pyeval_evalframedefault + 0x6d2 (0x521952 in vllm::worker_tp1) frame #22: <unknown function> + 0x85294a… |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | 3-vl/lib/python3.12/site-packages/torch/lib/libtorch_python.so) frame #27: <unknown function> + 0x81567a (0x7f89bd35367a in /root/miniconda3/envs/qwen3-vl/lib/python3.12/site-pack… |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | 3-vl/lib/python3.12/site-packages/torch/lib/libtorch_python.so) frame #29: vllm::worker_tp1() [0x543944] frame #30: _pyobject_call + 0xb5 (0x555cd5 in vllm::worker_tp1) frame #31:… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | pyeval_evalframedefault + 0x53fe (0x52667e in vllm::worker_tp1) frame #32: _pyobject_fastcalldicttstate + 0x285 (0x519fc5 in vllm::worker_tp1) frame #33: _pyobject_call_prepend +… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | main + 0x80 (0x7f89cb159e40 in /lib/x86_64-linux-gnu/libc.so.6) frame #53: vllm::worker_tp1() [0x5c69e9] [rank1]:[w1023 09:29:42.988847516 tcpstore.cpp:125] [c10d] recvvalue faile… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
