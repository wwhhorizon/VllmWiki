# vllm-project/vllm#14756: [Usage]: where to find cpu vllm formal image

| 字段 | 值 |
| --- | --- |
| Issue | [#14756](https://github.com/vllm-project/vllm/issues/14756) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: where to find cpu vllm formal image

### Issue 正文摘录

### Your current environment hi, according to issue https://github.com/vllm-project/vllm/pull/11261 that was merged, there should be a public vllm-cpu image. where can I find this image? I can find vllm-cpu images that personal people built, like https://hub.docker.com/r/thecmrfrd/vllm-cpu or https://hub.docker.com/r/konstantinvernermaif/vllm-cpu but I'm looking for the formal image and I'm unable to find it. ### How would you like to use vllm I want to run inference ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: I can find vllm-cpu images that personal people built, like https://hub.docker.com/r/thecmrfrd/vllm-cpu or https://hub.docker.com/r/konstantinvernermaif/vllm-cpu but I'm looking for the formal image and I'm unable to fi...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ce ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
