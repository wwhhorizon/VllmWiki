# vllm-project/vllm#670: LightLLM benchmark

| 字段 | 值 |
| --- | --- |
| Issue | [#670](https://github.com/vllm-project/vllm/issues/670) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> LightLLM benchmark

### Issue 正文摘录

Hi vLLM genius @zhuohan123 @WoosukKwon I find a new project https://github.com/ModelTC/lightllm After reading their [blog](https://mp.weixin.qq.com/s/-wMLMGAHkxeyDYkixqni9Q), the performance advantage on the 7b model is not very obvious, but the gap is larger on the 65b. We will also do some verification and comparison later. The reason for bringing up this issue is to hope that we may see what the LightLLM does well, so that we can refer to and port similar optimizations to vLLM. Cheers.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: enius @zhuohan123 @WoosukKwon I find a new project https://github.com/ModelTC/lightllm After reading their [blog](https://mp.weixin.qq.com/s/-wMLMGAHkxeyDYkixqni9Q), the performance advantage on the 7b model is not very...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: LightLLM benchmark feature request Hi vLLM genius @zhuohan123 @WoosukKwon I find a new project https://github.com/ModelTC/lightllm After reading their [blog](https://mp.weixin.qq.com/s/-wMLMGAHkxeyDYkixqni9Q), the perfo...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: LightLLM benchmark feature request Hi vLLM genius @zhuohan123 @WoosukKwon I find a new project https://github.com/ModelTC/lightllm After reading their [blog](https://mp.weixin.qq.com/s/-wMLMGAHkxeyDYkixqni9Q), the perfo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
