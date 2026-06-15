# vllm-project/vllm#10365: [Bug]: Torch profiling does not stop and cannot get traces for all workers

| 字段 | 值 |
| --- | --- |
| Issue | [#10365](https://github.com/vllm-project/vllm/issues/10365) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Torch profiling does not stop and cannot get traces for all workers

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was following https://docs.vllm.ai/en/v0.5.5/dev/profiling/profiling_index.html#profiling-vllm and profiling vLLM with the following commands: ``` VLLM_TORCH_PROFILER_DIR=/home/ubuntu/data/vllm_traces vllm serve meta-llama/Meta-Llama-3-8B --swap-space 16 --disable-log-requests --max-model-len 4096 -pp 2 python benchmarks/benchmark_serving.py --backend vllm --model meta-llama/Meta-Llama-3-8B --dataset-name sharegpt --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json --profile --num-prompts 2 ``` The API server could not stop the profiler: Only seeing: ``` INFO 11-15 15:26:33 api_server.py:406] Stopping profiler... ``` But not: ``` logger.info("Profiler stopped.") ``` And only one trace file was generated for a worker, but not the other worker. I tried with `--distributed-executor-backend ray` and it has the same issue. When there is a single worker (removing `-pp 2`) it works OK. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/),...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: [Bug]: Torch profiling does not stop and cannot get traces for all workers bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was following https://docs.vllm.ai/en/v0.5.5...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: Torch profiling does not stop and cannot get traces for all workers bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I was following https://docs.vllm.ai/en/v0.5.5/dev/pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s --max-model-len 4096 -pp 2 python benchmarks/benchmark_serving.py --backend vllm --model meta-llama/Meta-Llama-3-8B --dataset-name sharegpt --dataset-path ShareGPT_V3_unfiltered_cleaned_split.json --profile --num-prom...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: OK. ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
