# vllm-project/vllm#20993: [Bug]: Is image embedding supported in llama 4

| 字段 | 值 |
| --- | --- |
| Issue | [#20993](https://github.com/vllm-project/vllm/issues/20993) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Is image embedding supported in llama 4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to run inference of a [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) by directly passing the image embedding, following the instruction [here](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html#embedding-inputs). But I am observing the following error message which appears that the execution is trying to process the image embedding as if it is an image. After some code search I figured that passing image embedding is [not supported](https://github.com/vllm-project/vllm/blob/68d28e37b0d3706601b0d5231178cebaad032605/vllm/model_executor/models/mllama.py#L1395-L1396) whereas the Llava model in the example does have [type](https://github.com/vllm-project/vllm/blob/e7e3e6d2636f6cd012c7ffeff773b20b3c90b958/vllm/model_executor/models/llava.py#L71-L81) for embedding input. I wonder if passing image embedding to llama 4 is not supported in vLLM. And if not, how can I properly pass it to vLLM? ``` Traceback (most recent call last): File "/opt/vllm/vllm/vllm/inputs/registry.py", line 169, in call_hf_processor output = hf_processor(**data, **merged_kwargs, return_tensors="pt") ^...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Is image embedding supported in llama 4 bug;stale ### Your current environment ### 🐛 Describe the bug I want to run inference of a [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-In...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Is image embedding supported in llama 4 bug;stale ### Your current environment ### 🐛 Describe the bug I want to run inference of a [Llama-4-Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-In...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ck](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8) by directly passing the image embedding, following the instruction [here](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html#embe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: to process the image embedding as if it is an image. After some code search I figured that passing image embedding is [not supported](https://github.com/vllm-project/vllm/blob/68d28e37b0d3706601b0d5231178cebaad032605/vl...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ge embedding, following the instruction [here](https://docs.vllm.ai/en/latest/features/multimodal_inputs.html#embedding-inputs). But I am observing the following error message which appears that the execution is trying...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
