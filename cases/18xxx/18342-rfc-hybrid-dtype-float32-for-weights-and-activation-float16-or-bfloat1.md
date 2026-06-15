# vllm-project/vllm#18342: [RFC]: hybrid dtype: float32 for weights and activation, float16 or bfloat16 for attention.

| 字段 | 值 |
| --- | --- |
| Issue | [#18342](https://github.com/vllm-project/vllm/issues/18342) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: hybrid dtype: float32 for weights and activation, float16 or bfloat16 for attention.

### Issue 正文摘录

### Motivation. vllm defaults to using float16 inference for float32 models. https://github.com/vllm-project/vllm/blob/275c5daeb0048c3b3f359bb5d9478b1e75e02857/vllm/config.py#L3053C1-L3055C44 ``` # Set default dtype from model config if config_dtype == torch.float32: # Following common practice, we use float16 for float32 models torch_dtype = torch.float16 ``` Most models can maintain their original precision, but a few models require float32. But flash attn does not support float32, making it a very ineffective choice. More reports of embedding model precision significantly decreasing at float16: #17175 #17986 #17785 #15393 .... Wider numerical issues PTAL #17123 ### Proposed Change. This RFC manage to use float32 for weights and activation, float16 or bfloat16 for attention. For models where precision drops significantly at float16, this might be a better choice, especially models that support long context. But previously, kv_cache_dtype defaulting to dtype. If the generation model is to support hybrid dtype, kv_cache_dtype should default to be consistent with attn_dtype., which requires changing many places and can introduce a lot of bugs. So it's better to implement this RPC i...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: [RFC]: hybrid dtype: float32 for weights and activation, float16 or bfloat16 for attention. RFC ### Motivation. vllm defaults to using float16 inference for float32 models. https://github.com/vllm-project/vllm/blob/275c...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: torch_dtype = torch.float16 ``` Most models can maintain their original precision, but a few models require float32. But flash attn does not support float32, making it a very ineffective choice. More reports of embeddin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: #18940 #### Generative models I carefully constructed [a test with a small model](https://github.com/noooop/vllm/blob/hybrid/tests/models/test_hybrid_dtype.py), which only passed with float32 and hybrid dtype, but faile...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: FC ### Motivation. vllm defaults to using float16 inference for float32 models. https://github.com/vllm-project/vllm/blob/275c5daeb0048c3b3f359bb5d9478b1e75e02857/vllm/config.py#L3053C1-L3055C44 ``` # Set default dtype...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rch_dtype = torch.float16 ``` Most models can maintain their original precision, but a few models require float32. But flash attn does not support float32, making it a very ineffective choice. More reports of embedding...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
