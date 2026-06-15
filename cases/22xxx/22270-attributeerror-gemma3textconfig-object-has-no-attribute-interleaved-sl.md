# vllm-project/vllm#22270: AttributeError: 'Gemma3TextConfig' object has no attribute 'interleaved_sliding_window'

| 字段 | 值 |
| --- | --- |
| Issue | [#22270](https://github.com/vllm-project/vllm/issues/22270) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AttributeError: 'Gemma3TextConfig' object has no attribute 'interleaved_sliding_window'

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/59a0b8554bf0e8a9902e14e3d0e564fea38157b6/vllm/model_executor/models/gemma3.py#L151C7-L167C39 In the following logic: `self.sliding_window = (config.interleaved_sliding_window or config.sliding_window) ` If the attribute interleaved_sliding_window does not exist in the config object, this will raise an AttributeError. Even worse, if self.is_sliding is True due to the layer_types condition, the code still assumes config.interleaved_sliding_window exists — which might not be the case. Suggested fix : Replace the line with a safer getattr() call that handles missing attributes gracefully: `self.sliding_window = (getattr(config, "interleaved_sliding_window", None) or config.sliding_window) `

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: AttributeError: 'Gemma3TextConfig' object has no attribute 'interleaved_sliding_window' https://github.com/vllm-project/vllm/blob/59a0b8554bf0e8a9902e14e3d0e564fea38157b6/vllm/model_executor/models/gemma3.py#L151C7-L167...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: AttributeError: 'Gemma3TextConfig' object has no attribute 'interleaved_sliding_window' https://github.com/vllm-project/vllm/blob/59a0b8554bf0e8a9902e14e3d0e564fea38157b6/vllm/model_executor/models/gemma3.py#L151C7-L167...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
