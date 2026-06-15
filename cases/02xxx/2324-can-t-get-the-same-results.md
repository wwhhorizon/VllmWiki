# vllm-project/vllm#2324: Can't get the same results 

| 字段 | 值 |
| --- | --- |
| Issue | [#2324](https://github.com/vllm-project/vllm/issues/2324) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | debug |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Can't get the same results 

### Issue 正文摘录

I try to adapte CogVLM to VLLM, but I got different result when using the same input and the same network weight **VLLM** ```bash hiddens_states tensor([[[ 0.0019, -0.0034, 0.0021, ..., -0.0099, 0.0027, -0.0037], [-0.0073, -0.0082, -0.0618, ..., 0.0200, -0.0043, -0.0006], [-0.0889, 0.0262, 0.0144, ..., -0.1797, 0.0549, 0.1406], ..., [-0.0205, -0.0162, 0.0045, ..., 0.0172, 0.0013, 0.0128], [-0.0049, -0.0032, -0.0046, ..., 0.0201, 0.0166, 0.0149], [ 0.0040, 0.0019, 0.0052, ..., -0.0051, 0.0153, 0.0014]]], device='cuda:0', dtype=torch.bfloat16) input_layernorm Parameter containing: tensor([0.0266, 0.0114, 0.0044, ..., 0.0113, 0.0120, 0.0052], device='cuda:0', dtype=torch.bfloat16, requires_grad=True) hidden_states tensor([[[-0.0889, 0.0262, 0.0144, ..., -0.1797, 0.0549, 0.1406], [ 0.0332, 0.0322, 0.1157, ..., 0.1309, -0.0688, 0.0781], [-0.1050, 0.2734, -0.1230, ..., -0.0879, 0.0874, 0.0047], ..., [ 0.0000, 0.0000, 0.0000, ..., 0.0000, 0.0000, 0.0000], [ 0.0000, 0.0000, 0.0000, ..., 0.0000, 0.0000, 0.0000], [ 0.0000, 0.0000, 0.0000, ..., 0.0000, 0.0000, 0.0000]]], device='cuda:0', dtype=torch.bfloat16) tensor([[[ 0.0173, 0.0126, -0.0182, ..., -0.0106, 0.0649, 0.0432], [ 0.0728, 0.0918...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 19, 0.0052, ..., -0.0051, 0.0153, 0.0014]]], device='cuda:0', dtype=torch.bfloat16) input_layernorm Parameter containing: tensor([0.0266, 0.0114, 0.0044, ..., 0.0113, 0.0120, 0.0052], device='cuda:0', dtype=torch.bfloat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: dden_states) ``` So how can I fix the error？ development cuda dtype;env_dependency I try to adapte CogVLM to VLLM, but I got different result when using the same input and the same network weight
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 40, 0.0019, 0.0052, ..., -0.0051, 0.0153, 0.0014]]], device='cuda:0', dtype=torch.bfloat16) input_layernorm Parameter containing: tensor([0.0266, 0.0114, 0.0044, ..., 0.0113, 0.0120, 0.0052], device='cuda:0', dtype=torc...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: hidden_states = self.input_layernorm(hidden_states) else: hidden_states, residual = self.input_layernorm( hidden_states, residual) if token_type_ids is not None: print("input_layernorm") print(self.input_layernorm
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Can't get the same results stale I try to adapte CogVLM to VLLM, but I got different result when using the same input and the same network weight **VLLM** ```bash hiddens_states tensor([[[ 0.0019, -0.0034, 0.0021, ...,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
