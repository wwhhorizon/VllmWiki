# vllm-project/vllm#17336: [Bug]: Several parameters in model Qwen3 and Qwen3MoE should be modified accordingly.

| 字段 | 值 |
| --- | --- |
| Issue | [#17336](https://github.com/vllm-project/vllm/issues/17336) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Several parameters in model Qwen3 and Qwen3MoE should be modified accordingly.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Current parameters of MoE Qwen3 is not entirely match that in huggingface. e.g. theta should be 100,000 instead of 10000. ```python class Qwen3MoeAttention(nn.Module): def __init__( self, hidden_size: int, num_heads: int, num_kv_heads: int, rope_theta: float = 10000, rope_scaling: Optional[Dict[str, Any]] = None, max_position_embeddings: int = 8192, head_dim: Optional[int] = None, rms_norm_eps: float = 1e-06, qkv_bias: bool = False, cache_config: Optional[CacheConfig] = None, quant_config: Optional[QuantizationConfig] = None, prefix: str = "", ) -> None: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Several parameters in model Qwen3 and Qwen3MoE should be modified accordingly. bug ### Your current environment ### 🐛 Describe the bug Current parameters of MoE Qwen3 is not entirely match that in huggingface. e....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ool = False, cache_config: Optional[CacheConfig] = None, quant_config: Optional[QuantizationConfig] = None, prefix: str = "", ) -> None: ``` ### Before submitting a new issue... - [x] Make sure you already searched for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: = None, rms_norm_eps: float = 1e-06, qkv_bias: bool = False, cache_config: Optional[CacheConfig] = None, quant_config: Optional[QuantizationConfig] = None, prefix: str = "", ) -> None: ``` ### Before submitting a new is...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Several parameters in model Qwen3 and Qwen3MoE should be modified accordingly. bug ### Your current environment ### 🐛 Describe the bug Current parameters of MoE Qwen3 is not entirely match that in huggingface. e....

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
