# vllm-project/vllm#28915: [Performance]: Diagnose speed difference using spec decode branch

| 字段 | 值 |
| --- | --- |
| Issue | [#28915](https://github.com/vllm-project/vllm/issues/28915) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Diagnose speed difference using spec decode branch

### Issue 正文摘录

### Report of performance regression @litone01 reported a performance regression on the branch of spec decode (https://github.com/vllm-project/vllm/pull/24322), where models run slower than on main even without using spec decode. His branch: https://github.com/litone01/vllm/tree/origin/feature/spec-decode-draft-model-debug This issue is for tracking progress.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Performance]: Diagnose speed difference using spec decode branch performance ### Report of performance regression @litone01 reported a performance regression on the branch of spec decode (https://github.com/vllm-projec...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: of spec decode (https://github.com/vllm-project/vllm/pull/24322), where models run slower than on main even without using spec decode. His branch: https://github.com/litone01/vllm/tree/origin/feature/spec-decode-draft-m...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ifference using spec decode branch performance ### Report of performance regression @litone01 reported a performance regression on the branch of spec decode (https://github.com/vllm-project/vllm/pull/24322), where model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
