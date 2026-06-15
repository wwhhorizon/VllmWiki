# vllm-project/vllm#8284: [Usage]: Throughput and quality issue with vllm 0.6.0.

| 字段 | 值 |
| --- | --- |
| Issue | [#8284](https://github.com/vllm-project/vllm/issues/8284) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Throughput and quality issue with vllm 0.6.0.

### Issue 正文摘录

As per vllm community, vllm 0.6.0 is improved version with 5x throughput. I have installed vllm==0.6.0 but the throughput remains same as earlier. Also the response quality of output is degraded in this version. Has anyone faced similar issue with this version?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: th vllm 0.6.0. usage;stale As per vllm community, vllm 0.6.0 is improved version with 5x throughput. I have installed vllm==0.6.0 but the throughput remains same as earlier. Also the response quality of output is degrad...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: Throughput and quality issue with vllm 0.6.0. usage;stale As per vllm community, vllm 0.6.0 is improved version with 5x throughput. I have installed vllm==0.6.0 but the throughput remains same as earlier. Also...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Usage]: Throughput and quality issue with vllm 0.6.0. usage;stale As per vllm community, vllm 0.6.0 is improved version with 5x throughput. I have installed vllm==0.6.0 but the throughput remains same as earlier. Also...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
