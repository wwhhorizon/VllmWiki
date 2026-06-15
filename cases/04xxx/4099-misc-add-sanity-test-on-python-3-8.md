# vllm-project/vllm#4099: [Misc]: Add sanity test on Python 3.8

| 字段 | 值 |
| --- | --- |
| Issue | [#4099](https://github.com/vllm-project/vllm/issues/4099) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]: Add sanity test on Python 3.8

### Issue 正文摘录

### Anything you want to discuss about vllm. Currently, CI only runs on Python 3.9. For Python > 3.9, there's no problem with this approach because Python guarantees the backward compatibility, but Python 3.8 (which is still the version that's supported) is not properly tested and sometimes caused issue like https://github.com/vllm-project/vllm/pull/4092#issuecomment-2057867553 To solve this issue, we can have a simple sanity check test on Python 3.8.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ython 3.8 stale ### Anything you want to discuss about vllm. Currently, CI only runs on Python 3.9. For Python > 3.9, there's no problem with this approach because Python guarantees the backward compatibility, but Pytho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Misc]: Add sanity test on Python 3.8 stale ### Anything you want to discuss about vllm. Currently, CI only runs on Python 3.9. For Python > 3.9, there's no problem with this approach because Python guarantees the backw...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Misc]: Add sanity test on Python 3.8 stale ### Anything you want to discuss about vllm. Currently, CI only runs on Python 3.9. For Python > 3.9, there's no problem with this approach because Python guarantees the backw...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
