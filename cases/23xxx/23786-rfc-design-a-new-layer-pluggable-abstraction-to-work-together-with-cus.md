# vllm-project/vllm#23786: [RFC]: Design a new Layer-Pluggable abstraction to work together with CustomOp

| 字段 | 值 |
| --- | --- |
| Issue | [#23786](https://github.com/vllm-project/vllm/issues/23786) |
| 状态 | closed |
| 标签 | RFC;keep-open;vllm-ir |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Design a new Layer-Pluggable abstraction to work together with CustomOp

### Issue 正文摘录

### Motivation. In the current vllm, when various layers of different models require different implementations for various platforms, the plugin mechanism of `CustomOp` is used for extension. This mechanism was introduced in [PR 5255](https://github.com/vllm-project/vllm/pull/5255) to address issues with custom layers and has performed excellently at smaller granularity levels such as **RoPE**, **LayerNorm**, and **activation layers**. However, with the growth of the community, an increasing number of model layers also need to support customized implementations through the plugin mechanism, including many larger-grained layers such as high-level model layers like **FusedMoE** and **DeepseekV2MLAAttention** (An example of MLA layer requiring platform-specific customization can be found in #23332 ). If `CustomOp` is used to implement the plugin mechanism for all these layers, it will blur the original positioning of `CustomOp`. Based on the above observations, we propose redefining `CustomOp` while introducing a new `CustomLayer` abstraction to work alongside `CustomOp`, addressing a broader range of application scenarios. Overall, our definitions of `CustomOp` and `CustomLayer` are...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: r ### Motivation. In the current vllm, when various layers of different models require different implementations for various platforms, the plugin mechanism of `CustomOp` is used for extension. This mechanism was introd...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: quire different implementations for various platforms, the plugin mechanism of `CustomOp` is used for extension. This mechanism was introduced in [PR 5255](https://github.com/vllm-project/vllm/pull/5255) to address issu...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: g many larger-grained layers such as high-level model layers like **FusedMoE** and **DeepseekV2MLAAttention** (An example of MLA layer requiring platform-specific customization can be found in #23332 ). If `CustomOp` is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: *DeepseekV2MLAAttention** (An example of MLA layer requiring platform-specific customization can be found in #23332 ). If `CustomOp` is used to implement the plugin mechanism for all these layers, it will blur the origi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ModelConfig, cache_config: Optional[CacheConfig] = None, quant_config: Optional[QuantizationConfig] = None, enable_eplb: bool = False, ) -> None: ... if model_config.use_mla: # modified here attn_cls = CustomMLA else:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
