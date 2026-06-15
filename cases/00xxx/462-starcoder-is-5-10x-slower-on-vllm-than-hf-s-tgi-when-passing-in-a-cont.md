# vllm-project/vllm#462: Starcoder is 5-10x slower on vllm than HF's TGI when passing in a continuous batch of requests

| 字段 | 值 |
| --- | --- |
| Issue | [#462](https://github.com/vllm-project/vllm/issues/462) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Starcoder is 5-10x slower on vllm than HF's TGI when passing in a continuous batch of requests

### Issue 正文摘录

Hi! We're testing out the new Starcoder implementation [here](https://github.com/vllm-project/vllm/pull/209) (thank you for the contribution @michaelfeil!) and have noticed that it's about 5-10x slower on vllm than HF's text-generation-inference when passing in a batch of requests. Our test is pretty rudimentary, we simply make a series of 10 requests in parallel returning a fixed number of output tokens, and wait for all the results to return. The results are roughly: VLLM: 2000 tokens in 40 seconds, ~50 tokens/s TGI: 2000 tokens in 6 seconds, ~300 tokens/s Is there something we might be doing wrong here?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Starcoder is 5-10x slower on vllm than HF's TGI when passing in a continuous batch of requests bug Hi! We're testing out the new Starcoder implementation [here](https://github.com/vllm-project/vllm/pull/209) (thank you...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: 5-10x slower on vllm than HF's TGI when passing in a continuous batch of requests bug Hi! We're testing out the new Starcoder implementation [here](https://github.com/vllm-project/vllm/pull/209) (thank you for the contr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: n HF's TGI when passing in a continuous batch of requests bug Hi! We're testing out the new Starcoder implementation [here](https://github.com/vllm-project/vllm/pull/209) (thank you for the contribution @michaelfeil!) a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
