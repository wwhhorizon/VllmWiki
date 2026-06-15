# vllm-project/vllm#16993: [Bug]: vLLM sleep experiences segmentation fault when used in TRL

| 字段 | 值 |
| --- | --- |
| Issue | [#16993](https://github.com/vllm-project/vllm/issues/16993) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling |
| 症状 | crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: vLLM sleep experiences segmentation fault when used in TRL

### Issue 正文摘录

### Your current environment I am utilizing vLLM sleep in HF - TRL to efficiently manage GPU memory between training and generation. See my draft [PR](https://github.com/toslali-ibm/trl/pull/4/files). The training is completed successfully, but I see a `segmentation fault` error at the end. I am not seeing this error in vLLM==0.7.3, but observing the error in 0.8.0, 0.8.1, and so on. ### 🐛 Describe the bug Segmentation fault occurs when distributed training is complete. I tried to reproduce it in a simpler script (see below). I don't get the segmentation fault, but observe a critical warning, which may be a hint: ``` [rank0]:[W422 15:49:17.205132298 ProcessGroupNCCL.cpp:1496] Warning: WARNING: destroy_process_group() was not called before program exit, which can leak resources. For more info, please see https://pytorch.org/docs/stable/distributed.html#shutdown (function operator()) /usr/lib/python3.10/multiprocessing/resource_tracker.py:224: UserWarning: resource_tracker: There appear to be 1 leaked shared_memory objects to clean up at shutdown warnings.warn('resource_tracker: There appear to be %d ' ``` ### Before submitting a new issue... - [x] Make sure you already searched for...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Implement preemption via recomputation & Refactor scheduling logic | #16 Add custom kernel for RMS normalization | #20 Optimize data movement | #21 Add ninja to dependency

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ed in TRL bug ### Your current environment I am utilizing vLLM sleep in HF - TRL to efficiently manage GPU memory between training and generation. See my draft [PR](https://github.com/toslali-ibm/trl/pull/4/files). The...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: # Your current environment I am utilizing vLLM sleep in HF - TRL to efficiently manage GPU memory between training and generation. See my draft [PR](https://github.com/toslali-ibm/trl/pull/4/files). The training is comp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: environment I am utilizing vLLM sleep in HF - TRL to efficiently manage GPU memory between training and generation. See my draft [PR](https://github.com/toslali-ibm/trl/pull/4/files). The training is completed successfu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: logits cuda;kernel;operator;sampling crash;nan_inf env_dependency #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation | #12 Impl...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | sr/local/lib/python3.10/dist-packages/torch/lib/libc10_cuda.so) frame #4: <unknown function> + 0x2320e (0x7fee9574620e in /usr/local/lib/python3.10/dist-packages/torch/lib/libc10_… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | sr/local/lib/python3.10/dist-packages/torch/lib/libc10_cuda.so) frame #6: c10::cuda::mempool::~mempool() + 0x1b9 (0x7fee95748329 in /usr/local/lib/python3.10/dist-packages/torch/l… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | sr/local/lib/python3.10/dist-packages/torch/lib/libc10_cuda.so) frame #7: <unknown function> + 0xdf74f0 (0x7fee8d4864f0 in /usr/local/lib/python3.10/dist-packages/torch/lib/libtor… |
| [#12](https://github.com/vllm-project/vllm/pull/12) | mentioned | 0.45 | Implement preemption via recomputation & Refactor scheduling logic | nknown function> + 0x135c52 (0x564c79bedc52 in /usr/bin/python) frame #12: <unknown function> + 0x136991 (0x564c79bee991 in /usr/bin/python) frame #13: <unknown function> + 0x1367… |
| [#16](https://github.com/vllm-project/vllm/pull/16) | mentioned | 0.45 | Add custom kernel for RMS normalization | nknown function> + 0x172aa0 (0x564c79c2aaa0 in /usr/bin/python) frame #16: <unknown function> + 0x1caa87 (0x564c79c82a87 in /usr/bin/python) frame #17: <unknown function> + 0x129e… |
| [#20](https://github.com/vllm-project/vllm/pull/20) | mentioned | 0.45 | Optimize data movement | #19: py_finalizeex + 0x148 (0x564c79d184c8 in /usr/bin/python) frame #20: py_runmain + 0x173 (0x564c79d09913 in /usr/bin/python) frame #21: py_bytesmain + 0x2d (0x564c79ce002d in… |
| [#21](https://github.com/vllm-project/vllm/pull/21) | mentioned | 0.45 | Add ninja to dependency | ame #20: py_runmain + 0x173 (0x564c79d09913 in /usr/bin/python) frame #21: py_bytesmain + 0x2d (0x564c79ce002d in /usr/bin/python) frame #22: <unknown function> + 0x29d90 (0x7feec… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
