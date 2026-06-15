# vllm-project/vllm#41264: [Feature]: Update default Python version in pre-built docker images

| 字段 | 值 |
| --- | --- |
| Issue | [#41264](https://github.com/vllm-project/vllm/issues/41264) |
| 状态 | open |
| 标签 | feature request |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Update default Python version in pre-built docker images

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Since vLLM==0.20.0 now supports Python 3.14, are there plans to update the default python version in the vLLM docker images? It's still using python 3.12. When I scan it with grype, I get a handful of CVEs that would be resolved by upgrading to a more recent python version. These look like they could be resolved by upgrading to either Python 3.13 or Python 3.14. ``` libpython3.12-dev 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 libpython3.12-minimal 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 libpython3.12-stdlib 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 libpython3.12t64 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 python3.12 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 python3.12-dev 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 python3.12-minimal 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 python3.12-venv 3.12.3-1ubuntu0.13 deb CVE-2026-4519 Medium < 0.1% (0th) < 0.1 libpython3.12-dev 3.12.3-1ubuntu0.13 deb CVE-2026-3479 Medium < 0.1% (3rd) < 0.1 libpython3.12-minimal 3.12.3-1ubuntu0.13 deb CVE-2026-3479 Medium...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Feature]: Update default Python version in pre-built docker images feature request ### 🚀 The feature, motivation and pitch Since vLLM==0.20.0 now supports Python 3.14, are there plans to update the default python versi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ature]: Update default Python version in pre-built docker images feature request ### 🚀 The feature, motivation and pitch Since vLLM==0.20.0 now supports Python 3.14, are there plans to update the default python version...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
