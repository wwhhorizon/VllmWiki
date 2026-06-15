# vllm-project/vllm#37284: [Bug]: Docker Build Failure for Dockerfile.nightly_pytorch

| 字段 | 值 |
| --- | --- |
| Issue | [#37284](https://github.com/vllm-project/vllm/issues/37284) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker Build Failure for Dockerfile.nightly_pytorch

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The docker build fails during the FlashInfer build step in `Dockerfile.nightly_torch`. The Dockerfile attempts to build FlashInfer using the legacy `setup.py` approach, but [FlashInfer](https://github.com/flashinfer-ai/flashinfer/tree/v0.6.4) no longer ships `setup.py` from `v0.4.0` - it has migrated to a modern build system (`pyproject.toml`). --- ### Error ```bash 30.30 python3: can't open file `/vllm-workspace/flashinfer/setup.py`: [Error 2] No such file or directory ``` --- ### Steps to Reproduce 1. Build Docker image using `Dockerfile.nightly_torch` 2. Build proceeds through `[vllm-base 10/20]` successfully 3. Failed at `[vllm-base 11/20]` during FlashInfer wheel build --- ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Docker Build Failure for Dockerfile.nightly_pytorch bug ### Your current environment ### 🐛 Describe the bug The docker build fails during the FlashInfer build step in `Dockerfile.nightly_torch`. The Dockerfile at...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fer](https://github.com/flashinfer-ai/flashinfer/tree/v0.6.4) no longer ships `setup.py` from `v0.4.0` - it has migrated to a modern build system (`pyproject.toml`). --- ### Error ```bash 30.30 python3: can't open file...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: nvironment ### 🐛 Describe the bug The docker build fails during the FlashInfer build step in `Dockerfile.nightly_torch`. The Dockerfile attempts to build FlashInfer using the legacy `setup.py` approach, but [FlashInfer]...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: nfer/setup.py`: [Error 2] No such file or directory ``` --- ### Steps to Reproduce 1. Build Docker image using `Dockerfile.nightly_torch` 2. Build proceeds through `[vllm-base 10/20]` successfully 3. Failed at `[vllm-ba...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
