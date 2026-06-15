# vllm-project/vllm#8749: [Performance]: Analysis of performance dashboard movements

| 字段 | 值 |
| --- | --- |
| Issue | [#8749](https://github.com/vllm-project/vllm/issues/8749) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Analysis of performance dashboard movements

### Issue 正文摘录

It would be good to have some analysis of recent and ongoing jumps/drops in the various performance dashboard graphs: https://perf.vllm.ai/ Mainly keeping a list of the particular commits that caused non-negligible change in one or more of the tests results. For the regressions we can further look into whether it's expected and if not what can be done to address that particular thing. Otherwise these can be missed because later unrelated changes might make up the difference. Some recent examples: Improvement in serving latency for llama3 8B tp=1, due to MQLLMEngine addition, custom vllm-flash-attention build: ![image](https://github.com/user-attachments/assets/80de3525-be41-45fd-b560-f88b43491073) Possibly unexplained increases in TTFT for high QPS llama 70b tp=4: ![image](https://github.com/user-attachments/assets/1e92eddb-85f8-47ee-870c-8751020d424c)

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: rticular commits that caused non-negligible change in one or more of the tests results. For the regressions we can further look into whether it's expected and if not what can be done to address that particular thing. Ot...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: llama3 8B tp=1, due to MQLLMEngine addition, custom vllm-flash-attention build: ![image](https://github.com/user-attachments/assets/80de3525-be41-45fd-b560-f88b43491073) Possibly unexplained increases in TTFT for high Q...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: e difference. Some recent examples: Improvement in serving latency for llama3 8B tp=1, due to MQLLMEngine addition, custom vllm-flash-attention build: ![image](https://github.com/user-attachments/assets/80de3525-be41-45...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Performance]: Analysis of performance dashboard movements performance;stale It would be good to have some analysis of recent and ongoing jumps/drops in the various performance dashboard graphs: https://perf.vllm.ai/ Ma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
