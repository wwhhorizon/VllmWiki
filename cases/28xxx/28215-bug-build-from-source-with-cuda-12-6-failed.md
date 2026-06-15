# vllm-project/vllm#28215: [Bug]: Build from source with cuda 12.6 failed

| 字段 | 值 |
| --- | --- |
| Issue | [#28215](https://github.com/vllm-project/vllm/issues/28215) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Build from source with cuda 12.6 failed

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `VLLM_USE_PRECOMPILED=1 uv pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --index-strategy unsafe-best-match --prerelease=allow` works fine, but `VLLM_USE_PRECOMPILED=1 uv pip install -e . --extra-index-url https://download.pytorch.org/whl/cu126 --index-strategy unsafe-best-match --prerelease=allow` fails. Since my GPU driver only supports CUDA 12.6, I have to use the CUDA 12.6 build. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Build from source with cuda 12.6 failed bug;stale ### Your current environment ### 🐛 Describe the bug `VLLM_USE_PRECOMPILED=1 uv pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --index-s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Build from source with cuda 12.6 failed bug;stale ### Your current environment ### 🐛 Describe the bug `VLLM_USE_PRECOMPILED=1 uv pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --index-s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Build from source with cuda 12.6 failed bug;stale ### Your current environment ### 🐛 Describe the bug `VLLM_USE_PRECOMPILED=1 uv pip install -e . --extra-index-url https://download.pytorch.org/whl/cu129 --index-s...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
