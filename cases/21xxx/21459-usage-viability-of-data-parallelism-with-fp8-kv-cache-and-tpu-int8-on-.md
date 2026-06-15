# vllm-project/vllm#21459: [Usage]: Viability of Data Parallelism with FP8 KV-Cache and tpu_int8 on TPU v4-64

| 字段 | 值 |
| --- | --- |
| Issue | [#21459](https://github.com/vllm-project/vllm/issues/21459) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Viability of Data Parallelism with FP8 KV-Cache and tpu_int8 on TPU v4-64

### Issue 正文摘录

### Your current environment miniconda3/envs/vllm/bin/pip install datasets transformers git clone https://github.com/vllm-project/vllm.git miniconda3/envs/vllm/bin/pip install -r vllm/requirements/tpu.txt rm -rf vllm VLLM_TARGET_DEVICE="tpu" miniconda3/envs/vllm/bin/pip install git+https://github.com/vllm-project/vllm.git ### How would you like to use vllm Hi vLLM team, I am writing to inquire about the support for a specific configuration for running inference with vLLM on a TPU v4-64. I would like to run inference for the Qwen/Qwen3-30B-A3B model and leverage several features simultaneously to optimize performance. My target hardware is a TPU v4-64. Specifically, I would like to confirm if the following combination of settings is supported and expected to work together: data-parallel-size > 1 (to utilize multiple TPU cores for data parallelism) kv-cache-dtype=fp8 quantization=tpu_int8 My goal is to achieve the highest possible throughput by combining data parallelism with these quantization and memory-saving techniques on the TPU. Could you please advise if this combination of features is currently supported on a TPU v4-64? Are there any known limitations or potential issues I s...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: Viability of Data Parallelism with FP8 KV-Cache and tpu_int8 on TPU v4-64 usage ### Your current environment miniconda3/envs/vllm/bin/pip install datasets transformers git clone https://github.com/vllm-project/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Hi vLLM team, I am writing to inquire about the support for a specific configuration for running inference with vLLM on a TPU v4-64. I would like to run inference for the Qwen/Qwen3-30B-A3B model and leverage several fe...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: U v4-64 usage ### Your current environment miniconda3/envs/vllm/bin/pip install datasets transformers git clone https://github.com/vllm-project/vllm.git miniconda3/envs/vllm/bin/pip install -r vllm/requirements/tpu.txt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: Viability of Data Parallelism with FP8 KV-Cache and tpu_int8 on TPU v4-64 usage ### Your current environment miniconda3/envs/vllm/bin/pip install datasets transformers git clone https://github.com/vllm-project/...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ype=fp8 quantization=tpu_int8 My goal is to achieve the highest possible throughput by combining data parallelism with these quantization and memory-saving techniques on the TPU. Could you please advise if this combinat...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
