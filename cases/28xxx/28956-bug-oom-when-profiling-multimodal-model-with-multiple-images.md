# vllm-project/vllm#28956: [Bug]: OOM when profiling multimodal model with multiple images

| 字段 | 值 |
| --- | --- |
| Issue | [#28956](https://github.com/vllm-project/vllm/issues/28956) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;multimodal_vlm;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 | crash;oom |
| 根因提示 | env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: OOM when profiling multimodal model with multiple images

### Issue 正文摘录

### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug As per title. The error log is as follows: ``` [multiproc_executor.py:671] Traceback (most recent call last): [multiproc_executor.py:671] File "/root/miniconda3/lib/python3.11/site-packages/vllm/v1/executor/multiproc_executor.py", line 666, in worker_busy_loop [multiproc_executor.py:671] output = func(*args, **kwargs) [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^ [multiproc_executor.py:671] File "/root/miniconda3/lib/python3.11/site-packages/torch/utils/_contextlib.py", line 120, in decorate_context [multiproc_executor.py:671] return func(*args, **kwargs) [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^^^^^ [multiproc_executor.py:671] File "/root/miniconda3/lib/python3.11/site-packages/vllm/v1/worker/gpu_worker.py", line 263, in determine_available_memory [multiproc_executor.py:671] self.model_runner.profile_run() [multiproc_executor.py:671] File "/root/miniconda3/lib/python3.11/site-packages/vllm/v1/worker/gpu_model_runner.py", line 3379, in profile_run [multiproc_executor.py:671] expanded = output.new_zeros( [multiproc_executor.py:671] ^^^^^^^^^^^^^^^^^ [multiproc_executor.py:671] torch.OutOfMemoryError: CUDA out o...

## 现有链接修复摘要

#29386 [Bugfix] Fix overallocation in MM profiling

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: OOM when profiling multimodal model with multiple images bug ### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug As per title. The error log is as follows: ``` [multiproc_executor.py:671] Traceback (m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: OOM when profiling multimodal model with multiple images bug ### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug As per title. The error log is as follows: ``` [multiproc_executor.py:671] Traceback (m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: r: CUDA out of memory. Tried to allocate 3.00 GiB. GPU 6 has a total capacity of 139.81 GiB of which 2.58 GiB is free. Including non-PyTorch memory, this process has 137.21 GiB memory in use. Of the allocated memory 134...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ^^^^^^^^^^^^^^^^^ [multiproc_executor.py:671] torch.OutOfMemoryError: CUDA out of memory. Tried to allocate 3.00 GiB. GPU 6 has a total capacity of 139.81 GiB of which 2.58 GiB is free. Including non-PyTorch memory, thi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: OOM when profiling multimodal model with multiple images bug ### Your current environment vLLM 0.11.0 ### 🐛 Describe the bug As per title. The error log is as follows: ``` [multiproc_executor.py:671] Traceback (m...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#29386](https://github.com/vllm-project/vllm/pull/29386) | closes_keyword | 0.95 | [Bugfix] Fix overallocation in MM profiling  | FIXES #28956 ## Test Plan ## Test Result --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [ ] The purpose of the PR, such as "Fi |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
