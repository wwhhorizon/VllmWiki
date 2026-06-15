# vllm-project/vllm#13412: [Usage]: TTFT Decreases with longer input length and output length when using max_concurrency in vLLM (benchmark_serving.py)

| 字段 | 值 |
| --- | --- |
| Issue | [#13412](https://github.com/vllm-project/vllm/issues/13412) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: TTFT Decreases with longer input length and output length when using max_concurrency in vLLM (benchmark_serving.py)

### Issue 正文摘录

### Your current environment LLM model used: "meta-llama/Llama-3.3-70B-Instruct" GPU used: Nvidia H200 (8 GPUs) Parameters used to load model using vllm. ```python docker run -d --gpus all -v /raid/vllm_cache/huggingface:/root/.cache/huggingface -p 8002:8002 --ipc=host vllm/vllm-openai:latest --model meta-llama/Llama-3.3-70B-Instruct --tensor-parallel-size 8 --max-num-seqs 256 --num-scheduler-steps 10 --max-seq-len-to-capture 8192 --enable-chunked-prefill=False --port 8002 ``` benchmark_serving.py command: ```python python3 ./vllm/benchmarks/benchmark_serving.py --base-url "http://127.0.0.1:8002/" --model "meta-llama/Llama-3.3-70B-Instruct" --dataset-name "random" --random-output-len 1 --random-input-len 3100 --num-prompts 1024 --max-concurrency 32 --seed 12345 --save-result --result-filename "result.json" ``` ### How would you like to use vllm While benchmarking vLLM (benchmark_serving.py) with max_concurrency=32 , I observed that Time to First Token (TTFT) decreases significantly when output sequence length (OSL) increases , even when input sequence length (ISL) is high. Here are the results with num_prompts = 960 and max_concurrency = 32 request-rate=inf: ISL | OSL | Max Concur...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: t length when using max_concurrency in vLLM (benchmark_serving.py) usage;stale ### Your current environment LLM model used: "meta-llama/Llama-3.3-70B-Instruct" GPU used: Nvidia H200 (8 GPUs) Parameters used to load mode...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: onger input length and output length when using max_concurrency in vLLM (benchmark_serving.py) usage;stale ### Your current environment LLM model used: "meta-llama/Llama-3.3-70B-Instruct" GPU used: Nvidia H200 (8 GPUs)...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: LLM (benchmark_serving.py) usage;stale ### Your current environment LLM model used: "meta-llama/Llama-3.3-70B-Instruct" GPU used: Nvidia H200 (8 GPUs) Parameters used to load model using vllm. ```python docker run -d --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vidia H200 (8 GPUs) Parameters used to load model using vllm. ```python docker run -d --gpus all -v /raid/vllm_cache/huggingface:/root/.cache/huggingface -p 8002:8002 --ipc=host vllm/vllm-openai:latest --model meta-llam...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
