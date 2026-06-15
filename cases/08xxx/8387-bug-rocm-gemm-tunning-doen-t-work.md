# vllm-project/vllm#8387: [Bug]: Rocm gemm tunning doen't work.

| 字段 | 值 |
| --- | --- |
| Issue | [#8387](https://github.com/vllm-project/vllm/issues/8387) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;import_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Rocm gemm tunning doen't work.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I try to do the Gemm tunning doing this: export VLLM_UNTUNE_FILE="/tmp/mistral7b.csv" export VLLM_TUNE_FILE="/work/mistral7b.csv" export HIP_FORCE_DEV_KERNARG=1 export DEBUG_CLR_GRAPH_PACKET_CAPTURE=1 VLLM_TUNE_GEMM=1 torchrun --standalone --nnodes=1 --nproc-per-node=1 ./vllm/benchmarks/benchmark_latency.py --batch-size 1 --input-len 2048 --output-len 128 --model ./Mistral-7B-v0.3 -tp 1 python ./vllm/gradlib/gradlib/gemm_tuner.py --input /tmp/mistral7b.csv --tuned_file ./mistral7b.csv But when I try the models after using this: python -m vllm.entrypoints.openai.api_server --model Mistral-7B-v0.3 --tensor-parallel-size 1 --port 8010 --host 0.0.0.0 --distributed-executor-backend mp --gpu-memory-utilization 0.94 --enable-prefix-caching I only get strange symbols or nothing. I also tried instead of benchmark_latency.py to use directly the python -m vllm.entrypoints.openai.api_server for tune but same result. I'm using the vllm-rocm master of Today. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://d...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;gemm;operator;sampling;triton b...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Rocm gemm tunning doen't work. bug ### Your current environment ### 🐛 Describe the bug I try to do the Gemm tunning doing this: export VLLM_UNTUNE_FILE="/tmp/mistral7b.csv" export VLLM_TUNE_FILE="/work/mistral7b....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: M_TUNE_GEMM=1 torchrun --standalone --nnodes=1 --nproc-per-node=1 ./vllm/benchmarks/benchmark_latency.py --batch-size 1 --input-len 2048 --output-len 128 --model ./Mistral-7B-v0.3 -tp 1 python ./vllm/gradlib/gradlib/gem...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: tensor-parallel-size 1 --port 8010 --host 0.0.0.0 --distributed-executor-backend mp --gpu-memory-utilization 0.94 --enable-prefix-caching I only get strange symbols or nothing. I also tried instead of benchmark_latency....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: /benchmark_latency.py --batch-size 1 --input-len 2048 --output-len 128 --model ./Mistral-7B-v0.3 -tp 1 python ./vllm/gradlib/gradlib/gemm_tuner.py --input /tmp/mistral7b.csv --tuned_file ./mistral7b.csv But when I try t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
