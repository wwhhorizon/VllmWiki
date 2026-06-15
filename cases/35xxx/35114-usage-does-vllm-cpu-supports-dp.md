# vllm-project/vllm#35114: [Usage]: Does vllm cpu supports DP

| 字段 | 值 |
| --- | --- |
| Issue | [#35114](https://github.com/vllm-project/vllm/issues/35114) |
| 状态 | open |
| 标签 | usage;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Does vllm cpu supports DP

### Issue 正文摘录

### Your current environment I was looking to achieve Parallelism with better throughput on CPU, I am running vllm like this: export MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct export VLLM_USE_V1=1 VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 VLLM_ENGINE_ITERATION_TIMEOUT_S=6000 VLLM_CPU_KVCACHE_SPACE=80 OMP_NUM_THREADS=32 VLLM_CPU_OMP_THREADS_BIND="0-31|32-63|64-95|96-127" python3 -m vllm.entrypoints.openai.api_server --model $MODEL --dtype=bfloat16 -O3 --port 8000 --host 0.0.0.0 -tp=4 --distributed-executor-backend mp --enable_chunked_prefill --max_num_seqs 4096 --max-model-len 128000 --max-num-batched-tokens 65536 --no-enable-prefix-caching ### How would you like to use vllm _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 96-127" python3 -m vllm.entrypoints.openai.api_server --model $MODEL --dtype=bfloat16 -O3 --port 8000 --host 0.0.0.0 -tp=4 --distributed-executor-backend mp --enable_chunked_prefill --max_num_seqs 4096 --max-model-len 1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge;stale ### Your current environment I was looking to achieve Parallelism with better throughput on CPU, I am running vllm like this: export MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct export VLLM_USE_V1=1 VLLM_ALLOW_L...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: lism with better throughput on CPU, I am running vllm like this: export MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct export VLLM_USE_V1=1 VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 VLLM_ENGINE_ITERATION_TIMEOUT_S=6000 VLLM_CPU_KVCA...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Usage]: Does vllm cpu supports DP usage;stale ### Your current environment I was looking to achieve Parallelism with better throughput on CPU, I am running vllm like this: export MODEL=meta-llama/Meta-Llama-3.1-8B-Inst...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ur current environment I was looking to achieve Parallelism with better throughput on CPU, I am running vllm like this: export MODEL=meta-llama/Meta-Llama-3.1-8B-Instruct export VLLM_USE_V1=1 VLLM_ALLOW_LONG_MAX_MODEL_L...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
