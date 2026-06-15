# vllm-project/vllm#30655: [Performance]: VLLM with DP performing worst

| 字段 | 值 |
| --- | --- |
| Issue | [#30655](https://github.com/vllm-project/vllm/issues/30655) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: VLLM with DP performing worst

### Issue 正文摘录

### Name of failing test examples/offline_inference/data_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test I have tested DP feature with 4 x A100 card. I observed that vllm with DP 4 and api-server-count = 4 performs poor as compare to 4 x VLLM instances with 1 GPU each . ### 📝 History of failing test NA ### CC List. _No response_

## 候选优化模式

- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ence/data_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing test I have tested DP feature with 4 x...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: rs`) ### 🧪 Describe the failing test I have tested DP feature with 4 x A100 card. I observed that vllm with DP 4 and api-server-count = 4 performs poor as compare to 4 x VLLM instances with 1 GPU each . ### 📝 History of...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: f failing test examples/offline_inference/data_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libraries (e.g. bug in `transformers`) ### 🧪 Describe the failing te...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: formance]: VLLM with DP performing worst performance ### Name of failing test examples/offline_inference/data_parallel.py ### Basic information - [ ] Flaky test - [x] Can reproduce locally - [ ] Caused by external libra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
