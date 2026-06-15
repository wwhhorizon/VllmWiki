# vllm-project/vllm#26922: [Bug]: torch symm mem - CUDA driver error: system not yet initialized

| 字段 | 值 |
| --- | --- |
| Issue | [#26922](https://github.com/vllm-project/vllm/issues/26922) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | distributed_parallel;moe;quantization |
| 子分类 | runtime_err |
| Operator 关键词 | cuda;moe |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: torch symm mem - CUDA driver error: system not yet initialized

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --enable-expert-parallel --port 9256` will trigger error: ```bash ERROR 10-15 09:00:49 [multiproc_executor.py:628] File "/home/wentao/vllm-source/vllm/distributed/parallel_state.py", line 363, in __init__ ERROR 10-15 09:00:49 [multiproc_executor.py:628] self.device_communicator = device_comm_cls( ERROR 10-15 09:00:49 [multiproc_executor.py:628] ^^^^^^^^^^^^^^^^ ERROR 10-15 09:00:49 [multiproc_executor.py:628] File "/home/wentao/vllm-source/vllm/distributed/device_communicators/cuda_communicator.py", line 70, in __init__ ERROR 10-15 09:00:49 [multiproc_executor.py:628] self.symm_mem_comm = SymmMemCommunicator( ERROR 10-15 09:00:49 [multiproc_executor.py:628] ^^^^^^^^^^^^^^^^^^^^ ERROR 10-15 09:00:49 [multiproc_executor.py:628] File "/home/wentao/vllm-source/vllm/distributed/device_communicators/symm_mem.py", line 94, in __init__ ERROR 10-15 09:00:49 [multiproc_executor.py:628] handle = torch_symm_mem.rendezvous(self.buffer, self.group.group_name) ERROR 10-15 09:00:49 [multiproc_executor.py:628] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 10-15 09:00:49 [multiproc_exe...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: t environment ### 🐛 Describe the bug `vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --enable-expert-parallel --port 9256` will trigger error: ```bash ERROR 10-15 09:00:49 [multiproc_executor.py:628] File "/home/wentao/vllm-so...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: torch symm mem - CUDA driver error: system not yet initialized bug ### Your current environment ### 🐛 Describe the bug `vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --enable-expert-parallel --port 9256` will trigger e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: # 🐛 Describe the bug `vllm serve nvidia/DeepSeek-R1-FP4 -tp 4 --enable-expert-parallel --port 9256` will trigger error: ```bash ERROR 10-15 09:00:49 [multiproc_executor.py:628] File "/home/wentao/vllm-source/vllm/distri...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ns. development distributed_parallel;moe;quantization cuda;moe crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _environment ERROR 10-15 09:00:49 [multiproc_executor.py:628] ensure_model_parallel_initialized( ERROR 10-15 09:00:49 [multiproc_executor.py:628] File "/home/wentao/vllm-source/vllm/distributed/parallel_state.py", line...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
