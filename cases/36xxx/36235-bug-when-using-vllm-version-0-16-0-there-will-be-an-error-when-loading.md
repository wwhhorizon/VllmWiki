# vllm-project/vllm#36235: [Bug]: When using VLLM version 0.16.0, there will be an error when loading the qwen3-14b-awq model, such as: ERROR _wrapper.py:141: Error in wrapped target: CUDA error: the provided PTX was compiled with an unsupported toolchain.

| 字段 | 值 |
| --- | --- |
| Issue | [#36235](https://github.com/vllm-project/vllm/issues/36235) |
| 状态 | open |
| 标签 | bug |
| 评论 | 17; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;model_support;quantization |
| 子分类 | cold_start |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: When using VLLM version 0.16.0, there will be an error when loading the qwen3-14b-awq model, such as: ERROR _wrapper.py:141: Error in wrapped target: CUDA error: the provided PTX was compiled with an unsupported toolchain.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using VLLM version 0.16.0, there will be an error when loading the qwen3-14b-awq model, such as: ERROR _wrapper.py:141: Error in wrapped target: CUDA error: the provided PTX was compiled with an unsupported toolchain. The process of running the model is as follows, there will be two types of errors: First run of the model: Command: vllm serve /mnt/workspace/qwen3-14b-awq \ --enable-lora \ --max-lora-rank 32 \ --lora-modules ai-customer-rewrite=/mnt/workspace/v4_260228_qwen3_14b \ --port 8000 \ --host 0.0.0.0 --tensor-parallel-size 2 --gpu-memory-utilization 0.90 Error reported as follows: ``` RuntimeError: flashinfer-cubin version (0.6.4) does not match flashinfer version (0.6.3). Please install the same version of both packages. Set FLASHINFER_DISABLE_VERSION_CHECK=1 to bypass this check. ``` The error message asked me to add the FLASHINFER_DISABLEVERSIONCHECK parameter, and I set it： Second run of the model: Command: FLASHINFER_DISABLE_VERSION_CHECK=1 vllm serve /mnt/workspace/ai-customer-rewrite_16_1772608530718/qwen3-14b-awq \ --enable-lora \ --max-lora-rank 32 \ --lora-modules ai-customer-rewrite=/mnt/workspace/ai-custo...

## 现有链接修复摘要

#36579 Guard AWQ-Marlin auto-selection on CUDA driver/toolkit mismatch

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: When using VLLM version 0.16.0, there will be an error when loading the qwen3-14b-awq model, such as: ERROR _wrapper.py:141: Error in wrapped target: CUDA error: the provided PTX was compiled with an unsupported...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: -14b-awq model, such as: ERROR _wrapper.py:141: Error in wrapped target: CUDA error: the provided PTX was compiled with an unsupported toolchain. bug ### Your current environment ### 🐛 Describe the bug When using VLLM v...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: When using VLLM version 0.16.0, there will be an error when loading the qwen3-14b-awq model, such as: ERROR _wrapper.py:141: Error in wrapped target: CUDA error: the provided PTX was compiled with an unsupported toolcha...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: gpu-memory-utilization 0.90 Error reported as follows: ``` RuntimeError: flashinfer-cubin version (0.6.4) does not match flashinfer version (0.6.3). Please install the same version of both packages. Set FLASHINFER_DISAB...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: dependency #36579 Guard AWQ-Marlin auto-selection on CUDA driver/toolkit mismatch Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#36579](https://github.com/vllm-project/vllm/pull/36579) | closes_keyword | 0.95 | Guard AWQ-Marlin auto-selection on CUDA driver/toolkit mismatch | Fixes #36235 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
