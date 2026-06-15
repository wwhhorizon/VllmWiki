# vllm-project/vllm#3399: Why AWQ and GPTQ model slower than ORI model in concurrency?

| 字段 | 值 |
| --- | --- |
| Issue | [#3399](https://github.com/vllm-project/vllm/issues/3399) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Why AWQ and GPTQ model slower than ORI model in concurrency?

### Issue 正文摘录

I've conducted a performance comparison using VLLM version 0.3.3 on an 8 A800 GPU machine, employing four GPUs for testing 10,000 address parsing data points with a concurrency of 500. The results are as follows: 1638s for GPTQ, 2025s for AWQ, and 1468s for the Original method. Surprisingly, both GPTQ and AWQ performed slower than the original setup. blow is my cmd and pic: GPT-1638s-CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --model /xxx/Qwen1.5-72B-Chat-GPTQ-Int4/ --tensor-parallel-size 4 --port 30142 --dtype half --max-model-len 2000 --gpu-memory-utilization 0.95 --enforce-eager --quantization gptq AWQ-2025s-CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --model /xxx/Qwen1.5-72B-Chat-AWQ/ --tensor-parallel-size 4 --port 30142 --dtype half --max-model-len 2000 --gpu-memory-utilization 0.95 --enforce-eager --quantization awq ORI-1468s-CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --model /xxx/Qwen_Qwen1.5-72B-Chat/ --tensor-parallel-size 4 --port 30142 --dtype half --max-model-len 2000 --gpu-memory-utilization 0.95 --enforce-eager ![vXba3UresO](https://github.com/vllm-project/vllm/assets/9215190...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: llm.entrypoints.openai.api_server --model /xxx/Qwen1.5-72B-Chat-GPTQ-Int4/ --tensor-parallel-size 4 --port 30142 --dtype half --max-model-len 2000 --gpu-memory-utilization 0.95 --enforce-eager --quantization gptq AWQ-20...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Why AWQ and GPTQ model slower than ORI model in concurrency? I've conducted a performance comparison using VLLM version 0.3.3 on an 8 A800 GPU machine, employing four GPUs for testing 10,000 address parsing data points...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: model in concurrency? I've conducted a performance comparison using VLLM version 0.3.3 on an 8 A800 GPU machine, employing four GPUs for testing 10,000 address parsing data points with a concurrency of 500. The results...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ormed slower than the original setup. blow is my cmd and pic: GPT-1638s-CUDA_VISIBLE_DEVICES=4,5,6,7 python -m vllm.entrypoints.openai.api_server --model /xxx/Qwen1.5-72B-Chat-GPTQ-Int4/ --tensor-parallel-size 4 --port...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ing VLLM version 0.3.3 on an 8 A800 GPU machine, employing four GPUs for testing 10,000 address parsing data points with a concurrency of 500. The results are as follows: 1638s for GPTQ, 2025s for AWQ, and 1468s for the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
