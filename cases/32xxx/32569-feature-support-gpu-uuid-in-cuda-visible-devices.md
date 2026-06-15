# vllm-project/vllm#32569: [Feature]: Support GPU UUID in `CUDA_VISIBLE_DEVICES`

| 字段 | 值 |
| --- | --- |
| Issue | [#32569](https://github.com/vllm-project/vllm/issues/32569) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support;moe;quantization |
| 子分类 |  |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | crash;nondeterministic |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support GPU UUID in `CUDA_VISIBLE_DEVICES`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently, vLLM does not support GPU UUIDs when specified via `CUDA_VISIBLE_DEVICES`. While CUDA natively supports both integer indices and GPU UUIDs for device specification, vLLM crashes with a `ValueError` when UUIDs are used. This error occurs in `vllm/platforms/interface.py` in the `device_id_to_physical_device_id` method, which assumes `CUDA_VISIBLE_DEVICES` only contains integer values. https://github.com/vllm-project/vllm/blob/3c8740aacb2b288390c986c169993ed2d97363f8/vllm/platforms/interface.py#L201-L214 **Motivation:** GPU UUIDs provide several critical advantages over integer indices: 1. **Deterministic device selection**: GPU indices can change after system reboots or driver updates, but UUIDs remain constant and tied to physical hardware 2. **Multi-node consistency**: In multi-GPU clusters, UUIDs provide a reliable way to identify specific GPUs across nodes 3. **Container orchestration compatibility**: Kubernetes GPU device plugins and other orchestrators often allocate GPUs by UUID 4. **Production stability**: UUIDs prevent accidental GPU reassignment in production environments **Use case:** ```bash # This is valid CUDA usage bu...

## 现有链接修复摘要

#32644 [Feature] Add GPU UUID support in CUDA_VISIBLE_DEVICES

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: motivation and pitch Currently, vLLM does not support GPU UUIDs when specified via `CUDA_VISIBLE_DEVICES`. While CUDA natively supports both integer indices and GPU UUIDs for device specification, vLLM crashes with a `V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Feature]: Support GPU UUID in `CUDA_VISIBLE_DEVICES` feature request ### 🚀 The feature, motivation and pitch Currently, vLLM does not support GPU UUIDs when specified via `CUDA_VISIBLE_DEVICES`. While CUDA natively sup...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: VISIBLE_DEVICES=GPU-441f29f8-b53a-1c18-174a-dd2066ebd468 vllm serve meta-llama/Llama-2-7b-hf ``` This is particularly important for: - Kubernetes deployments with GPU device plugins - SLURM and HPC schedulers that use U...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: PU UUIDs provide several critical advantages over integer indices: 1. **Deterministic device selection**: GPU indices can change after system reboots or driver updates, but UUIDs remain constant and tied to physical har...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Support GPU UUID in `CUDA_VISIBLE_DEVICES` feature request ### 🚀 The feature, motivation and pitch Currently, vLLM does not support GPU UUIDs when specified via `CUDA_VISIBLE_DEVICES`. While CUDA natively sup...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#32644](https://github.com/vllm-project/vllm/pull/32644) | closes_keyword | 0.95 | [Feature] Add GPU UUID support in CUDA_VISIBLE_DEVICES | Fixes #32569 Right now, vLLM crashes when you set `CUDA_VISIBLE_DEVICES` to a GPU UUID instead of an integer index. This is a problem because CUDA itself supports UUIDs natively. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
