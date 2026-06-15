# vllm-project/vllm#35463: [Bug]: Error on sleep mode when upgrade into vllm 0.16.0

| 字段 | 值 |
| --- | --- |
| Issue | [#35463](https://github.com/vllm-project/vllm/issues/35463) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | scheduler_memory |
| 子分类 | shape_align |
| Operator 关键词 | cuda |
| 症状 | oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error on sleep mode when upgrade into vllm 0.16.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When upgrade from vllm 0.15.0 to vllm 0.16.0 I got error ``` CUDA Error: invalid argument at /workspace/csrc/cumem_allocator.cpp:119 torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 79.19 GiB of which 78.67 GiB is free. Process 23769 has 530.00 MiB memory in use. Of the allocated memory 4.00 MiB is allocated by PyTorch, and 16.00 MiB is reserved by PyTorch but unallocated. If reserved but unallocated memory is large try setting PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True to avoid fragmentation ``` Sample reproduce code ```python import torch from vllm.device_allocator.cumem import CuMemAllocator def test_basic_cumem(): # some tensors from default memory pool shape = (1024, 1024) x = torch.empty(shape, device="cuda") x.zero_() # some tensors from custom memory pool allocator = CuMemAllocator.get_instance() with allocator.use_memory_pool(): # custom memory pool y = torch.empty(shape, device="cuda") y.zero_() y += 1 z = torch.empty(shape, device="cuda") z.zero_() z += 2 # they can be used together output = x + y + z assert torch.allclose(output, torch.ones_like(output) * 3)...

## 现有链接修复摘要

#35489 [Bugfix] Fix Fabric/RDMA attribute queries poisoning global error_code in cumem allocator

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: A_ALLOC_CONF=expandable_segments:True to avoid fragmentation ``` Sample reproduce code ```python import torch from vllm.device_allocator.cumem import CuMemAllocator def test_basic_cumem(): # some tensors from default me...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: : CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0 has a total capacity of 79.19 GiB of which 78.67 GiB is free. Process 23769 has 530.00 MiB memory in use. Of the allocated memory 4.00 MiB is allocated by PyTorch...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: the bug When upgrade from vllm 0.15.0 to vllm 0.16.0 I got error ``` CUDA Error: invalid argument at /workspace/csrc/cumem_allocator.cpp:119 torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 20.00 MiB. GPU 0...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Error on sleep mode when upgrade into vllm 0.16.0 bug;stale ### Your current environment ### 🐛 Describe the bug When upgrade from vllm 0.15.0 to vllm 0.16.0 I got error ``` CUDA Error: invalid argument at /worksp...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: er lots of frequently asked questions. correctness scheduler_memory cuda oom env_dependency;shape #35489 [Bugfix] Fix Fabric/RDMA attribute queries poisoning global error_code in cumem allocator Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#35489](https://github.com/vllm-project/vllm/pull/35489) | closes_keyword | 0.95 | [Bugfix] Fix Fabric/RDMA attribute queries poisoning global error_code in cumem allocator | Fix #35463. When upgrading from vllm 0.15.0 to 0.16.0, users encounter `CUDA Error: invalid argument at cumem_allocator.cpp:119` followed by OOM errors during `allocator.sleep()`. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
