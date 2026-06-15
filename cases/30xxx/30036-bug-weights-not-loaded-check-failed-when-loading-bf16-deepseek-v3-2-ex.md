# vllm-project/vllm#30036: [Bug]: weights_not_loaded check failed when loading bf16 DeepSeek-V3.2-Exp

| 字段 | 值 |
| --- | --- |
| Issue | [#30036](https://github.com/vllm-project/vllm/issues/30036) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: weights_not_loaded check failed when loading bf16 DeepSeek-V3.2-Exp

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug error raised in `vllm/model_executor/model_loader/default_loader.py #Line324` because `weights_to_load` has extra model.layers.{layer_index}.self_attn.indexer.weights_proj.bias in bf16 unquantized scenario. I checked initialization of `self.weights_proj` in `vllm/model_executor/models/deepseek_v2.py` `self.weights_proj` in Indexer initialized with bias not configured, thus leads to default `bias = True` and add bias in weights_proj.bias in `weights_to_load` ``` # vllm/model_executor/models/deepseek_v2.py self.weights_proj = ReplicatedLinear( hidden_size, self.n_head, quant_config=None, prefix=f"{prefix}.weights_proj" ) # vllm.model_executor.layers.linear.ReplicatedLinear def __init__( self, input_size: int, output_size: int, bias: bool = True, skip_bias_add: bool = False, params_dtype: torch.dtype | None = None, quant_config: QuantizationConfig | None = None, prefix: str = "", *, return_bias: bool = True, disable_tp: bool = False, ): ``` check model.py in deepseek `https://github.com/deepseek-ai/DeepSeek-V3.2-Exp/blob/main/inference/model.py` `self.weights_proj` has no bias acutally. maybe we can change ``` # vllm/model_executor/...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: weights_not_loaded check failed when loading bf16 DeepSeek-V3.2-Exp bug;stale ### Your current environment ### 🐛 Describe the bug error raised in `vllm/model_executor/model_loader/default_loader.py #Line324` beca...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rent environment ### 🐛 Describe the bug error raised in `vllm/model_executor/model_loader/default_loader.py #Line324` because `weights_to_load` has extra model.layers.{layer_index}.self_attn.indexer.weights_proj.bias in...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: output_size: int, bias: bool = True, skip_bias_add: bool = False, params_dtype: torch.dtype | None = None, quant_config: QuantizationConfig | None = None, prefix: str = "", *, return_bias: bool = True, disable_tp: bool...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: weights_not_loaded check failed when loading bf16 DeepSeek-V3.2-Exp bug;stale ### Your current environment ### 🐛 Describe the bug error raised in `vllm/model_executor/model_loader/default_loader.py #Line324` because `we...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
