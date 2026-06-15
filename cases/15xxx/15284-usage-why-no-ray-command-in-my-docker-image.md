# vllm-project/vllm#15284: [Usage]: why no ray command in my docker image

| 字段 | 值 |
| --- | --- |
| Issue | [#15284](https://github.com/vllm-project/vllm/issues/15284) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: why no ray command in my docker image

### Issue 正文摘录

### Your current environment no need ### How would you like to use vllm I want to Distributed Inference and Serving whit CPU only . I build the docker image refer to https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#build-image-from-source, but there is no ray command in the image. Did Ray support in CPU mode Now ? ![Image](https://github.com/user-attachments/assets/e590304c-5885-441d-a16b-bd432694ce5f) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: why no ray command in my docker image usage;stale ### Your current environment no need ### How would you like to use vllm I want to Distributed Inference and Serving whit CPU only . I build the docker image ref...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 5f) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: why no ray command in my docker image usage;stale ### Your current environment no need ### How would you like to use vllm I want to Distributed Inference and Serving whit CPU only . I build the docker image ref...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: t CPU only . I build the docker image refer to https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#build-image-from-source, but there is no ray command in the image. Did Ray support in CPU mode Now ? ![...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
