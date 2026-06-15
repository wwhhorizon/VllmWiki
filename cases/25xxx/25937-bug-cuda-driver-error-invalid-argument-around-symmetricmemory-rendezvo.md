# vllm-project/vllm#25937: [Bug]: CUDA driver error: invalid argument around _SymmetricMemory.rendezvous

| 字段 | 值 |
| --- | --- |
| Issue | [#25937](https://github.com/vllm-project/vllm/issues/25937) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;scheduler_memory |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: CUDA driver error: invalid argument around _SymmetricMemory.rendezvous

### Issue 正文摘录

### Your current environment vllm main branch ### 🐛 Describe the bug On some machines, running `vllm serve -tp 8` will get this error: ```text ERROR 09-30 01:24:08 [multiproc_executor.py:597] self.symm_mem_comm = SymmMemCommunicator( ERROR 09-30 01:24:08 [multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^ ERROR 09-30 01:24:08 [multiproc_executor.py:597] File "/data/youkaichao/vllm/vllm/distributed/device_communicators/symm_mem.py", line 88, in __init__ ERROR 09-30 01:24:08 [multiproc_executor.py:597] handle = torch_symm_mem.rendezvous(self.buffer, self.group.group_name) ERROR 09-30 01:24:08 [multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 09-30 01:24:08 [multiproc_executor.py:597] File "/data/youkaichao/uv_envs/py312/lib/python3.12/site-packages/torch/distributed/_symmetric_memory/__init__.py", line 1711, in rendezvous ERROR 09-30 01:24:08 [multiproc_executor.py:597] return _SymmetricMemory.rendezvous(tensor, group_name) ERROR 09-30 01:24:08 [multiproc_executor.py:597] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 09-30 01:24:08 [multiproc_executor.py:597] RuntimeError: CUDA driver error: invalid argument ``` We can run `TORCH_CP...

## 现有链接修复摘要

#4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ybind11::detail::function_call&) const from :0 ``` So this happens when building the multicast object. One way to get around the issue is to run with `TORCH_SYMM_MEM_DISABLE_MULTICAST=1 vllm serve -tp 8` , i.e. adding `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: CUDA driver error: invalid argument around _SymmetricMemory.rendezvous bug;stale ### Your current environment vllm main branch ### 🐛 Describe the bug On some machines, running `vllm serve -tp 8` will get this err...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: :08 [multiproc_executor.py:597] Exception raised from init_multicast_for_block at /pytorch/torch/csrc/distributed/c10d/symm_mem/CUDASymmetricMemory.cu:573 (most recent call first): ERROR 09-30 01:28:08 [multiproc_execut...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: DA driver error: invalid argument around _SymmetricMemory.rendezvous bug;stale ### Your current environment vllm main branch ### 🐛 Describe the bug On some machines, running `vllm serve -tp 8` will get this error: ```te...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: allel;scheduler_memory cuda;operator env_dependency;memory_layout #4 Use FlashAttention for `multi_query_kv_attention` | #6 Automatically configure KV cache size | #7 Support beam search & parallel generation Your curre...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#4](https://github.com/vllm-project/vllm/pull/4) | mentioned | 0.45 | Use FlashAttention for `multi_query_kv_attention` | + capturedtraceback: error 09-30 01:28:08 [multiproc_executor.py:597] #4 std::_function_handler<std::shared_ptr<c10::lazyvalue<std::__cxx11::basic_string<char, std::char_traits<ch… |
| [#6](https://github.com/vllm-project/vllm/pull/6) | mentioned | 0.45 | Automatically configure KV cache size | r<char> >) from ??:0 error 09-30 01:28:08 [multiproc_executor.py:597] #6 c10::detail::torchcheckfail(char const*, char const*, unsigned int, std::__cxx11::basic_string<char, std::… |
| [#7](https://github.com/vllm-project/vllm/pull/7) | mentioned | 0.45 | Support beam search & parallel generation | > const&) from ??:0 error 09-30 01:28:08 [multiproc_executor.py:597] #7 c10d::symmetric_memory::init_multicast_for_block(unsigned long long&, void*&, c10::intrusive_ptr<c10d::symm… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
