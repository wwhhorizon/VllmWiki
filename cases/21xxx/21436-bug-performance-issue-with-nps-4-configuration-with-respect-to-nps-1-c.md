# vllm-project/vllm#21436: [Bug]: Performance issue with NPS-4 configuration with respect to NPS-1 configuration

| 字段 | 值 |
| --- | --- |
| Issue | [#21436](https://github.com/vllm-project/vllm/issues/21436) |
| 状态 | closed |
| 标签 | bug;unstale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Performance issue with NPS-4 configuration with respect to NPS-1 configuration

### Issue 正文摘录

### Your current environment In my evaluation, I executed vLLM workloads on two machines configured with different NUMA Partitioning Settings (NPS): one with NPS set to 4 (NPS-4) and another with NPS set to 1 (NPS-1) for comparison. The results indicate a significant performance degradation when running vLLM on the NPS-4 configuration relative to NPS-1. ### 🐛 Describe the bug I used below environments in both the cases VLLM_CPU_KVCACHE_SPACE=60 VLLM_CPU_OMP_THREADS_BIND=0- LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4:$LD_PRELOAD vllm version is 0.9.0 python benchmark_throughput.py --input-len 128 --output-len 1024 --model meta-llama/Llama-3.1-8B --num-prompts 500 --dtype bfloat16 --max-num-seqs 32 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: t to NPS-1 configuration bug;unstale ### Your current environment In my evaluation, I executed vLLM workloads on two machines configured with different NUMA Partitioning Settings (NPS): one with NPS set to 4 (NPS-4) and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 28 --output-len 1024 --model meta-llama/Llama-3.1-8B --num-prompts 500 --dtype bfloat16 --max-num-seqs 32 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chat...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Performance issue with NPS-4 configuration with respect to NPS-1 configuration bug;unstale ### Your current environment In my evaluation, I executed vLLM workloads on two machines configured with different NUMA P...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: OAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4:$LD_PRELOAD vllm version is 0.9.0 python benchmark_throughput.py --input-len 128 --output-len 1024 --model meta-llama/Llama-3.1-8B --num-prompts 500 --dtype bfloat1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 32 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
