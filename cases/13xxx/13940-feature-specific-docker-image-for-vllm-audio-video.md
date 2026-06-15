# vllm-project/vllm#13940: [Feature]: Specific Docker Image for vllm["audio,video"]

| 字段 | 值 |
| --- | --- |
| Issue | [#13940](https://github.com/vllm-project/vllm/issues/13940) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: Specific Docker Image for vllm["audio,video"]

### Issue 正文摘录

### 🚀 The feature, motivation and pitch I am using the `audio` and `video` parts of the vllm package, specifically to write guides. I understand [why it is a separate package](https://github.com/vllm-project/vllm/issues/8030#), and I understand [how to make the dockerfile to create the image that we need with the right dependencies installed](https://docs.vllm.ai/en/latest/deployment/docker.html). However, I'd like to have 0 ops in terms of keeping this image up to date + many cloud deployment tools assume users only need images from dockerhub . Could you all have a `vllm/vllm-openai-audio-video` image on the hub that users could pull directly? Having it automatically sync'ed with `latest` would increase access and ability to write about new features. I'd be happy to potentially write the dockerfile myself if there is interest in the proposal. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature]: Specific Docker Image for vllm["audio,video"] feature request;stale ### 🚀 The feature, motivation and pitch I am using the `audio` and `video` parts of the vllm package, specifically to write guides. I unders...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: Specific Docker Image for vllm["audio,video"] feature request;stale ### 🚀 The feature, motivation and pitch I am using the `audio` and `video` parts of the vllm package, specifically to write guides. I unders...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: we need with the right dependencies installed](https://docs.vllm.ai/en/latest/deployment/docker.html). However, I'd like to have 0 ops in terms of keeping this image up to date + many cloud deployment tools assume users...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
