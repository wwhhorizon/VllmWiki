# vllm-project/vllm#19335: [Installation]: Nightly builds not available in container registry

| 字段 | 值 |
| --- | --- |
| Issue | [#19335](https://github.com/vllm-project/vllm/issues/19335) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Nightly builds not available in container registry

### Issue 正文摘录

### Your current environment Is it possible for nightly builds to be published to the container registry? https://hub.docker.com/r/vllm/vllm-openai/tags According to this issue, it seems like nightly (ish) wheels are available: https://github.com/vllm-project/vllm/issues/4949 It would be very convenient to do the same for the Docker images. I have tried to build myself by pulling master and performing `sudo podman build -t vllm -f docker/Dockerfile --target vllm-openai .` But this 1) takes a VERY long time and 2) ultimately fails with a CUDA error. Of course, the build failure is the fault of my machine/environment, not VLLM, but I'm saying the pain could be entirely eliminated if nightly images were available. ### How you are installing vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Nightly builds not available in container registry installation ### Your current environment Is it possible for nightly builds to be published to the container registry? https://hub.docker.com/r/vllm/vll
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ai .` But this 1) takes a VERY long time and 2) ultimately fails with a CUDA error. Of course, the build failure is the fault of my machine/environment, not VLLM, but I'm saying the pain could be entirely eliminated if...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development ci_build cuda build_error Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
