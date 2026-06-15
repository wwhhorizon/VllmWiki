# vllm-project/vllm#18136: [Performance]: SGLANG is 4 times faster than vLLM for Qwen/Qwen3-32B-AWQ

| 字段 | 值 |
| --- | --- |
| Issue | [#18136](https://github.com/vllm-project/vllm/issues/18136) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: SGLANG is 4 times faster than vLLM for Qwen/Qwen3-32B-AWQ

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance vLLM command ``` VLLM_ATTENTION_BACKEND=FLASHINFER python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3-32B-AWQ --port 8000 --gpu-memory-utilization 0.90 --tensor-parallel-size 4 --disable-log-requests --quantization awq_marlin -O3 ``` SGLang command ``` python -m sglang.launch_server --model-path Qwen/Qwen3-32B-AWQ --port 8000 --tensor-parallel-size 4 --quantization awq_marlin --dtype auto --enable-torch-compile --attention-backend flashinfer --show-time-cost --enable-metrics ``` benchmarking command ``` vllm bench serve \ --model Qwen/Qwen3-32B-AWQ \ --num-prompts 50 \ --random-input-len 25000 \ --random-output-len 1024 \ --ignore-eos \ --request-rate inf \ ``` vLLM results ``` ============ Serving Benchmark Result ============ Successful requests: 50 Benchmark duration (s): 7303.93 Total input tokens: 1250000 Total generated tokens: 51200 Request throughput (req/s): 0.01 Output token throughput (tok/s): 7.01 Total Token throughput (tok/s): 178.15 ---------------Time to First Token---------------- Mean TTFT (ms): 2945424.93 Median TT...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: or-parallel-size 4 --quantization awq_marlin --dtype auto --enable-torch-compile --attention-backend flashinfer --show-time-cost --enable-metrics ``` benchmarking command ``` vllm bench serve \ --model Qwen/Qwen3-32B-AW...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance vLLM command ``` VLLM_ATTENTION_BACKEND=FLASHINFER python3 -m vllm.entrypoints.openai.ap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: onment information... PyTorch version: 2.7.0+cu126 Is debug build: False CUDA used to build PyTorch: 12.6 ROCM used to build PyTorch: N/A OS: Amazon Linux 2023.6.20250303 (x86_64) GCC version: (GCC) 11.4.1 20230605 (Red...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Performance]: SGLANG is 4 times faster than vLLM for Qwen/Qwen3-32B-AWQ performance;stale ### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on perf...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: e_ ### Misc discussion on performance vLLM command ``` VLLM_ATTENTION_BACKEND=FLASHINFER python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen3-32B-AWQ --port 8000 --gpu-memory-utilization 0.90 --tensor-parall...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
