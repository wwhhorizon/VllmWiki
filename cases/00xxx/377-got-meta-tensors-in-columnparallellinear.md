# vllm-project/vllm#377: got meta tensors in ColumnParallelLinear

| 字段 | 值 |
| --- | --- |
| Issue | [#377](https://github.com/vllm-project/vllm/issues/377) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> got meta tensors in ColumnParallelLinear

### Issue 正文摘录

Hi, I am tring to use the latest vllm, when creating the model, the weight in `ColumnParallelLinear` are all meta tensors, I debuged and print out the weight: ``` vllm/vllm/model_executor/parallel_utils/tensor_parallel/layers.py(276)__init__() -> self.weight = Parameter(torch.ones(self.output_size_per_partition, self.input_size,device=torch.cuda.current_device(), dtype=params_dtype)) p self.weight (Pdb) Parameter containing: tensor(..., device='meta', size=(15360, 5120), requires_grad=True) p torch.cuda.current_device() (Pdb) 0 p params_dtype (Pdb) torch.float16 ``` and finally when calling `model.cuda()` I got: `NotImplementedError: Cannot copy out of meta tensor; no data!` It is very strange, should the paramaters be metatensors?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _size_per_partition, self.input_size,device=torch.cuda.current_device(), dtype=params_dtype)) p self.weight (Pdb) Parameter containing: tensor(..., device='meta', size=(15360, 5120), requires_grad=True) p torch.cuda.cur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: (torch.ones(self.output_size_per_partition, self.input_size,device=torch.cuda.current_device(), dtype=params_dtype)) p self.weight (Pdb) Parameter containing: tensor(..., device='meta', size=(15360, 5120), requires_grad...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: nParallelLinear Hi, I am tring to use the latest vllm, when creating the model, the weight in `ColumnParallelLinear` are all meta tensors, I debuged and print out the weight: ``` vllm/vllm/model_executor/parallel_utils/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: got meta tensors in ColumnParallelLinear Hi, I am tring to use the latest vllm, when creating the model, the weight in `ColumnParallelLinear` are all meta tensors, I debuged and print out the weight: ``` vllm/vllm/model...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
