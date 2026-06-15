# vllm-project/vllm#18691: [Bug]: build source errors

| 字段 | 值 |
| --- | --- |
| Issue | [#18691](https://github.com/vllm-project/vllm/issues/18691) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: build source errors

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use `pip install --no-build-isolation -e .` and failed with ```text build source errors cuda 12.3 Ubuntu 20.04.6 LTS git commit : commit 35be8fad62099199ab26fdb5e7c0001fd9f4d71c (HEAD -> main, origin/main, origin/HEAD) Author: Reid Date: Sun May 25 18:10:51 2025 +0800 [CI/build] fix no regex (#18676) Signed-off-by: reidliu41 Co-authored-by: reidliu41 ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: build source errors bug;stale ### Your current environment ### 🐛 Describe the bug I use `pip install --no-build-isolation -e .` and failed with ```text build source errors cuda 12.3 Ubuntu 20.04.6 LTS git co
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: build-isolation -e .` and failed with ```text build source errors cuda 12.3 Ubuntu 20.04.6 LTS git commit : commit 35be8fad62099199ab26fdb5e7c0001fd9f4d71c (HEAD -> main, origin/main, origin/HEAD) Author: Reid Date: Sun...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: build source errors bug;stale ### Your current environment ### 🐛 Describe the bug I use `pip install --no-build-isolation -e .` and failed with ```text build source errors cuda 12.3 Ubuntu 20.04.6 LTS git commit...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
