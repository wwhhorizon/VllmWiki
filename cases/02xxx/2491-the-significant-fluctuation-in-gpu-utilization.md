# vllm-project/vllm#2491: The significant fluctuation in GPU utilization

| 字段 | 值 |
| --- | --- |
| Issue | [#2491](https://github.com/vllm-project/vllm/issues/2491) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> The significant fluctuation in GPU utilization

### Issue 正文摘录

Compared to other frameworks, vllm cannot maintain a high GPU utilization rate consistently. When running llama2 70b on the A800 platform, the utilization rate significantly fluctuates between 0-100 And this leads to limited throughput performance.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: m cannot maintain a high GPU utilization rate consistently. When running llama2 70b on the A800 platform, the utilization rate significantly fluctuates between 0-100 And this leads to limited throughput performance.
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: on rate significantly fluctuates between 0-100 And this leads to limited throughput performance.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
