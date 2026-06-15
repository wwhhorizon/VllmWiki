# vllm-project/vllm#2904: _yarn_linear_ramp_mask() missing 1 required positional argument: 'device'

| 字段 | 值 |
| --- | --- |
| Issue | [#2904](https://github.com/vllm-project/vllm/issues/2904) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> _yarn_linear_ramp_mask() missing 1 required positional argument: 'device'

### Issue 正文摘录

In vllm/model_executor/layers/rotary_embedding.py, function `_yarn_linear_ramp_mask` need a parameter device and it doesn't have a default value, but in line:307: `inv_freq_mask = (1 - _yarn_linear_ramp_mask(low, high, self.rotary_dim // 2, dtype=torch.float)) * self.extrapolation_factor` don't use this parameter.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: freq_mask = (1 - _yarn_linear_ramp_mask(low, high, self.rotary_dim // 2, dtype=torch.float)) * self.extrapolation_factor` don't use this parameter.
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ear_ramp_mask() missing 1 required positional argument: 'device' In vllm/model_executor/layers/rotary_embedding.py, function `_yarn_linear_ramp_mask` need a parameter device and it doesn't have a default value, but in l...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
