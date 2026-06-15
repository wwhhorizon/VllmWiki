# vllm-project/vllm#21403: [Bug]: auto_tune.sh profiling attempts are hanging (i.e., "benchmarking_serving.py --profile" is failing)

| 字段 | 值 |
| --- | --- |
| Issue | [#21403](https://github.com/vllm-project/vllm/issues/21403) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: auto_tune.sh profiling attempts are hanging (i.e., "benchmarking_serving.py --profile" is failing)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm/benchmarks/auto_tune/auto_tune.sh was executed with VLLM_LOGGING_LEVEL=DEBUG with the following configuration: ```shell TAG=$(date +"%Y_%m_%d_%H_%M") BASE="/vllm-workspace" MODEL="google/gemma-3-27b-it" SYSTEM="GPU" TP=1 DOWNLOAD_DIR="/vllm-workspace/models" INPUT_LEN=1500 OUTPUT_LEN=200 MIN_CACHE_HIT_PCT=50 MAX_LATENCY_ALLOWED_MS=10000 NUM_SEQS_LIST="10" NUM_BATCHED_TOKENS_LIST="512 1024 2048 4096" ``` Initialization works fine and first inf benchmark works fine until "Stopping profiler..." i.e., line 399 in benchmark_serving.py - the hang occurs after this and before "Profiler stopped" so it must be hanging at like 408 ```python if profile: print("Stopping profiler...") profile_input = RequestFuncInput( model=model_id, prompt=test_prompt, api_url=base_url + "/stop_profile", prompt_len=test_prompt_len, output_len=test_output_len, logprobs=logprobs, ) profile_output = await request_func(request_func_input=profile_input) # LINE 408 HANG if profile_output.success: print("Profiler stopped") ``` I attempted to pass the same inputs to RequesFuncInput here as when the profiler is instantiated (noticed they are substantially differ...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: auto_tune.sh profiling attempts are hanging (i.e., "benchmarking_serving.py --profile" is failing) bug;stale ### Your current environment ### 🐛 Describe the bug vllm/benchmarks/auto_tune/auto_tune.sh was executed...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: s are hanging (i.e., "benchmarking_serving.py --profile" is failing) bug;stale ### Your current environment ### 🐛 Describe the bug vllm/benchmarks/auto_tune/auto_tune.sh was executed with VLLM_LOGGING_LEVEL=DEBUG with t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: print("Stopping profiler...") profile_input = RequestFuncInput( model=model_id, prompt=test_prompt, api_url=base_url + "/stop_profile", prompt_len=test_prompt_len, output_len=test_output_len, logprobs=log
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to_tune.sh was executed with VLLM_LOGGING_LEVEL=DEBUG with the following configuration: ```shell TAG=$(date +"%Y_%m_%d_%H_%M") BASE="/vllm-workspace" MODEL="google/gemma-3-27b-it" SYSTEM="GPU" TP=1 DOWNLOAD_DIR="/vllm-w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
