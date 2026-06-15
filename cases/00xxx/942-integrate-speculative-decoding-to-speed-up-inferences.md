# vllm-project/vllm#942: Integrate Speculative decoding to speed up inferences

| 字段 | 值 |
| --- | --- |
| Issue | [#942](https://github.com/vllm-project/vllm/issues/942) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Integrate Speculative decoding to speed up inferences

### Issue 正文摘录

It is already mentioned by @WoosukKwon here: https://github.com/vllm-project/vllm/issues/249#issuecomment-1607908452 that the samplers are not optimized and are a part of the [vLLM roadmap](https://github.com/vllm-project/vllm/issues/244). It will be great if we take a leap forward to incorporate speculative decoding into vLLM. Speculative Decoding is the latest [paper](https://arxiv.org/abs/2211.17192) from DeepMind researchers and they claim to achieve 2-2.5x decoding speedup. There is already an open-source contribution of the technique here: https://github.com/shreyansh26/Speculative-Sampling

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: s the latest [paper](https://arxiv.org/abs/2211.17192) from DeepMind researchers and they claim to achieve 2-2.5x decoding speedup. There is already an open-source contribution of the technique here: https://github.com/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Integrate Speculative decoding to speed up inferences It is already mentioned by @WoosukKwon here: https://github.com/vllm-project/vllm/issues/249#issuecomment-1607908452 that the samplers are not optimized and are a pa...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: corporate speculative decoding into vLLM. Speculative Decoding is the latest [paper](https://arxiv.org/abs/2211.17192) from DeepMind researchers and they claim to achieve 2-2.5x decoding speedup. There is already an ope...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
