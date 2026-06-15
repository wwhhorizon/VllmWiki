# vllm-project/vllm#28642: [Feature][P0]:  Enable BuildKit Remote Cache in CI

| 字段 | 值 |
| --- | --- |
| Issue | [#28642](https://github.com/vllm-project/vllm/issues/28642) |
| 状态 | closed |
| 标签 | feature request;ci/build;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P0]:  Enable BuildKit Remote Cache in CI

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description The CI currently builds images from scratch on every run because there's no remote cache configured. BuildKit supports registry-based caching that can dramatically speed up builds by reusing layers across different build agents. ### What You'll Do 1. Create ECR repository for BuildKit cache: `vllm-ci-cache` 2. Update Terraform to grant ECR cache access to build agents 3. Modify `test-template-ci.j2` to use `docker buildx` with cache flags: - `--cache-from type=registry,ref=...` - `--cache-to type=registry,ref=...,mode=max` 4. Test cache behavior across multiple builds 5. Set up cache cleanup/retention policies ### Deliverables - [ ] ECR repository created and configured - [ ] Terraform IAM policies updated - [ ] Modified `test-template-ci.j2` with buildx commands ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature][P0]: Enable BuildKit Remote Cache in CI feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description The CI currently builds images from scratch on every run because there's no remote...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature][P0]: Enable BuildKit Remote Cache in CI feature request;ci/build;stale ### 🚀 The feature, motivation and pitch ### Description The CI currently builds images from scratch on every run because there's no remote...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: builds images from scratch on every run because there's no remote cache configured. BuildKit supports registry-based caching that can dramatically speed up builds by reusing layers across different build agents. ### Wha...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 2. Update Terraform to grant ECR cache access to build agents 3. Modify `test-template-ci.j2` to use `docker buildx` with cache flags: - `--cache-from type=registry,ref=...` - `--cache-to type=registry,ref=...,mode=max`...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
