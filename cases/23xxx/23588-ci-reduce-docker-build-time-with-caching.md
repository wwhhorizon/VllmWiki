# vllm-project/vllm#23588: [CI]: Reduce docker build time with caching

| 字段 | 值 |
| --- | --- |
| Issue | [#23588](https://github.com/vllm-project/vllm/issues/23588) |
| 状态 | closed |
| 标签 | ci/build;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [CI]: Reduce docker build time with caching

### Issue 正文摘录

The build image stage currently takes ~40 minutes and most other tests can't start until this is complete. We should ensure rarely-changing parts/layers are cached, with changes to the layer arrangement to accommodate this if necessary. In particular if there are no changes to dependencies or C++/cuda code (e.g. if the changes are only docs and/or python files), the update should be equivalent to overlaying just the changed files within the file structure in the container which should in theory take seconds. The vast majority of PRs are in this category - we should get to the point where the image setup time is < 1min for these.

## 现有链接修复摘要

#20988 [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [CI]: Reduce docker build time with caching ci/build;stale The build image stage currently takes ~40 minutes and most other tests can't start until this is complete. We should ensure rarely-changing parts/layers are cach
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: necessary. In particular if there are no changes to dependencies or C++/cuda code (e.g. if the changes are only docs and/or python files), the update should be equivalent to overlaying just the changed files within the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [CI]: Reduce docker build time with caching ci/build;stale The build image stage currently takes ~40 minutes and most other tests can't start until this is complete. We should ensure rarely-changing parts/layers are cac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: d;stale The build image stage currently takes ~40 minutes and most other tests can't start until this is complete. We should ensure rarely-changing parts/layers are cached, with changes to the layer arrangement to accom...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#20988](https://github.com/vllm-project/vllm/pull/20988) | mentioned | 0.6 | [CI] [Doc]: Add GH Action for auto labeling issues with `rocm` tag | nvestigate use of CPU backend for subset of tests... [ci/build] 22. #23588: [CI]: Reduce docker build time with caching... [ci/build] 23. #23587: [Bug]: NIXL Crashes if P/D Protoc… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
