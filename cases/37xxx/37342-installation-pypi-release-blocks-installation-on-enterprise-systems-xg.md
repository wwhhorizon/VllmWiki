# vllm-project/vllm#37342: [Installation]: PyPI release blocks installation on enterprise systems: xgrammar==0.1.29 blocked by security scanners (CVE-2026-25048)

| 字段 | 值 |
| --- | --- |
| Issue | [#37342](https://github.com/vllm-project/vllm/issues/37342) |
| 状态 | open |
| 标签 | installation |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: PyPI release blocks installation on enterprise systems: xgrammar==0.1.29 blocked by security scanners (CVE-2026-25048)

### Issue 正文摘录

### Your current environment ## Problem Installing vLLM from PyPI fails in enterprise environments where security scanners or Artifactory policies block vulnerable packages. **Error:** `pip install vllm` tries to install `xgrammar==0.1.29`, which is affected by CVE-2026-25048. The vLLM package requirement was limited to only accept version 0.1.29. ## Request Please release a new vLLM version to PyPI that includes the xgrammar upgrade from [PR #36168] (`xgrammar>=0.1.32`) so that users can install vLLM without pulling in the vulnerable xgrammar version. This fix is already in main; a new PyPI release is needed. ### How you are installing vllm ```sh pip install vllm ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Installation]: PyPI release blocks installation on enterprise systems: xgrammar==0.1.29 blocked by security scanners (CVE-2026-25048) installation ### Your current environment ## Problem Installing vLLM from PyPI fails
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: [Installation]: PyPI release blocks installation on enterprise systems: xgrammar==0.1.29 blocked by security scanners (CVE-2026-25048) installation ### Your current environment ## Problem Installing vLLM from PyPI fails...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: vLLM package requirement was limited to only accept version 0.1.29. ## Request Please release a new vLLM version to PyPI that includes the xgrammar upgrade from [PR #36168] (`xgrammar>=0.1.32`) so that users can install...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
