# vllm-project/vllm#5337: [Bug]: non-deterministic Python gc order leads to flaky tests

| 字段 | 值 |
| --- | --- |
| Issue | [#5337](https://github.com/vllm-project/vllm/issues/5337) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: non-deterministic Python gc order leads to flaky tests

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I often see many flaky tests, and I think the Python gc system is one of the factor to blame. Python gc system is notoriously random. When we call `del x`, and `x`'s refcount is 0, it is not guaranteed that all resources held by `x` will be released immediately. This is true especially when `x` is a complicated object, and might contain self-reference inside it. That's one of the motivation for Python to propose the concept of context manager, to enforce some critical resource to be released immediately. Take the following code as an example: ```python import torch import weakref import gc def tensor_destructed(tensor_ref): # This function is called when the tensor is destructed. print(f"Tensor with id {id(tensor_ref)} is being destructed.") class A: def __init__(self): self.tensor = torch.tensor([1.0, 2.0, 3.0]) def __del__(self): print("A is being destructed.") del self.tensor def main(): # Create a complex object with a tensor. data = A() # the object is so complicated that it has a reference to itself. data.self = data # Attach a weak reference to the tensor with a callback fo...

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: non-deterministic Python gc order leads to flaky tests bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I often see many flaky tests, and I think the Pytho...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: all resources held by `x` will be released immediately. This is true especially when `x` is a complicated object, and might contain self-reference inside it. That's one of the motivation for Python to propose the concep...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: 2/tests/models/test_models.py#L37-L44 After `del hf_model`, chances are GPU memory held by `hf_model` is not released yet. This will cause OOM for the later vLLM model, leading to a flaky test. I have seen it broken for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: om/vllm-project/vllm/blob/388596c91437a51d428a447594e9faec340c29b2/tests/models/test_models.py#L37-L44 After `del hf_model`, chances are GPU memory held by `hf_model` is not released yet. This will cause OOM for the lat...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: [Bug]: non-deterministic Python gc order leads to flaky tests bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug I often see many flaky tests, and I think the Pytho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
