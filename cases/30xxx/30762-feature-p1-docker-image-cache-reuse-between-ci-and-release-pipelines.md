# vllm-project/vllm#30762: [Feature][P1]:  docker image / cache reuse between CI and release pipelines

| 字段 | 值 |
| --- | --- |
| Issue | [#30762](https://github.com/vllm-project/vllm/issues/30762) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Feature][P1]:  docker image / cache reuse between CI and release pipelines

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Now the CI and release pipelines are using the same dockerfile with different arguments. For example, * CI - build image: `docker buildx build --file docker/Dockerfile --build-arg max_jobs=16 --build-arg buildkite_commit=0d0c929f2360cde5bae6817ad0f555641329e79d --build-arg USE_SCCACHE=1 --build-arg TORCH_CUDA_ARCH_LIST="8.0 8.9 9.0 10.0" --build-arg FI_TORCH_CUDA_ARCH_LIST="8.0 8.9 9.0a 10.0a" --build-arg VLLM_USE_PRECOMPILED=0 [REDACTED: CACHE RELATED] --tag public.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:0d0c929f2360cde5bae6817ad0f555641329e79d --tag public.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:latest --push --target test --progress plain .` * release - cuda 12.9 wheel: `DOCKER_BUILDKIT=1 docker build --build-arg max_jobs=16 --build-arg USE_SCCACHE=1 --build-arg GIT_REPO_CHECK=1 --build-arg CUDA_VERSION=12.9.1 --tag vllm-ci:build-image --target build --progress plain -f docker/Dockerfile .` If we ignore some caching-related arguments, they seem to differ only on CUDA versions / architectures. I wonder whether we could unify them and leverage the existing caching mechanism when possible (maybe adding some inter-pipeline dependencies, which...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Feature][P1]: docker image / cache reuse between CI and release pipelines feature request;stale ### 🚀 The feature, motivation and pitch Now the CI and release pipelines are using the same dockerfile with different argu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: cde5bae6817ad0f555641329e79d --build-arg USE_SCCACHE=1 --build-arg TORCH_CUDA_ARCH_LIST="8.0 8.9 9.0 10.0" --build-arg FI_TORCH_CUDA_ARCH_LIST="8.0 8.9 9.0a 10.0a" --build-arg VLLM_USE_PRECOMPILED=0 [REDACTED: CACHE REL...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 1]: docker image / cache reuse between CI and release pipelines feature request;stale ### 🚀 The feature, motivation and pitch Now the CI and release pipelines are using the same dockerfile with different arguments. For...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ad0f555641329e79d --tag public.ecr.aws/q9t5s3a7/vllm-ci-postmerge-repo:latest --push --target test --progress plain .` * release - cuda 12.9 wheel: `DOCKER_BUILDKIT=1 docker build --build-arg max_jobs=16 --build-arg USE...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
