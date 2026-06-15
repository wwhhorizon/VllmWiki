# vllm-project/vllm#9129: [Misc]: CMake Clean-up / Refactor Tasks

| 字段 | 值 |
| --- | --- |
| Issue | [#9129](https://github.com/vllm-project/vllm/issues/9129) |
| 状态 | open |
| 标签 | help wanted;good first issue;keep-open;unstale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Misc]: CMake Clean-up / Refactor Tasks

### Issue 正文摘录

In an effort to make the CMake more readable, stable and easy to use we have a few tasks we'd like to work on, creating a GitHub issue here to track that progress, some planned changes/investigations: - [ ] Rename `define_gpu_extension_target`, currently this is used for CPU extensions too so the name is now misleading - [ ] Add a CI test of local builds, i.e. `pip install -e .` - [ ] Warn that PTX builds are not currently supported (post https://github.com/vllm-project/vllm/pull/8845), currently if there is a `+PTX` in `TORCH_CUDA_ARCH_LIST` this will be ignored. We should warn when this is the case. Alternatively we can add support for PTX builds although this is generally not desirable since PTX increases the wheel size by quite a bit (PTX is larger than SASS), and we already build for all currently supported arches. - [ ] Have vllm-flash-attn use [ExternalProject](https://cmake.org/cmake/help/latest/module/ExternalProject.html) currently vllm-flash-attn uses the parent CMake scope which creates many footguns since it is in a separate repo, using `ExternalProject` will mean that the vllm-flash-attn will be run in a separate CMake scope/process - [ ] It might be even better to r...

## 现有链接修复摘要

#31073 [CI/Build] Add CMake warning for ignored +PTX suffix in TORCH_CUDA_ARCH_LIST | #31481 [CI/Build] Add source build test to catch build failures early | #33878 [CMake] Switch vllm-flash-attn to ExternalProject for separate scope (#9129) | #41432 [CMake] Move _C_stable_libtorch and _rocm_C builds to separate files (#9129) | #42375 [Misc] Warn when CUDA PTX arch flags are ignored

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Misc]: CMake Clean-up / Refactor Tasks help wanted;good first issue;keep-open;unstale In an effort to make the CMake more readable, stable and easy to use we have a few tasks we'd like to work on, creating a GitHub iss...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: m/vllm-project/vllm/pull/8845), currently if there is a `+PTX` in `TORCH_CUDA_ARCH_LIST` this will be ignored. We should warn when this is the case. Alternatively we can add support for PTX builds although this is gener...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: [ ] Look into removing early returns in CMakeLists.txt (potentially move backends into its own files) - [ ] Potential build both C++ and CUDA extensions when building for CUDA and using torch dispatcher to dispatch betw...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: CMake Clean-up / Refactor Tasks help wanted;good first issue;keep-open;unstale In an effort to make the CMake more readable, stable and easy to use we have a few tasks we'd like to work on, creating a GitHub issue here...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: used for CPU extensions too so the name is now misleading - [ ] Add a CI test of local builds, i.e. `pip install -e .` - [ ] Warn that PTX builds are not currently supported (post https://github.com/vllm-project/vllm/pu...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#31073](https://github.com/vllm-project/vllm/pull/31073) | closes_keyword | 0.95 | [CI/Build] Add CMake warning for ignored +PTX suffix in TORCH_CUDA_ARCH_LIST | Closes #9129 (partial) ## Test Plan Configure cmake with `+PTX` in `TORCH_CUDA_ARCH_LIST`: ```bash mkdir build && cd build TORCH_CUDA_ARCH_LIST="8.0+PTX" cmake -G Ninja -DVLLM_P |
| [#31481](https://github.com/vllm-project/vllm/pull/31481) | mentioned | 0.6 | [CI/Build] Add source build test to catch build failures early | build test to catch build failures early ## Purpose Addresses Issue #9129 (Task 2) by adding a new "Source Build Test" to the CI pipeline. 1. **New Buildkite Step**: Adds `Source… |
| [#33878](https://github.com/vllm-project/vllm/pull/33878) | closes_keyword | 0.95 | [CMake] Switch vllm-flash-attn to ExternalProject for separate scope (#9129) | Closes #9129 (partial – item 4) --- <details> <summary> Essential Elements of an Effective PR Description Checklist </summary> - [x] The purpose of the PR, such as "Fix some issu |
| [#41432](https://github.com/vllm-project/vllm/pull/41432) | mentioned | 0.6 | [CMake] Move _C_stable_libtorch and _rocm_C builds to separate files (#9129) | # Why this isn't duplicating an existing PR Two PRs are open against #9129 today, neither overlapping: - **#33878** (jungledesh) — switches `vllm-flash-attn` to ExternalProject; t… |
| [#42375](https://github.com/vllm-project/vllm/pull/42375) | mentioned | 0.6 | [Misc] Warn when CUDA PTX arch flags are ignored | n CUDA PTX arch flags are ignored ## Purpose Addresses one item from #9129: warn when PTX code generation is requested via CUDA architecture flags but vLLM normalizes those global… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
