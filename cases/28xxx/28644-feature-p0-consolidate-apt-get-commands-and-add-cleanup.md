# vllm-project/vllm#28644: [Feature][P0]:  Consolidate apt-get Commands and Add Cleanup

| 字段 | 值 |
| --- | --- |
| Issue | [#28644](https://github.com/vllm-project/vllm/issues/28644) |
| 状态 | closed |
| 标签 | feature request;ci/build |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P0]:  Consolidate apt-get Commands and Add Cleanup

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description The Dockerfile calls `apt-get update` multiple times across different stages (4+ times), downloading package lists repeatedly. Additionally, installed packages include "recommended" packages (not needed), and `/var/lib/apt/lists/` is not cleaned up, leaving ~200MB of package metadata in the image. ### What You'll Do 1. Identify all `apt-get` commands in Dockerfile 2. Consolidate installations within each stage into single RUN commands 3. Add `--no-install-recommends` flag to all apt-get install commands 4. Add `rm -rf /var/lib/apt/lists/*` cleanup after each apt-get 5. Merge GCC-10 installation into the initial apt-get in base stage 6. Document package requirements for maintainability ### Deliverables - [ ] Modified Dockerfile with consolidated apt-get commands - [ ] All apt-get using `--no-install-recommends` - [ ] Cleanup commands added after each apt-get - [ ] Documentation of required vs. optional packages - [ ] Before/after measurements ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot li...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ture][P0]: Consolidate apt-get Commands and Add Cleanup feature request;ci/build ### 🚀 The feature, motivation and pitch ### Description The Dockerfile calls `apt-get update` multiple times across different stages (4+ t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: , and `/var/lib/apt/lists/` is not cleaned up, leaving ~200MB of package metadata in the image. ### What You'll Do 1. Identify all `apt-get` commands in Dockerfile 2. Consolidate installations within each stage into sin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][P0]: Consolidate apt-get Commands and Add Cleanup feature request;ci/build ### 🚀 The feature, motivation and pitch ### Description The Dockerfile calls `apt-get update` multiple times across different stages (...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
