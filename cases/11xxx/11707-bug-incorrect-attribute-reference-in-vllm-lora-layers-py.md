# vllm-project/vllm#11707: [Bug]: Incorrect attribute reference in vllm/lora/layers.py

| 字段 | 值 |
| --- | --- |
| Issue | [#11707](https://github.com/vllm-project/vllm/issues/11707) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect attribute reference in vllm/lora/layers.py

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug self.output_dim should be changed to self.output_size ```python class ColumnParallelLinearWithLoRA(BaseLinearLayerWithLoRA): """ LoRA on top of ColumnParallelLinear layer. LoRA B is sliced for tensor parallelism. There are two types for the `base_layer`: 1. ColumnParallelLinear, e.g.`dense_h_to_4h` in `FalconForCausalLM`. 2. MergedColumnParallelLinear, e.g.`gate_up_proj` in `Phi3ForCausalLM`. """ def __init__(self, base_layer: ColumnParallelLinear) -> None: super().__init__(base_layer) # The base_layer type is ColumnParallelLinear or # MergedColumnParallelLinear, their weight sharding logic is # inconsistent when TP is greater than 1. self.is_merged_col_linear = type( base_layer) is MergedColumnParallelLinear self.tp_size = get_tensor_model_parallel_world_size() self.output_size = self.base_layer.output_size_per_partition # There is only one LoRA layer self.n_slices = 1 def slice_lora_b(self, lora_b: torch.Tensor) -> torch.Tensor: # Applicable to cases where the base_layer is # MergedColumnParallelLinear. if self.is_merged_col_linear: tp_rank = get_tensor_model_parallel_rank() shard_size = self...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: of ColumnParallelLinear layer. LoRA B is sliced for tensor parallelism. There are two types for the `base_layer`: 1. ColumnParallelLinear, e.g.`dense_h_to_4h` in `FalconForCausalLM`. 2. MergedColumnParallelLinear, e.g.`...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: as(self, bias: torch.Tensor) -> torch.Tensor: # TODO: Fix the slicing logic of bias. if bias is None: return bias tensor_model_parallel_rank = get_tensor_model_parallel_rank() shard_size = self.output_dim # self.output_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: o cases where the base_layer is # ColumnParallelLinear. else: tensor_model_parallel_rank = get_tensor_model_parallel_rank() shard_size = self.output_dim # self.output_dim is not defined start_idx = tensor_model_parallel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: eference in vllm/lora/layers.py bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug self.output_dim should be changed to self.output_size ```python class ColumnParallelLinearWithL...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
