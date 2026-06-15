# vllm-project/vllm#27404: [Bug]: Qwen3-Next FP8 error combining --tensor-parallel-size and --pipeline-parallel-size using MTP

| 字段 | 值 |
| --- | --- |
| Issue | [#27404](https://github.com/vllm-project/vllm/issues/27404) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | cold_start |
| Operator 关键词 | cuda;fp8;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-Next FP8 error combining --tensor-parallel-size and --pipeline-parallel-size using MTP

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm running Qwen3-Next-80B-A3B-Instruct-FP8 in 8xL4 gpus in a vllm docker image. When running it with the following command works as expected: ``` docker run \ --gpus all \ --network host \ --rm \ vllm/vllm-openai:nightly-243ed7d32e94f00a9a32fbbc51be932f6277a55d \ --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --port 8000 \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.9 \ --max-model-len 262144 \ --max-num-seqs 5 ``` However, if I add MTP with the following command I get errors: ``` docker run \ --gpus all \ --network host \ --rm \ vllm/vllm-openai:nightly-243ed7d32e94f00a9a32fbbc51be932f6277a55d \ --model Qwen/Qwen3-Next-80B-A3B-Instruct-FP8 \ --port 8000 \ --tensor-parallel-size 4 \ --pipeline-parallel-size 2 \ --gpu-memory-utilization 0.9 \ --max-model-len 262144 \ --max-num-seqs 5 \ --no-enable-prefix-caching \ --speculative-config '{"method":"mtp","num_speculative_tokens":2}' ``` The errors obtained are: ``` (Worker_PP0_TP2 pid=543) ERROR 10-23 01:29:39 [multiproc_executor.py:699] WorkerProc hit an exception. (Worker_PP0_TP2 pid=543) ERROR 10-23 01:29:39 [multiproc_executor.py:699] Trace...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: bug I'm running Qwen3-Next-80B-A3B-Instruct-FP8 in 8xL4 gpus in a vllm docker image. When running it with the following command works as expected: ``` docker run \ --gpus all \ --network host \ --rm \ vllm/vllm-openai:n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: Qwen3-Next FP8 error combining --tensor-parallel-size and --pipeline-parallel-size using MTP bug;stale ### Your current environment ### 🐛 Describe the bug I'm running Qwen3-Next-80B-A3B-Instruct-FP8 in 8xL4 gpus...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3-Next FP8 error combining --tensor-parallel-size and --pipeline-parallel-size using MTP bug;stale ### Your current environment ### 🐛 Describe the bug I'm running Qwen3-Next-80B-A3B-Instruct-FP8 in 8xL4 gpus...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: bining --tensor-parallel-size and --pipeline-parallel-size using MTP bug;stale ### Your current environment ### 🐛 Describe the bug I'm running Qwen3-Next-80B-A3B-Instruct-FP8 in 8xL4 gpus in a vllm docker image. When ru...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: lm/entrypoints/cli/main.py", line 73, in main (APIServer pid=1) args.dispatch_function(args) (APIServer pid=1) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/cli/serve.py", line 59, in cmd (APIServer pid...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
