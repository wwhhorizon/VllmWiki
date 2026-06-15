# vllm-project/vllm#28916: [Bug]: @create_new_process_for_each_test("spawn") succeed unconditionally and does not work correctly all usages need to be revistied.

| 字段 | 值 |
| --- | --- |
| Issue | [#28916](https://github.com/vllm-project/vllm/issues/28916) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: @create_new_process_for_each_test("spawn") succeed unconditionally and does not work correctly all usages need to be revistied.

### Issue 正文摘录

### Your current environment NA ### 🐛 Describe the bug @create_new_process_for_each_test("spawn") calls python .. main function, tests using it will succeed even though no test is running lol

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ionally and does not work correctly all usages need to be revistied. bug;stale ### Your current environment NA ### 🐛 Describe the bug @create_new_process_for_each_test("spawn") calls python .. main function, tests using...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Bug]: @create_new_process_for_each_test("spawn") succeed unconditionally and does not work correctly all usages need to be revistied. bug;stale ### Your current environment NA ### 🐛 Describe the bug @create_new_process...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
