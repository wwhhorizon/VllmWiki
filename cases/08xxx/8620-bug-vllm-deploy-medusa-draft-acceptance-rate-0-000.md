# vllm-project/vllm#8620: [Bug]: vllm deploy medusa, draft acceptance rate: 0.000

| 字段 | 值 |
| --- | --- |
| Issue | [#8620](https://github.com/vllm-project/vllm/issues/8620) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm deploy medusa, draft acceptance rate: 0.000

### Issue 正文摘录

### Your current environment vllm==0.6.1 ### Model Input Dumps when i use medusa train, medusa0,medusa1,medusa2 acc has 0.95, train result is ok, but i try vllm to delpoy medusa, deploy is ok, **but test sample result not has accelerate, draft acceptance rate is 0.0** ### 🐛 Describe the bug **Speculative metrics: Draft acceptance rate: 0.000, System efficiency: 0.250, Number of speculative tokens: 3, Number of accepted tokens: 0, Number of draft tokens: 483, Number of emitted tokens: 161.**

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: vllm deploy medusa, draft acceptance rate: 0.000 bug ### Your current environment vllm==0.6.1 ### Model Input Dumps when i use medusa train, medusa0,medusa1,medusa2 acc has 0.95, train result is ok, but i try vll...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: the bug **Speculative metrics: Draft acceptance rate: 0.000, System efficiency: 0.250, Number of speculative tokens: 3, Number of accepted tokens: 0, Number of draft tokens: 483, Number of emitted tokens: 161.**
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: cceptance rate: 0.000 bug ### Your current environment vllm==0.6.1 ### Model Input Dumps when i use medusa train, medusa0,medusa1,medusa2 acc has 0.95, train result is ok, but i try vllm to delpoy medusa, deploy is ok,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ain result is ok, but i try vllm to delpoy medusa, deploy is ok, **but test sample result not has accelerate, draft acceptance rate is 0.0** ### 🐛 Describe the bug **Speculative metrics: Draft acceptance rate: 0.000, Sy...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
