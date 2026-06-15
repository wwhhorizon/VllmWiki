# vllm-project/vllm#28643: [Feature][P0]:  Switch to Runtime Base Image

| 字段 | 值 |
| --- | --- |
| Issue | [#28643](https://github.com/vllm-project/vllm/issues/28643) |
| 状态 | closed |
| 标签 | feature request;ci/build |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature][P0]:  Switch to Runtime Base Image

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ### Description The Dockerfile currently uses `nvidia/cuda:12.9.1-devel-ubuntu22.04` as the final base image. The `devel` variant includes the full CUDA compiler toolchain (~7GB) which is only needed during build, not at runtime. Switching to the `runtime` variant will significantly reduce image size. ### What You'll Do 1. Change `FINAL_BASE_IMAGE` from `devel` to `runtime` (line 24) 2. Analyze if any runtime components actually need build tools 3. Handle FlashInfer JIT compilation requirements: - Test if AOT wheels work without build deps - If needed, add conditional minimal build tools 4. Verify all GPU functionality works with runtime image 5. Update documentation ### Deliverables - [ ] Modified Dockerfile with runtime base image - [ ] Conditional build dependency installation for FlashInfer (if needed) - [ ] GPU functionality test results - [ ] Before/after image size comparison ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vll...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Feature][P0]: Switch to Runtime Base Image feature request;ci/build ### 🚀 The feature, motivation and pitch ### Description The Dockerfile currently uses `nvidia/cuda:12.9.1-devel-ubuntu22.04` as the final base image....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ivation and pitch ### Description The Dockerfile currently uses `nvidia/cuda:12.9.1-devel-ubuntu22.04` as the final base image. The `devel` variant includes the full CUDA compiler toolchain (~7GB) which is only needed d...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 2. Analyze if any runtime components actually need build tools 3. Handle FlashInfer JIT compilation requirements: - Test if AOT wheels work without build deps - If needed, add conditional minimal build tools 4. Verify a...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][P0]: Switch to Runtime Base Image feature request;ci/build ### 🚀 The feature, motivation and pitch ### Description The Dockerfile currently uses `nvidia/cuda:12.9.1-devel-ubuntu22.04` as the final base image....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: need build tools 3. Handle FlashInfer JIT compilation requirements: - Test if AOT wheels work without build deps - If needed, add conditional minimal build tools 4. Verify all GPU functionality works with runtime image...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
