# vllm-project/vllm#13032: [Performance]: cutlass_scaled_sparse_mm support per_channel weight ?

| 字段 | 值 |
| --- | --- |
| Issue | [#13032](https://github.com/vllm-project/vllm/issues/13032) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: cutlass_scaled_sparse_mm support per_channel weight ?

### Issue 正文摘录

### Proposal to improve performance cutlass_scaled_sparse_mm support per_channel weight 【? IN func: void cutlass_scaled_sparse_mm(torch::Tensor& c, torch::Tensor const& a, torch::Tensor const& bt_nzs, torch::Tensor const& bt_meta, torch::Tensor const& a_scales, torch::Tensor const& b_scales, std::optional const& bias) { b_scales now is scalar（1，1）。 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: const& bias) { b_scales now is scalar（1，1）。 ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The out...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Performance]: cutlass_scaled_sparse_mm support per_channel weight ? performance ### Proposal to improve performance cutlass_scaled_sparse_mm support per_channel weight 【? IN func: void cutlass_scaled_sparse_mm(torch::T...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Performance]: cutlass_scaled_sparse_mm support per_channel weight ? performance ### Proposal to improve performance cutlass_scaled_sparse_mm support per_channel weight 【? IN func: void cutlass_scaled_sparse_mm(torch::T...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
