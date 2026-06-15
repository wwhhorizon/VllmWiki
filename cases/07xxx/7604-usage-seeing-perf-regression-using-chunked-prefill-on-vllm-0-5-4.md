# vllm-project/vllm#7604: [Usage]: Seeing perf regression using chunked_prefill on VLLM 0.5.4

| 字段 | 值 |
| --- | --- |
| Issue | [#7604](https://github.com/vllm-project/vllm/issues/7604) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Seeing perf regression using chunked_prefill on VLLM 0.5.4

### Issue 正文摘录

### Your current environment ```text Docker container following build_from _source instruction ``` ### How would you like to use vllm I want to experiment how chunked_prefill can increase throughput but see perf regression when enabling chunked_prefill. I am testing on [Llama-3-70B-Instruct-Gradient-1048k ](https://huggingface.co/gradientai/Llama-3-70B-Instruct-Gradient-1048k) on 8 H100 SXM GPUs. I am benchmarking using `/benchmark/benchmark_throughput.py` and Tensor Parallel size 8 Is there any guidance how to choose `max_batched_tokens` properly? My command is : ``` Python python3 ./benchmarks/benchmark_throughput.py \ --model hf_model_path \ --tokenizer hf_model_path \ --tensor-parallel-size 8 \ --num-prompts 50 \ --input-len 40000 \ --output-len 256 \ --enable-chunked-prefill \ --max_batched_tokens 4096 --trust-remote-code ``` My benchmark result is: ![image](https://github.com/user-attachments/assets/9a15b0e2-a0d9-4243-9f2e-40c64f9c19c1)

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: but see perf regression when enabling chunked_prefill. I am testing on [Llama-3-70B-Instruct-Gradient-1048k ](https://huggingface.co/gradientai/Llama-3-70B-Instruct-Gradient-1048k) on 8 H100 SXM GPUs. I am benchmarking...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Usage]: Seeing perf regression using chunked_prefill on VLLM 0.5.4 usage;stale ### Your current environment ```text Docker container following build_from _source instruction ``` ### How would you like to use vllm I wan...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: _prefill on VLLM 0.5.4 usage;stale ### Your current environment ```text Docker container following build_from _source instruction ``` ### How would you like to use vllm I want to experiment how chunked_prefill can incre...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Seeing perf regression using chunked_prefill on VLLM 0.5.4 usage;stale ### Your current environment ```text Docker container following build_from _source instruction ``` ### How would you like to use vllm I wan...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ps://huggingface.co/gradientai/Llama-3-70B-Instruct-Gradient-1048k) on 8 H100 SXM GPUs. I am benchmarking using `/benchmark/benchmark_throughput.py` and Tensor Parallel size 8 Is there any guidance how to choose `max_ba...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
