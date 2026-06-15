# vllm-project/vllm#28645: [Feature][P1]:  Remove Duplicate Python Installation

| 字段 | 值 |
| --- | --- |
| Issue | [#28645](https://github.com/vllm-project/vllm/issues/28645) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P1]:  Remove Duplicate Python Installation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description Python 3.12 is fully installed in the `base` stage, but then the `vllm-base` stage reinstalls Python from scratch using the deadsnakes PPA. This is redundant and wastes build time. We should copy Python from the base stage instead. ### What You'll Do 1. Analyze Python installation in base stage (lines 86-98) 2. Identify what needs to be copied to vllm-base stage: - `/opt/venv/` (virtual environment) - `/usr/bin/python3*` (binaries) - `/usr/lib/python3.12/` (libraries) - `/root/.local/` (uv installation) 3. Replace Python installation in vllm-base with COPY commands 4. Ensure all Python functionality works in final image 5. Update PATH and environment variables ### Deliverables - [ ] Modified Dockerfile with Python copied from base stage - [ ] Removed redundant Python installation code - [ ] Environment variables properly set - [ ] Validation that Python and pip work correctly - [ ] Build time measurements ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Feature][P1]: Remove Duplicate Python Installation feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Python 3.12 is fully installed in the `base` stage, but then the `vllm-base` sta...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][P1]: Remove Duplicate Python Installation feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description Python 3.12 is fully installed in the `base` stage, but then the `vllm-base` sta...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
