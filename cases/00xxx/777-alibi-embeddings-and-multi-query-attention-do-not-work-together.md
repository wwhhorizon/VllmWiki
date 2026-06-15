# vllm-project/vllm#777: Alibi embeddings and multi_query_attention do not work together

| 字段 | 值 |
| --- | --- |
| Issue | [#777](https://github.com/vllm-project/vllm/issues/777) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Alibi embeddings and multi_query_attention do not work together

### Issue 正文摘录

I am trying to integrate my experimental model architecture, which uses both `alibi` embeddings and `multi_query_attention`. In comparing outputs from the vllm-integrated model and my underlying model, I notice that the generations do not match if `alibi` and `multi_query_attention` are both turned on. They do match if I turn off `multi_query_attention`. With a larger model, I actually run into nans, and the generation fails. I initialize the attention module as follows: ``` self.attention = PagedAttentionWithALiBi(num_heads, head_dim, scale=scaling, slopes=slopes, num_kv_heads=1) ``` I have narrowed down the discrepancy to the `single_query_cached_kv_attention` call. I don't see any test cases for `PagedAttentionWithAlibi`, so debugging is a little difficult. Any help will be appreciated!

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ionWithAlibi`, so debugging is a little difficult. Any help will be appreciated!
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: lows: ``` self.attention = PagedAttentionWithALiBi(num_heads, head_dim, scale=scaling, slopes=slopes, num_kv_heads=1) ``` I have narrowed down the discrepancy to the `single_query_cached_kv_attention` call. I don't see...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: tion do not work together I am trying to integrate my experimental model architecture, which uses both `alibi` embeddings and `multi_query_attention`. In comparing outputs from the vllm-integrated model and my underlyin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _attention do not work together I am trying to integrate my experimental model architecture, which uses both `alibi` embeddings and `multi_query_attention`. In comparing outputs from the vllm-integrated model and my und...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: crepancy to the `single_query_cached_kv_attention` call. I don't see any test cases for `PagedAttentionWithAlibi`, so debugging is a little difficult. Any help will be appreciated!

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
