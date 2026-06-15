# vllm-project/vllm#30546: [Bug]: Incorrect dimension movement in reduce_scatter (first movedim(0, dim) should be movedim(dim, 0))

| 字段 | 值 |
| --- | --- |
| Issue | [#30546](https://github.com/vllm-project/vllm/issues/30546) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Incorrect dimension movement in reduce_scatter (first movedim(0, dim) should be movedim(dim, 0))

### Issue 正文摘录

### Your current environment latest vllm version ### 🐛 Describe the bug In vllm/distributed/device_communicators/base_device_communicator/base_device_communicator.py:reduce_scatter ```python def reduce_scatter(self, input_: torch.Tensor, dim: int = -1) -> torch.Tensor: world_size = self.world_size # Bypass the function if we are using only 1 GPU. if world_size == 1: return input_ assert -input_.dim() <= dim < input_.dim(), ( f"Invalid dim ({dim}) for input tensor with shape {input_.size()}" ) if dim < 0: # Convert negative dim to positive. dim += input_.dim() # Note: This will produce an incorrect answer if we don't make # the input_tensor contiguous. Possible bug in reduce_scatter_tensor? input_tensor = input_.movedim(0, dim).contiguous() # [my question]: should be movedim(dim, 0)? assert input_tensor.shape[0] % world_size == 0 chunk_size = input_tensor.shape[0] // world_size output_shape = (chunk_size,) + input_tensor.shape[1:] output_tensor = torch.empty( output_shape, dtype=input_tensor.dtype, device=input_tensor.device ) # Perform reduce-scatter operation torch.distributed.reduce_scatter_tensor( output_tensor, input_tensor, group=self.device_group ) # Reshape before returning...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ppears in vllm/distributed/device_communicators/base_device_communicator/cuda_communicator.py:reduce_scatter, reduce_scatterv ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: be movedim(dim, 0)) bug;stale ### Your current environment latest vllm version ### 🐛 Describe the bug In vllm/distributed/device_communicators/base_device_communicator/base_device_communicator.py:reduce_scatter ```pytho...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: tensor.shape[1:] output_tensor = torch.empty( output_shape, dtype=input_tensor.dtype, device=input_tensor.device ) # Perform reduce-scatter operation torch.distributed.reduce_scatter_tensor( output_tensor, input_tensor,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: will produce an incorrect answer if we don't make # the input_tensor contiguous. Possible bug in reduce_scatter_tensor? input_tensor = input_.movedim(0, dim).contiguous() # [my question]: should be movedim(dim, 0)? asse...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: in reduce_scatter (first movedim(0, dim) should be movedim(dim, 0)) bug;stale ### Your current environment latest vllm version ### 🐛 Describe the bug In vllm/distributed/device_communicators/base_device_communicator/bas...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
