# vllm-project/vllm#14940: [Feature]: a new attention adaptation

| 字段 | 值 |
| --- | --- |
| Issue | [#14940](https://github.com/vllm-project/vllm/issues/14940) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: a new attention adaptation

### Issue 正文摘录

### 🚀 The feature, motivation and pitch ``` class GatedLinearAttention(nn.Module): r""" The layer implementaion for [Gated Linear Attention Transformers with Hardware-Efficient Training](https://arxiv.org/abs/2312.06635). # noqa Args: mode (str, Optional): Which GLA kernel to use. Currently available: `chunk`, `fused_recurrent`, and `fused_chunk`. Default: `chunk`. hidden_size (int, Optional): The hidden size of the input. Default: 1024. expand_k (float, Optional): The expansion ratio for the key dim. Default: 0.5. expand_v (float, Optional): The expansion ratio for the value dim. Default: 1.0. num_heads (int, Optional): The number of heads. Default: 4. num_kv_heads (int, Optional): The number of key/value heads, used for MQA. Default: None. feature_map (str, Optional): Feature map function applied to queries/keys. Default: None. use_short_conv (bool, Optional): Whether to use short convolutions. Default: `False`. conv_size (int, Optional): The kernel size of the short convolution, only used when `use_short_conv` is `True`. Default: 4. conv_bias (bool, Optional): Whether to use bias in the short convolution, only used when `use_short_conv` is `True`. Default: `False`. use_output_g...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ialize_weights(self, module: nn.Module): if getattr(module, "_is_hf_initialized", False): return if isinstance(module, nn.Linear): nn.init.xavier_uniform_(module.weight, gain=2 ** -2.5) if module.bias is not None: nn.in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: a new attention adaptation feature request;stale ### 🚀 The feature, motivation and pitch ``` class GatedLinearAttention(nn.Module): r""" The layer implementaion for [Gated Linear Attention Transformers with H...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ensor, Optional[torch.Tensor], Optional[Cache]]: # launching the triton kernel for just one token will actually be slower mode = 'fused_recurrent' if hidden_states.shape[1] == 1 else self.mode last_state = past_key_valu...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: implementaion for [Gated Linear Attention Transformers with Hardware-Efficient Training](https://arxiv.org/abs/2312.06635). # noqa Args: mode (str, Optional): Which GLA kernel to use. Currently available: `chunk`, `fuse...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
