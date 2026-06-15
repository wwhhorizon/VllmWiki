# vllm-project/vllm#8223: [Bug]: Poor TTFT performance with simultaneous --enable-chunked-prefill and --enable-prefix-caching

| 字段 | 值 |
| --- | --- |
| Issue | [#8223](https://github.com/vllm-project/vllm/issues/8223) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Poor TTFT performance with simultaneous --enable-chunked-prefill and --enable-prefix-caching

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description: I enabled both chunked prefix and prefix cache simultaneously using the following launch command: ```bash nohup python -m vllm.entrypoints.openai.api_server --enable-prefix-caching --tensor-parallel-size 1 --model meta-llama/Llama-2-13b-chat-hf --trust-remote-code --enable-chunked-prefill 1>vlog 2>&1 & ``` During benchmark testing, the input and output lengths were **3072** and **180**, respectively. From the logs, I observed that the **prefix cache hit rate** reaches **94.5%**, confirming that the cache mechanism is working. However, despite this high hit rate, the Time to First Token (TTFT) performance remains poor. Expected Behavior: With both chunked prefix and prefix cache enabled together, and with such a high prefix cache hit rate, I would expect a significant reduction in TTFT, as the caching mechanism should optimize the performance. Actual Behavior: The TTFT performance remains slow, and the expected benefits from enabling both caching mechanisms simultaneously are not realized. Benchmark Metrics: ```text ============ Serving Benchmark Result ============ Backend: vllm Concurrent num: 48 Successful requests...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: [Bug]: Poor TTFT performance with simultaneous --enable-chunked-prefill and --enable-prefix-caching bug;stale ### Your current environment ### 🐛 Describe the bug Description: I enabled both chunked prefix and prefix cac...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: hf --trust-remote-code --enable-chunked-prefill 1>vlog 2>&1 & ``` During benchmark testing, the input and output lengths were **3072** and **180**, respectively. From the logs, I observed that the **prefix cache hit rat...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory;speculative_decoding cuda;operator;triton build_error;s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: fix cache hit rate** reaches **94.5%**, confirming that the cache mechanism is working. However, despite this high hit rate, the Time to First Token (TTFT) performance remains poor. Expected Behavior: With both chunked...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: nts.openai.api_server --enable-prefix-caching --tensor-parallel-size 1 --model meta-llama/Llama-2-13b-chat-hf --trust-remote-code --enable-chunked-prefill 1>vlog 2>&1 & ``` During benchmark testing, the input and output...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
