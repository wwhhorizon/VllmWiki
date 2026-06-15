# vllm-project/vllm#4803: [Performance]: how to test tensorrt-llm serving correctly

| 字段 | 值 |
| --- | --- |
| Issue | [#4803](https://github.com/vllm-project/vllm/issues/4803) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;quantization;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: how to test tensorrt-llm serving correctly

### Issue 正文摘录

### Proposal to improve performance Hi, how to test tensorrt-llm serving correctly? I've tested on llama2-8b-chat and llama3-8b and the performances are too bad for TTFT. Could you tell me where goes wrong? THX I use docker image `nvcr.io/nvidia/tritonserver:24.04-trtllm-python-py3` and follow this doc https://github.com/triton-inference-server/tensorrtllm_backend/blob/main/docs/llama.md This is the results for request rate=7 ``` Traffic request rate: 7.0 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [02:05<00:00, 1.25s/it] ============ Serving Benchmark Result ============ Successful requests: 100 Benchmark duration (s): 125.17 Total input tokens: 22925 Total generated tokens: 21752 Request throughput (req/s): 0.80 Input token throughput (tok/s): 183.14 Output token throughput (tok/s): 173.77 ---------------Time to First Token---------------- Mean TTFT (ms): 47395.15 Median TTFT (ms): 45446.53 P99 TTFT (ms): 96636.63 -----Time per Output Token (excl. 1st token)------ Mean TPOT (ms): 19.38 Median TPOT (ms): 18.76 P99 TPOT (ms): 25.42 ``` related issue: https://github.com/triton-inference-server/tensorrtllm_bac...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ces are too bad for TTFT. Could you tell me where goes wrong? THX I use docker image `nvcr.io/nvidia/tritonserver:24.04-trtllm-python-py3` and follow this doc https://github.com/triton-inference-server/tensorrtllm_backe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: s necessary) ```text PyTorch version: 2.3.0+cu121 Is debug build: False CUDA used to build PyTorch: 12.1 ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Performance]: how to test tensorrt-llm serving correctly performance ### Proposal to improve performance Hi, how to test tensorrt-llm serving correctly? I've tested on llama2-8b-chat and llama3-8b and the performances...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: formance Hi, how to test tensorrt-llm serving correctly? I've tested on llama2-8b-chat and llama3-8b and the performances are too bad for TTFT. Could you tell me where goes wrong? THX I use docker image `nvcr.io/nvidia/...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: er/tensorrtllm_backend/blob/main/docs/llama.md This is the results for request rate=7 ``` Traffic request rate: 7.0 100%|██████████████████████████████████████████████████████████████████████████████████████████████████...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
