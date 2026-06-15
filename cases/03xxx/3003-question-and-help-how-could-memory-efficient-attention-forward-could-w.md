# vllm-project/vllm#3003: question and help❓ how could  memory_efficient_attention_forward could work on the concatenating batches?

| 字段 | 值 |
| --- | --- |
| Issue | [#3003](https://github.com/vllm-project/vllm/issues/3003) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 |  |
| 子分类 | precision |
| Operator 关键词 | cuda;operator |
| 症状 |  |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> question and help❓ how could  memory_efficient_attention_forward could work on the concatenating batches?

### Issue 正文摘录

[memory_efficient_attention_forward](https://facebookresearch.github.io/xformers/components/ops.html#xformers.ops.memory_efficient_attention) is invoked in prefill phase. This function expects the input tensor to have a shape of [batch_size, num_seq, num_head, head_size]. However, previously, the queries and other tensors were transformed using torch.view, torch. unsqueeze, resulting in a shape of [1, batch_size * num_seq, num_head, head_size]. Doesn't this difference in tensor format from what memory_efficient_attention_forward pose a problem? How do we ensure that the final result is correct? in my own test. concating batches does not have the same result..., please enlighten me. ```python import torch from xformers import ops as xops device="cuda" dtype=torch.float16 #[B,M,H,K] query = torch.rand((3, 136, 32, 64), dtype=dtype, device=device) key = torch.rand((3, 136, 32, 64), dtype=dtype, device=device) value = torch.rand((3, 136, 32, 64),dtype=dtype, device=device) resized_query = query.view(-1, 32, 64).unsqueeze(0) resized_key = query.view(-1, 32, 64).unsqueeze(0) resized_value = query.view(-1, 32, 64).unsqueeze(0) scale=1.0/(query.size(-1)**0.5) print(scale) out1 = xops.memo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: question and help❓ how could memory_efficient_attention_forward could work on the concatenating batches? [memory_efficient_attention_forward](https://facebookresearch.github.io/xformers/components/ops.html#xformers.ops....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ```python import torch from xformers import ops as xops device="cuda" dtype=torch.float16 #[B,M,H,K] query = torch.rand((3, 136, 32, 64), dtype=dtype, device=device) key = torch.rand((3, 136, 32, 64), dtype=dtype, devic...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: ,64) print(out1.shape,out2.shape) # the TWO results are not same. assert torch.allclose(out1, out2, atol=1e-2, rtol=1e-2) ``` correctness cuda;operator dtype;env_dependency;shape [memory_efficient_attention_forward](htt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nating batches? [memory_efficient_attention_forward](https://facebookresearch.github.io/xformers/components/ops.html#xformers.ops.memory_efficient_attention) is invoked in prefill phase. This function expects the input...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ize * num_seq, num_head, head_size]. Doesn't this difference in tensor format from what memory_efficient_attention_forward pose a problem? How do we ensure that the final result is correct? in my own test. concating bat...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
