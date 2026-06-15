# vllm-project/vllm#14581: [Feature][Hardware][TPU]: Improve the token_num padding logic

| 字段 | 值 |
| --- | --- |
| Issue | [#14581](https://github.com/vllm-project/vllm/issues/14581) |
| 状态 | closed |
| 标签 | feature request;tpu |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][Hardware][TPU]: Improve the token_num padding logic

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently the token_num is padded to power of 2. It is quite a waste of computation when token_num is large. In the meantime, in one of our benchmarking, the best max-num-batched-tokens is 512, also according to https://jax-ml.github.io/scaling-book/roofline/, we don't really need max-num-batched-tokens to be very large. Also cudagraph precompiles for [512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,248,240,232,224,216,208,200,192,184,176,168,160,152,144,136,128,120,112,104,96,88,80,72,64,56,48,40,32,24,16,8,4,2,1], we can use a similar padding strategy for TPU. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ne/, we don't really need max-num-batched-tokens to be very large. Also cudagraph precompiles for [512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: e of computation when token_num is large. In the meantime, in one of our benchmarking, the best max-num-batched-tokens is 512, also according to https://jax-ml.github.io/scaling-book/roofline/, we don't really need max-...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: really need max-num-batched-tokens to be very large. Also cudagraph precompiles for [512,504,496,488,480,472,464,456,448,440,432,424,416,408,400,392,384,376,368,360,352,344,336,328,320,312,304,296,288,280,272,264,256,24...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][Hardware][TPU]: Improve the token_num padding logic feature request;tpu ### 🚀 The feature, motivation and pitch Currently the token_num is padded to power of 2. It is quite a waste of computation when token_nu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
