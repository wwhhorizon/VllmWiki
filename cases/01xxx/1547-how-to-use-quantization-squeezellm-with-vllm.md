# vllm-project/vllm#1547: how to use quantization squeezellm with vllm

| 字段 | 值 |
| --- | --- |
| Issue | [#1547](https://github.com/vllm-project/vllm/issues/1547) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> how to use quantization squeezellm with vllm

### Issue 正文摘录

already use https://github.com/SqueezeAILab/SqueezeLLM/tree/main/quantization to quantize my sft model, and get a packed model. try to run squeezellm quantized model in vllm 0.2.1 with script benchmarks/benchmark_latency.py shell is CUDA_VISIBLE_DEVICES=0 python benchmark_latency.py --model [fold contain packd pt] --tokenizer [model path] --quantization squeezellm --batch-size 128 and get error log File "/vllm/vllm/model_executor/weight_utils.py", line 107, in get_quant_config raise ValueError(f"Cannot find the config file for {quantization}") ValueError: Cannot find the config file for squeezellm after run with pdb vllm didn't find, while during quantization, squeezellm tutorial [https://github.com/SqueezeAILab/SqueezeLLM/tree/main/quantization] didn't output a quant_config.json. my issue is how to get that quant_config.json file. thx!

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ub.com/SqueezeAILab/SqueezeLLM/tree/main/quantization to quantize my sft model, and get a packed model. try to run squeezellm quantized model in vllm 0.2.1 with script benchmarks/benchmark_latency.py shell is CUDA_VISIB...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: d model. try to run squeezellm quantized model in vllm 0.2.1 with script benchmarks/benchmark_latency.py shell is CUDA_VISIBLE_DEVICES=0 python benchmark_latency.py --model [fold contain packd pt] --tokenizer [model pat...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: how to use quantization squeezellm with vllm already use https://github.com/SqueezeAILab/SqueezeLLM/tree/main/quantization to quantize my sft model, and get a packed model. try to run squeezellm quantized model in vllm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: odel in vllm 0.2.1 with script benchmarks/benchmark_latency.py shell is CUDA_VISIBLE_DEVICES=0 python benchmark_latency.py --model [fold contain packd pt] --tokenizer [model path] --quantization squeezellm --batch-size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
