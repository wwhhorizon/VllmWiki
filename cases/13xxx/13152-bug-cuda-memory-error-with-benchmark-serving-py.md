# vllm-project/vllm#13152: [Bug]: CUDA memory error with benchmark_serving.py

| 字段 | 值 |
| --- | --- |
| Issue | [#13152](https://github.com/vllm-project/vllm/issues/13152) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;oom |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CUDA memory error with benchmark_serving.py

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried to run the `benchmark_serving.py` script, but it crashed with a "CUDA out of memory" error. The full error message is below, but part of it is > vllm.engine.async_llm_engine.AsyncEngineDeadError: Task finished unexpectedly. This should never happen! Please open an issue on Github. See stack trace above for the actual cause. which is why I post it here. GPU is A100 80GB, which should be plenty. Steps to recreate: - Install vllm in a fresh python 3.11 venv environment (vllm version 0.7.2) - clone the vllm github repo for the benchmarking script, install `pandas` and `datasets` as additional requirements - run `vllm serve Qwen/Qwen2.5-72B-Instruct-AWQ --gpu-memory-utilization 0.99 --disable-frontend-multiprocessing --max_model_len 25000 --max-num-seqs 64 --port 8080` to start model serving (error also comes with only the --gpu_mem and --port args) - `python3 benchmark_serving.py --backend openai --base-url http://0.0.0.0:8080 --dataset-name=random --model Qwen/Qwen2.5-72B-Instruct-AWQ --request-rate 4` - wait for crash (came around 31%) ### Before submitting a new issue... - [x] Make sure you already searched for relevant is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: it here. GPU is A100 80GB, which should be plenty. Steps to recreate: - Install vllm in a fresh python 3.11 venv environment (vllm version 0.7.2) - clone the vllm github repo for the benchmarking script, install `pandas...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: CUDA memory error with benchmark_serving.py bug;stale ### Your current environment ### 🐛 Describe the bug I tried to run the `benchmark_serving.py` script, but it crashed with a "CUDA out of memory" error. The fu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: CUDA memory error with benchmark_serving.py bug;stale ### Your current environment ### 🐛 Describe the bug I tried to run the `benchmark_serving.py` script, but it crashed with a "CUDA out of memory" error. The fu...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: th only the --gpu_mem and --port args) - `python3 benchmark_serving.py --backend openai --base-url http://0.0.0.0:8080 --dataset-name=random --model Qwen/Qwen2.5-72B-Instruct-AWQ --request-rate 4` - wait for crash (came...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: all `pandas` and `datasets` as additional requirements - run `vllm serve Qwen/Qwen2.5-72B-Instruct-AWQ --gpu-memory-utilization 0.99 --disable-frontend-multiprocessing --max_model_len 25000 --max-num-seqs 64 --port 8080...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
