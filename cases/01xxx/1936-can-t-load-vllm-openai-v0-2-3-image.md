# vllm-project/vllm#1936: Can't load `vllm-openai/v0.2.3` image

| 字段 | 值 |
| --- | --- |
| Issue | [#1936](https://github.com/vllm-project/vllm/issues/1936) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api |
| 子分类 |  |
| Operator 关键词 | cuda;kernel |
| 症状 | build_error;mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Can't load `vllm-openai/v0.2.3` image

### Issue 正文摘录

As the title reads, upgraded from v0.2.2 and now getting this error: ``` vllm_1 | RuntimeError: CUDA error: no kernel image is available for execution on the device vllm_1 | CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect. vllm_1 | For debugging consider passing CUDA_LAUNCH_BLOCKING=1. vllm_1 | Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ```

## 现有链接修复摘要

#1950 [Docker] Add cuda arch list as build option

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: _1 | For debugging consider passing CUDA_LAUNCH_BLOCKING=1. vllm_1 | Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` correctness ci_build;frontend_api cuda;kernel build_error;mismatch #1950 [Dock...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ed from v0.2.2 and now getting this error: ``` vllm_1 | RuntimeError: CUDA error: no kernel image is available for execution on the device vllm_1 | CUDA kernel errors might be asynchronously reported at some other API c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ssertions. ``` correctness ci_build;frontend_api cuda;kernel build_error;mismatch #1950 [Docker] Add cuda arch list as build option As the title reads, upgraded from v0.2.2 and now getting this error:
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ight be incorrect. vllm_1 | For debugging consider passing CUDA_LAUNCH_BLOCKING=1. vllm_1 | Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. ``` correctness ci_build;frontend_api cuda;kernel build_err...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#1950](https://github.com/vllm-project/vllm/pull/1950) | closes_keyword | 0.95 | [Docker] Add cuda arch list as build option | close #1936 and prevent future regressions. |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
