# vllm-project/vllm#3987: [Feature]: Upgrade to PyTorch 2.2.2, Xformers to latest `v0.0.25.post1`

| 字段 | 值 |
| --- | --- |
| Issue | [#3987](https://github.com/vllm-project/vllm/issues/3987) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Upgrade to PyTorch 2.2.2, Xformers to latest `v0.0.25.post1`

### Issue 正文摘录

### 🚀 The feature, motivation and pitch The Xformers release that vLLM is pinned to requires PyTorch 2.1.2. I have the need to use at least 2.2.1. As such, I am submitting this issue with the request to upgrade Xformers to `v0.0.25.post1` which uses `torch==2.2.2`. There's a PR incoming. However, I am not able to get some of the tests to run locally, probably due to an issue with my environment. I am eager to see what the test output is in the CI environment. ### Alternatives _No response_ ### Additional context _No response_

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ue with my environment. I am eager to see what the test output is in the CI environment. ### Alternatives _No response_ ### Additional context _No response_
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e]: Upgrade to PyTorch 2.2.2, Xformers to latest `v0.0.25.post1` feature request ### 🚀 The feature, motivation and pitch The Xformers release that vLLM is pinned to requires PyTorch 2.1.2. I have the need to use at leas...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Feature]: Upgrade to PyTorch 2.2.2, Xformers to latest `v0.0.25.post1` feature request ### 🚀 The feature, motivation and pitch The Xformers release that vLLM is pinned to requires PyTorch 2.1.2. I have the need to use...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
