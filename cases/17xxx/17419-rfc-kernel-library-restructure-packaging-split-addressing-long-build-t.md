# vllm-project/vllm#17419: [RFC]: Kernel Library Restructure / Packaging Split (addressing long build times)

| 字段 | 值 |
| --- | --- |
| Issue | [#17419](https://github.com/vllm-project/vllm/issues/17419) |
| 状态 | open |
| 标签 | RFC;keep-open |
| 评论 | 33; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;frontend_api;hardware_porting |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;operator |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: Kernel Library Restructure / Packaging Split (addressing long build times)

### Issue 正文摘录

### Motivation. ![Reasonable Build Time?](https://github.com/user-attachments/assets/5631421a-9a02-4fd8-ac23-c79f1bca1c07) ## Motivation *vLLM local builds take too long.* On CI the wall clock time for a build (with no cache) exceeds [5 hours](https://buildkite.com/vllm/ci/builds/18094/steps?jid=01965b50-76d2-4a70-9d55-e517017e0a48). For the repository it’s noted that most of the commits to the vllm directory *did* *not* modify the csrc directory, effectively making them python only changes and not requiring extra build time (95% within the last year). It’s also acknowledged in the install from source docs about how long the build time is with most people being pointed towards python only builds as a means to get a reasonable build time to do most of their work. ([link](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#build-wheel-from-source)) As well, I think it’s worth it to consider how we structure the code to make it more clear over what is kernel specific vs. what is engine specific, which could benefit the project by clearly identifying when we would need to run things like performance testing vs. unit testing (i.e. kernel vs. engine). ### Proposed Chang...

## 现有链接修复摘要

#23866 [Build] Split Kernels into Separate `vllm-kernels` package

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [RFC]: Kernel Library Restructure / Packaging Split (addressing long build times) RFC;keep-open ### Motivation. ![Reasonable Build Time?](https://github.com/user-attachments/assets/5631421a-9a02-4fd8-ac23-c79f1bca1c07)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ve? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: e build time to do most of their work. ([link](https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#build-wheel-from-source)) As well, I think it’s worth it to consider how we structure the code to make...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23866](https://github.com/vllm-project/vllm/pull/23866) | mentioned | 0.6 | [Build] Split Kernels into Separate `vllm-kernels` package | in cmake files. ## Purpose This is first step towards implementing #17419. As splitting kernels into a new package involves changes to CI, dev workflow and release new package pro… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
