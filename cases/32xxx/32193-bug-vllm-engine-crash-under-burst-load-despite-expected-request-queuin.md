# vllm-project/vllm#32193: [Bug]: vLLM engine crash under burst load despite expected request queuing (72 concurrent API calls)

| 字段 | 值 |
| --- | --- |
| Issue | [#32193](https://github.com/vllm-project/vllm/issues/32193) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;multimodal_vlm |
| 子分类 | latency_reg |
| Operator 关键词 | gemm |
| 症状 | crash;oom;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vLLM engine crash under burst load despite expected request queuing (72 concurrent API calls)

### Issue 正文摘录

### Your current environment ### **Description** We observed that the **vLLM engine was killed** when a burst of API requests hit the server (approximately **72 API requests from two servers simultaneously**). Based on vLLM’s design, we expected these requests to be **queued and throttled internally**, rather than causing the engine to terminate. This behavior is unexpected and impacts stability during performance and E2E testing. --- ### **Expected Behavior** * Incoming requests should be **queued** once `max-num-seqs` or batching limits are reached. * Engine should **gracefully handle burst traffic**, even if latency increases. * No engine crash or process termination under moderate concurrent load. --- ### **Actual Behavior** * Engine process was **killed** when ~72 concurrent API requests were sent. * Requests were not fully queued or back-pressured as expected. * This resulted in **service unavailability** during testing. --- ### **Reproduction Steps** 1. Deploy vLLM with the configuration below. 2. Send ~72 concurrent multimodal API requests from two different servers. 3. Observe engine termination instead of queuing or throttling. --- ### **vLLM Serve Command** ```bash vllm...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: uring testing. --- ### **Reproduction Steps** 1. Deploy vLLM with the configuration below. 2. Send ~72 concurrent multimodal API requests from two different servers. 3. Observe engine termination instead of queuing or t...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 528 \ --tensor-parallel-size 1 \ --gpu-memory-utilization 0.75 \ --dtype bfloat16 \ --host 0.0.0.0 \ --port 7000 \ --limit-mm-per-prompt.video 0 \ --mm-encoder-tp-mode data \ --max-num-batched-tokens 22528 \ --max-num-s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: vLLM engine crash under burst load despite expected request queuing (72 concurrent API calls) bug;stale ### Your current environment ### **Description** We observed that the **vLLM engine was killed** when a burs...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e-code \ --enable-log-requests ``` ### 🐛 Describe the bug I am using A100 80GB machine Questions Is there a hard concurrency limit (especially for multimodal requests) beyond max-num-seqs? Are there known scenarios wher...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: behavior is unexpected and impacts stability during performance and E2E testing. --- ### **Expected Behavior** * Incoming requests should be **queued** once `max-num-seqs` or batching limits are reached. * Engine should...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
