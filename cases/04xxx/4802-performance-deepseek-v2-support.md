# vllm-project/vllm#4802: [Performance]: Deepseek-v2  support

| 字段 | 值 |
| --- | --- |
| Issue | [#4802](https://github.com/vllm-project/vllm/issues/4802) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Deepseek-v2  support

### Issue 正文摘录

### Proposal to improve performance I implement the newest Deepseek-v2 model(which is a MOE with 236B parameter, 21B activated) and it's relatively slow, what else should be optimized ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ```

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: MOE with 236B parameter, 21B activated) and it's relatively slow, what else should be optimized ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current enviro...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ### Proposal to improve performance I implement the newest Deepseek-v2 model(which is a MOE with 236B parameter, 21B activated) and it's relatively slow, what else should be optimized ### Report of performance regressio...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: improve performance I implement the newest Deepseek-v2 model(which is a MOE with 236B parameter, 21B activated) and it's relatively slow, what else should be optimized ### Report of performance regression _No response_...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: elatively slow, what else should be optimized ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The o...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
