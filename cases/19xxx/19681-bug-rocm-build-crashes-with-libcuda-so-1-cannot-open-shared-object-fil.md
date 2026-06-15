# vllm-project/vllm#19681: [Bug]: rocm build crashes with libcuda.so.1: cannot open shared object file

| 字段 | 值 |
| --- | --- |
| Issue | [#19681](https://github.com/vllm-project/vllm/issues/19681) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: rocm build crashes with libcuda.so.1: cannot open shared object file

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The current branch crashes with rocm: ``` libcuda.so.1: cannot open shared object file ``` The issue is here, it doesn't check for hip: https://github.com/vllm-project/vllm/blob/main/vllm/device_allocator/cumem.py#L48-L64 Replacing it with something like this solves the issue: ```Python cumem_available = False try: if torch.version.hip: raise RuntimeError("Skipping CuMemAllocator on ROCm platform") from vllm.cumem_allocator import (init_module, python_create_and_map, python_unmap_and_release) from vllm.distributed.device_communicators.cuda_wrapper import (CudaRTLibrary) lib_name = find_loaded_library("cumem_allocator") cumem_available = lib_name is not None except Exception: # rocm platform does not support cumem allocator init_module = None python_create_and_map = None python_unmap_and_release = None CudaRTLibrary = None lib_name = None libcudart = None ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: rocm build crashes with libcuda.so.1: cannot open shared object file bug;rocm ### Your current environment ### 🐛 Describe the bug The current branch crashes with rocm: ``` libcuda.so.1: cannot open shared object...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: rocm build crashes with libcuda.so.1: cannot open shared object file bug;rocm ### Your current environment ### 🐛 Describe the bug The current branch crashes with rocm: ``` libcuda.so.1: cannot open shared object...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: with something like this solves the issue: ```Python cumem_available = False try: if torch.version.hip: raise RuntimeError("Skipping CuMemAllocator on ROCm platform") from vllm.cumem_allocator import (init_module, pytho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ed questions. development ci_build;distributed_parallel;hardware_porting;scheduler_memory cuda build_error;crash env_dependency Your current environment
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;scheduler_memory cuda buil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
