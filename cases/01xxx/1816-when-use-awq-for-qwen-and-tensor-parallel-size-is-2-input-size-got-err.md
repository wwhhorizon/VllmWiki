# vllm-project/vllm#1816: when use awq for qwen and tensor_parallel_size is 2, input size got error.

| 字段 | 值 |
| --- | --- |
| Issue | [#1816](https://github.com/vllm-project/vllm/issues/1816) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> when use awq for qwen and tensor_parallel_size is 2, input size got error.

### Issue 正文摘录

File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, **kwargs) File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/worker/worker.py", line 70, in init_model self.model = get_model(self.model_config) File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/model_loader.py", line 90, in get_model model = model_class(model_config.hf_config, linear_method) File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen.py", line 243, in __init__ self.transformer = QWenModel(config, linear_method) File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen.py", line 199, in __init__ self.h = nn.ModuleList([ File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen.py", line 200, in QWenBlock(config, linear_method) File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen.py", line 151, in __init__ self.mlp = QWenMLP(config.hidden_size, File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: when use awq for qwen and tensor_parallel_size is 2, input size got error. File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/ray_utils.py", line 32, in execute_method return executor(*args, *...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: conda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/layers/quantization/awq.py", line 84, in create_weights raise ValueError( ValueError: The input size is not aligned with the quantized weight shape. This...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ite-packages/vllm/model_executor/models/qwen.py", line 200, in QWenBlock(config, linear_method) File "/usr/local/anaconda3/envs/vllm/lib/python3.10/site-packages/vllm/model_executor/models/qwen.py", line 151, in __init_...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
