# vllm-project/vllm#18728: [Performance]: yarn degrades the performance of qwen3

| 字段 | 值 |
| --- | --- |
| Issue | [#18728](https://github.com/vllm-project/vllm/issues/18728) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: yarn degrades the performance of qwen3

### Issue 正文摘录

### Proposal to improve performance `vllm version == 0.8.5.post1` without yarn ```bash vllm serve Qwen/Qwen3-32B \ --trust-remote-code --gpu_memory_utilization 0.95 --tensor-parallel-size 2 \ --quantization bitsandbytes --load_format bitsandbytes --enforce_eager \ --max-model-len 32768 ``` with yarn ```bash vllm serve Qwen/Qwen3-32B \ --trust-remote-code --gpu_memory_utilization 0.95 --tensor-parallel-size 2 \ --quantization bitsandbytes --load_format bitsandbytes --enforce_eager \ --rope-scaling '{"rope_type":"yarn","factor":4.0,"original_max_position_embeddings":32768}' \ --max-model-len 131072 ``` I have some tests on my end for its agentic capabilities based on qwen3 and I have some solid findings that enabling yarn to extend window context does degrade the performace, with around 15-20% performance drop. do u also encounter the same findings ? any suggestion about this drop ? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues,...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: yarn degrades the performance of qwen3 performance ### Proposal to improve performance `vllm version == 0.8.5.post1` without yarn ```bash vllm serve Qwen/Qwen3-32B \ --trust-remote-code --gpu_memory_utili...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: x_position_embeddings":32768}' \ --max-model-len 131072 ``` I have some tests on my end for its agentic capabilities based on qwen3 and I have some solid findings that enabling yarn to extend window context does degrade...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: formance of qwen3 performance ### Proposal to improve performance `vllm version == 0.8.5.post1` without yarn ```bash vllm serve Qwen/Qwen3-32B \ --trust-remote-code --gpu_memory_utilization 0.95 --tensor-parallel-size 2...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: t-remote-code --gpu_memory_utilization 0.95 --tensor-parallel-size 2 \ --quantization bitsandbytes --load_format bitsandbytes --enforce_eager \ --max-model-len 32768 ``` with yarn ```bash vllm serve Qwen/Qwen3-32B \ --t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
