# vllm-project/vllm#31450: [Feature]: vLLM should apply to Docker Open Source Program for removing image pull limits

| 字段 | 值 |
| --- | --- |
| Issue | [#31450](https://github.com/vllm-project/vllm/issues/31450) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vLLM should apply to Docker Open Source Program for removing image pull limits

### Issue 正文摘录

### 🚀 The feature, motivation and pitch https://docs.docker.com/docker-hub/repos/manage/trusted-content/dsos-program/ https://www.docker.com/community/open-source/application/ I believe that the vLLM Docker organization should apply for the OSS Program to gain a higher image pull quota/higher rate limit for everyone pulling the vLLM images. It's very slow compared to SGLang, which receives the program. Moreover, perhaps pushing to the GitHub Container Registry (`ghcr.io`) as well should also be considered. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Feature]: vLLM should apply to Docker Open Source Program for removing image pull limits feature request ### 🚀 The feature, motivation and pitch https://docs.docker.com/docker-hub/repos/manage/trusted-content/dsos-prog...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ply to Docker Open Source Program for removing image pull limits feature request ### 🚀 The feature, motivation and pitch https://docs.docker.com/docker-hub/repos/manage/trusted-content/dsos-program/ https://www.docker.c...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
