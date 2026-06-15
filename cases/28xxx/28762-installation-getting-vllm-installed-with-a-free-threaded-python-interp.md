# vllm-project/vllm#28762: [Installation]: getting vLLM installed with a free-threaded Python interpreter (3.14t)

| 字段 | 值 |
| --- | --- |
| Issue | [#28762](https://github.com/vllm-project/vllm/issues/28762) |
| 状态 | open |
| 标签 | installation |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | install |
| Operator 关键词 | attention;cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Installation]: getting vLLM installed with a free-threaded Python interpreter (3.14t)

### Issue 正文摘录

https://x.com/vllm_project/status/1942450223881605593 showed that it's possible to run vLLM in a free-threaded Python interpreter. That involved a lot of custom work to get dependencies to build, and the situation now (4 months later) is a lot better. This is meant as a tracking issue for all the dependencies of vLLM - to start with on Linux x86-64 (CPU and CUDA) - and as a "work list" for getting the remaining issues with those dependencies resolved. With a goal of `uv pip install vllm` to do the right thing out of the box in a clean 3.14t environment. Python 3.14t is necessary, both because CPython 3.14t itself is much more stable than 3.13t and because there are a number of important packages (e.g., `cffi`, `aiohttp`) that do support 3.14t but won't support 3.13t. Of course this depends on vLLM itself supporting Python 3.14 (the default, with-GIL build) first - see ~gh-26994~ gh-34096 for that. This is the dependency graph for vLLM, generated from the default dependencies for the latest release (0.11.0) on PyPI, with packages with compiled code with free-threading wheels on PyPI marked in green and those without in red (easier to browse in a fresh browser tab): ![Image](https:/...

## 现有链接修复摘要

#27933 [docs] Improve wide-EP performance + benchmarking documentation | #29241 [CI/Build]: make it possible to build with a free-threaded interpreter

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Installation]: getting vLLM installed with a free-threaded Python interpreter (3.14t) installation https://x.com/vllm_project/status/1942450223881605593 showed that it's possible to run vLLM in a free-threaded Python i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: And the CUDA-specific dependencies that don't yet have support: - [x] `flashinfer-python`: no upstream issue yet; ~uses stable ABI so doesn't build yet~ resolved by https://github.com/flashinfer-ai/flashinfer/pull/1687...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or all the dependencies of vLLM - to start with on Linux x86-64 (CPU and CUDA) - and as a "work list" for getting the remaining issues with those dependencies resolved. With a goal of `uv pip install vllm` to do the rig...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ndency graph for vLLM, generated from the default dependencies for the latest release (0.11.0) on PyPI, with packages with compiled code with free-threading wheels on PyPI marked in green and those without in red (easie...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: s/56434)) has landed - `ray` was made optional, so this is no longer blocking. ~Ray still doesn't even have regular 3.14 support as of 10 April 2026~ fixed on 22 April 2026. - [x] `xformers`: no support yet, not expecte...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27933](https://github.com/vllm-project/vllm/pull/27933) | mentioned | 0.45 | [docs] Improve wide-EP performance + benchmarking documentation | ] `opencv-python-headless`: no support yet, tracking issue is [opencv#27933](https://github.com/opencv/opencv/issues/27933) - to build from source: clone the repo, check out [open… |
| [#29241](https://github.com/vllm-project/vllm/pull/29241) | mentioned | 0.45 | [CI/Build]: make it possible to build with a free-threaded interpreter | be possible to build vllm itself. prs to get that to work: - [x] [vllm#29241](https://github.com/vllm-project/vllm/pull/29241) - [x] [flash-attention#112](https://github.com/vllm-… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
