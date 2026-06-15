# vllm-project/vllm#6879: [Performance]: use Python array to replace Python list for zero-copy tensor creation

| 字段 | 值 |
| --- | --- |
| Issue | [#6879](https://github.com/vllm-project/vllm/issues/6879) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cache;cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: use Python array to replace Python list for zero-copy tensor creation

### Issue 正文摘录

### Proposal to improve performance For flexibility, lots of code in vLLM uses Python list. The memory layout for a Python list of `[1, 2, 3, 4, 5]`, is: ``` ---- PyObject pointer --> PyLong(1) ---- PyObject pointer --> PyLong(2) ---- PyObject pointer --> PyLong(3) ---- PyObject pointer --> PyLong(4) ---- PyObject pointer --> PyLong(5) ---- ``` This is because a Python list can hold arbitrary Python object. When we use `torch.tensor([1, 2, 3, 4, 5], dtype=torch.int, device="cuda")`, there's two copy operation happening: 1. PyTorch has to collect all the data from scattered memory into a continuous memory area, i.e. a CPU memory segment holding `1, 2, 3, 4, 5` consecutively (40 bytes) 2. PyTorch launches an operation to copy the CPU memory to GPU memory, wraps it into a GPU tensor There is a better alternative in Python, called `array.array`. It is very similar to `vector` type in `C++`, which can hold variable length data with the same type. Since the memory layout is already compact, we can directly create pytorch tensor from it, without copying, and then copy it to GPU. i.e., we can reduce the copy in step 1. Here is some microbenchmark: ```python import array import torch # pri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: can reduce the copy in step 1. Here is some microbenchmark: ```python import array import torch # print header print("N\tlist\tarray") for N in [100, 1000, 10000, 100000, 1000000]: list_data = list(range(N)) array_data...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ly (40 bytes) 2. PyTorch launches an operation to copy the CPU memory to GPU memory, wraps it into a GPU tensor There is a better alternative in Python, called `array.array`. It is very similar to `vector` type in `C++`...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: nce For flexibility, lots of code in vLLM uses Python list. The memory layout for a Python list of `[1, 2, 3, 4, 5]`, is: ``` ---- PyObject pointer --> PyLong(1) ---- PyObject pointer --> PyLong(2) ---- PyObject pointer...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: n array to replace Python list for zero-copy tensor creation performance;stale ### Proposal to improve performance For flexibility, lots of code in vLLM uses Python list. The memory layout for a Python list of `[1, 2, 3...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: py it to GPU. i.e., we can reduce the copy in step 1. Here is some microbenchmark: ```python import array import torch # print header print("N\tlist\tarray") for N in [100, 1000, 10000, 100000, 1000000]: list_data = lis...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
