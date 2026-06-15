# vllm-project/vllm#10533: [Bug]: vllm failed to run two instance with one gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#10533](https://github.com/vllm-project/vllm/issues/10533) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm failed to run two instance with one gpu

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to run Qwen2.5-14B-Instruct-GPTQ-Int4 and Qwen2.5-72B-Instruct-GPTQ-Int4 with one 80G A100. with following command ``` python3 -m vllm.entrypoints.openai.api_server \ --model /models/Qwen2.5-72B-Instruct-GPTQ-Int4 \ --gpu-memory-utilization 0.75 \ --max-model-len=16384 \ --served-model-name qwen2.5-14b \ --quantization=gptq \ --enforce-eager \ --enable-chunked-prefill \ --enable-prefix-caching python3 -m vllm.entrypoints.openai.api_server \ --model /models/Qwen2.5-14B-Instruct-GPTQ-Int4 \ --gpu-memory-utilization 0.20 \ --max-model-len=16384 \ --served-model-name qwen2.5-14b \ --quantization=gptq \ --enforce-eager \ --enable-chunked-prefill \ --enable-prefix-caching ``` Both commands succeed when running separately, consuming approximately 75% and 20% of the vRAM respectively. However when you start the 72B first and then 14b. the 14b will refused to start with Exception ``` ValueError: No available memory for the cache blocks. Try increasing `gpu_memory_utilization` when initializing the engine. ``` Note that the 14B vllm server outputs the following log ``` Memory profiling results: to...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding cuda;operator;quantization;triton buil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: sponse_ ### 🐛 Describe the bug I want to run Qwen2.5-14B-Instruct-GPTQ-Int4 and Qwen2.5-72B-Instruct-GPTQ-Int4 with one 80G A100. with following command ``` python3 -m vllm.entrypoints.openai.api_server \ --model /model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 5-14B-Instruct-GPTQ-Int4 and Qwen2.5-72B-Instruct-GPTQ-Int4 with one 80G A100. with following command ``` python3 -m vllm.entrypoints.openai.api_server \ --model /models/Qwen2.5-72B-Instruct-GPTQ-Int4 \ --gpu-memory-uti...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: ``` Note that the 14B vllm server outputs the following log ``` Memory profiling results: total_gpu_memory=79.15GiB initial_memory_usage=68.01GiB peak_torch_memory=10.77GiB memory_usage_post_profile=68.04Gib non_torch_m...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: o run two instance with one gpu bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to run Qwen2.5-14B-Instruct-GPTQ-Int4 and Qwen2.5-72B-Instruct-GPTQ-Int4 with one 80G A1...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
