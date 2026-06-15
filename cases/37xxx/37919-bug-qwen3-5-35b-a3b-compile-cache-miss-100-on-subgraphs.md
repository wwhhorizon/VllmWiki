# vllm-project/vllm#37919: [Bug]: Qwen3.5-35B-A3B compile cache miss 100% on subgraphs.

| 字段 | 值 |
| --- | --- |
| Issue | [#37919](https://github.com/vllm-project/vllm/issues/37919) |
| 状态 | open |
| 标签 | bug;torch.compile |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 |  |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3.5-35B-A3B compile cache miss 100% on subgraphs.

### Issue 正文摘录

### Your current environment vllm trunk + torch trunk ### 🐛 Describe the bug repro ``` vllm serve Qwen/Qwen3.5-35B-A3B ``` On vllm trunk I saw the cold compilation time of Qwen3.5-35B-A3B went from 25sec to 60sec. So I took a deeper look and found that we are just recompiling all subgraphs instead of only compiling 3 distinct subgraph like usual case. Graph 1 will look like: ``` mul_6 = mul_5 * add_7; mul_5 = add_7 = None to_2 = mul_6.to(torch.bfloat16); mul_6 = None empty_like = torch.empty_like(to_2) gdn_in_proj = torch.ops.vllm.gdn_in_proj(to_2, 12288, 64, 'language_model.model.layers.10.linear_attn'); to_2 = None getitem_4 = gdn_in_proj[0] getitem_5 = gdn_in_proj[1]; gdn_in_proj = None split = getitem_4.split([8192, 4096], dim = -1); getitem_4 = None getitem_6 = split[0] getitem_7 = split[1]; split = None reshape_3 = getitem_7.reshape(s18, -1, 128); getitem_7 = None sym_size_int_21 = torch.ops.aten.sym_size.int(reshape_3, 0) chunk = getitem_5.chunk(2, dim = -1); getitem_5 = None getitem_8 = chunk[0] getitem_9 = chunk[1]; chunk = None contiguous = getitem_8.contiguous(); getitem_8 = None contiguous_1 = getitem_9.contiguous(); getitem_9 = None zeros = torch.zeros((s18, 32, 128),...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Qwen3.5-35B-A3B compile cache miss 100% on subgraphs. bug;torch.compile ### Your current environment vllm trunk + torch trunk ### 🐛 Describe the bug repro ``` vllm serve Qwen/Qwen3.5-35B-A3B ``` On vllm trunk I s...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: mul_6 = mul_5 * add_7; mul_5 = add_7 = None to_2 = mul_6.to(torch.bfloat16); mul_6 = None empty_like = torch.empty_like(to_2) gdn_in_proj = torch.ops.vllm.gdn_in_proj(to_2, 12288, 64, 'language_model.model.layers.10.lin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: orch.zeros((s18, 32, 128), dtype = torch.bfloat16, device = device(type='cuda', index=0)); s18 = None return (getitem_6, contiguous, contiguous_1, zeros, reshape_3, sym_size_int_21, empty_like, add_5) ``` And Graph 2: `...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: one getitem_8 = chunk[0] getitem_9 = chunk[1]; chunk = None contiguous = getitem_8.contiguous(); getitem_8 = None contiguous_1 = getitem_9.contiguous(); getitem_9 = None zeros = torch.zeros((s18, 32, 128), dtype = torch...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3.5-35B-A3B compile cache miss 100% on subgraphs. bug;torch.compile ### Your current environment vllm trunk + torch trunk ### 🐛 Describe the bug repro ``` vllm serve Qwen/Qwen3.5-35B-A3B ``` On vllm trunk I s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
