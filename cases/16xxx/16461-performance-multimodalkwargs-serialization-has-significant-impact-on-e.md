# vllm-project/vllm#16461: [Performance]: MultiModalKwargs serialization has significant impact on E2E latency (w/ proof-of-concept patch)

| 字段 | 值 |
| --- | --- |
| Issue | [#16461](https://github.com/vllm-project/vllm/issues/16461) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: MultiModalKwargs serialization has significant impact on E2E latency (w/ proof-of-concept patch)

### Issue 正文摘录

### Proposal to improve performance Through testing, it seems that the serialization of MultiModalKwargs is having a significant impact on multimodal inference performance. This is due to nested torch.tensor objects in the hierarchy of the dictionary of MultiModalKwargs. Although there is special treatment for pure torch.tensor objects in custom_enc_hook, this does not extend to objects that nest torch.tensor, thus the reason for the slowdown. I have not yet been able to compare the performance of the other patch ( https://github.com/vllm-project/vllm/pull/16432 ) regarding MultiModalKwargs memory usage due to compiling issues, but will provide figures later if possible. Also as this focuses primarily on E2E latency and/or throughput I have decided to post this as a separate issue. I have attached a diff (as well as the entire patched serial_utils.py) that converts the tensors in MultiModalKwargs (including ones inside 'field') to numpy or pure python integers. I have seen roughly 10x+ improvement in pickle speed by doing so. This patch is probably very incomplete mostly due to my lack of knowledge of vLLM internals and thus I would like this to serve merely as a proof of concept...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: rformance]: MultiModalKwargs serialization has significant impact on E2E latency (w/ proof-of-concept patch) performance;stale ### Proposal to improve performance Through testing, it seems that the serialization of Mult...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: rence performance. This is due to nested torch.tensor objects in the hierarchy of the dictionary of MultiModalKwargs. Although there is special treatment for pure torch.tensor objects in custom_enc_hook, this does not e...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: MultiModalKwargs serialization has significant impact on E2E latency (w/ proof-of-concept patch) performance;stale ### Proposal to improve performance Through testing, it seems that the serialization of M...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ignificant impact on E2E latency (w/ proof-of-concept patch) performance;stale ### Proposal to improve performance Through testing, it seems that the serialization of MultiModalKwargs is having a significant impact on m...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: he hierarchy of the dictionary of MultiModalKwargs. Although there is special treatment for pure torch.tensor objects in custom_enc_hook, this does not extend to objects that nest torch.tensor, thus the reason for the s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
