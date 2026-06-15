# vllm-project/vllm#42338: [BUG]  cu129 Nightly Installation Resolves to CUDA 13 Wheel

| 字段 | 值 |
| --- | --- |
| Issue | [#42338](https://github.com/vllm-project/vllm/issues/42338) |
| 状态 | open |
| 标签 | documentation |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | import_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [BUG]  cu129 Nightly Installation Resolves to CUDA 13 Wheel

### Issue 正文摘录

## Description The latest wheel available on the cu129 nightly channel is `0.20.2rc1.dev233+g5497ffbf7.cu129`, while PyPI now publishes `0.20.2` as the final release (built against CUDA 13). Per PEP 440, the cu129 pre-release version sorts below the PyPI stable release, causing the documented installation command to resolve to the PyPI artifact: ```bash uv pip install -U vllm --pre \ --extra-index-url https://wheels.vllm.ai/nightly/cu129 \ --extra-index-url https://download.pytorch.org/whl/cu129 \ --index-strategy unsafe-best-match ``` This command installs `vllm 0.20.2`. Every compiled `.so` in the resulting installation links against `libcudart.so.13` (confirmed via `readelf -d`), causing CUDA 12 environments to fail at import with `ImportError: libcudart.so.13`. Under a healthy release flow, cu129 nightlies should be versioned ahead of the stable release (for example, `0.20.3rc1.devN+cu129`) and would win resolution, allowing the documented command to behave as intended. The artifact catalog at `wheels.vllm.ai/nightly/cu129/` appears to be stalled. ## Reproduction ```console (vllm) ➜ vLLM git:(swap-cu-version) ✗ uv pip install -U vllm --pre \ --extra-index-url https://wheels.vl...

## 现有链接修复摘要

#42917 docs: clarify CUDA nightly wheel index priority

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [BUG] cu129 Nightly Installation Resolves to CUDA 13 Wheel documentation ## Description The latest wheel available on the cu129 nightly channel is `0.20.2rc1.dev233+g5497ffbf7.cu129`, while PyPI now publishes `0.20.2` a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [BUG] cu129 Nightly Installation Resolves to CUDA 13 Wheel documentation ## Description The latest wheel available on the cu129 nightly channel is `0.20.2rc1.dev233+g5497ffbf7.cu129`, while PyPI now publishes `0.20.2` a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 13.0/lib64/libcudart.so.13 (0x000077bc08a00000) ``` development ci_build;scheduler_memory cuda import_error env_dependency #42917 docs: clarify CUDA nightly wheel index priority Description
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: stallation Resolves to CUDA 13 Wheel documentation ## Description The latest wheel available on the cu129 nightly channel is `0.20.2rc1.dev233+g5497ffbf7.cu129`, while PyPI now publishes `0.20.2` as the final release (b...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#42917](https://github.com/vllm-project/vllm/pull/42917) | mentioned | 0.6 | docs: clarify CUDA nightly wheel index priority | arify CUDA nightly wheel index priority ## Purpose Addresses #42338 This PR clarifies the CUDA nightly wheel installation docs to warn users against adding `--index-strategy |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
