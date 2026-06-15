# vllm-project/vllm#29141: [Bug]: Unable to run Qwen3 MoE NVFP4 on SM120

| 字段 | 值 |
| --- | --- |
| Issue | [#29141](https://github.com/vllm-project/vllm/issues/29141) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;kernel;moe;operator |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run Qwen3 MoE NVFP4 on SM120

### Issue 正文摘录

### Your current environment ubuntu 24.04 uv python3.12 cuda 12.8 torch 2.9.0 vllm 0.11.2 gpu: rtx 5070ti * 2 ### 🐛 Describe the bug vllm version 0.11.2 model name nvidia/Qwen3-30B-A3B-FP4 error as following: (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] return torch.ops._C.cutlass_fp4_group_mm( (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] File "/home/terry/vllm_cu128/lib/python3.12/site-packages/torch/_ops.py", line 1255, in __call__ (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] return self._op(*args, **kwargs) (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] ^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] torch.AcceleratorError: CUDA error: no kernel image is available for execution on the device ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can ans...

## 现有链接修复摘要

#33516 [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Bug]: Unable to run Qwen3 MoE NVFP4 on SM120 bug;stale ### Your current environment ubuntu 24.04 uv python3.12 cuda 12.8 torch 2.9.0 vllm 0.11.2 gpu: rtx 5070ti * 2 ### 🐛 Describe the bug vllm version 0.11.2 model name...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Unable to run Qwen3 MoE NVFP4 on SM120 bug;stale ### Your current environment ubuntu 24.04 uv python3.12 cuda 12.8 torch 2.9.0 vllm 0.11.2 gpu: rtx 5070ti * 2 ### 🐛 Describe the bug vllm version 0.11.2 model name...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ERROR 11-21 09:36:12 [multiproc_executor.py:815] return torch.ops._C.cutlass_fp4_group_mm( (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (Worker_TP0 pid=1848...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: rch 2.9.0 vllm 0.11.2 gpu: rtx 5070ti * 2 ### 🐛 Describe the bug vllm version 0.11.2 model name nvidia/Qwen3-30B-A3B-FP4 error as following: (Worker_TP0 pid=184821) ERROR 11-21 09:36:12 [multiproc_executor.py:815] retur...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Unable to run Qwen3 MoE NVFP4 on SM120 bug;stale ### Your current environment ubuntu 24.04 uv python3.12 cuda 12.8 torch 2.9.0 vllm 0.11.2 gpu: rtx 5070ti * 2 ### 🐛 Describe the bug vllm version 0.11.2 model name...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33516](https://github.com/vllm-project/vllm/pull/33516) | closes_keyword | 0.95 | [Bugfix] Add SM110/SM120 device capability checks for NVFP4 MoE backends | Fixes #29141 Related to #28589 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
