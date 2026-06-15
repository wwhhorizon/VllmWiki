# vllm-project/vllm#1118: Stuck when running benchmarks/benchmark_throughput.py

| 字段 | 值 |
| --- | --- |
| Issue | [#1118](https://github.com/vllm-project/vllm/issues/1118) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Stuck when running benchmarks/benchmark_throughput.py

### Issue 正文摘录

I was trying vllm with [benchmarks/benchmark_throughput.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_throughput.py). It got stuck, while everything works well with hf backend. So, what seems to be the problem? environment: ``` nvcr.io/nvidia/pytorch:22.12-py3 GPU: T4 ``` vllm version: ``` vllm-0.1.7 ``` cmd: ``` python benchmark_throughput.py \ --backend vllm \ --dataset /workspace/tests/llama/ShareGPT_V3_unfiltered_cleaned_split.json \ --model /workspace/tests/llama/open_llama_7b_v2 \ --num-prompts 1 ``` log: ``` Namespace(backend='vllm', dataset='/workspace/tests/llama/ShareGPT_V3_unfiltered_cleaned_split.json', hf_max_batch_size=None, model='/workspace/tests/llama/open_llama_7b_v2', n=1, num_prompts=1, seed=0, tensor_parallel_size=1, tokenizer='/workspace/tests/llama/open_llama_7b_v2', trust_remote_code=False, use_beam_search=False) INFO 09-21 03:44:48 tokenizer.py:30] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate the initialization time, consider using 'hf-internal-testing/llama-tokenizer' instead of the original tokenizer. You are using the default legacy behaviour of the . If you see this, DO NOT PA...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: benchmark_throughput.py). It got stuck, while everything works well with hf backend. So, what seems to be the problem? environment: ``` nvcr.io/nvidia/pytorch:22.12-py3 GPU: T4 ``` vllm version: ``` vllm-0.1.7 ``` cmd:...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Stuck when running benchmarks/benchmark_throughput.py bug I was trying vllm with [benchmarks/benchmark_throughput.py](https://github.com/vllm-project/vllm/blob/main/benchmarks/benchmark_throughput.py). It got stuck, whi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: lem? environment: ``` nvcr.io/nvidia/pytorch:22.12-py3 GPU: T4 ``` vllm version: ``` vllm-0.1.7 ``` cmd: ``` python benchmark_throughput.py \ --backend vllm \ --dataset /workspace/tests/llama/ShareGPT_V3_unfiltered_clea...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: s/llama/open_llama_7b_v2', tokenizer_mode=auto, trust_remote_code=False, dtype=torch.float16, download_dir=None, load_format=auto, tensor_parallel_size=1, seed=0) INFO 09-21 03:45:22 tokenizer.py:30] For some LLaMA-base...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: space/tests/llama/open_llama_7b_v2', trust_remote_code=False, use_beam_search=False) INFO 09-21 03:44:48 tokenizer.py:30] For some LLaMA-based models, initializing the fast tokenizer may take a long time. To eliminate t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
