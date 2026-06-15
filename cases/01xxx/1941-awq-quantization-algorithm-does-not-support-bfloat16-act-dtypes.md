# vllm-project/vllm#1941: AWQ quantization algorithm does not support bfloat16 act dtypes

| 字段 | 值 |
| --- | --- |
| Issue | [#1941](https://github.com/vllm-project/vllm/issues/1941) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AWQ quantization algorithm does not support bfloat16 act dtypes

### Issue 正文摘录

https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/awq.py#L42 ` File "/work/vllm-github/vllm/engine/ray_utils.py", line 31, in execute_method return executor(*args, **kwargs) File "/work/vllm-github/vllm/worker/worker.py", line 72, in load_model self.model_runner.load_model() File "/work/vllm-github/vllm/worker/model_runner.py", line 33, in load_model self.model = get_model(self.model_config) File "/work/vllm-github/vllm/model_executor/model_loader.py", line 84, in get_model raise ValueError( ValueError: torch.bfloat16 is not supported for quantization method awq. Supported dtypes: [torch.float16]` I trained a model in which the parameter type is bf16 (this model will have NaN problems when using fp16). When I used AutoAWQ to quantify this model, I found in vllm that the act type only support fp16. Will you support bf16 as the act dtype?

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: AWQ quantization algorithm does not support bfloat16 act dtypes https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/awq.py#L42 ` File "/work/vllm-github/vllm/engine/ray_utils.py", line...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: bfloat16 act dtypes https://github.com/vllm-project/vllm/blob/main/vllm/model_executor/layers/quantization/awq.py#L42 ` File "/work/vllm-github/vllm/engine/ray_utils.py", line 31, in execute_method return executor(*args...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
