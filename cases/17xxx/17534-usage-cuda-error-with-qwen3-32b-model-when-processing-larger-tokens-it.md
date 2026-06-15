# vllm-project/vllm#17534: [Usage]: CUDA Error with Qwen3-32B Model When Processing larger tokens it leads to model went to non responsive condition / stability concerns

| 字段 | 值 |
| --- | --- |
| Issue | [#17534](https://github.com/vllm-project/vllm/issues/17534) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;hardware_porting;model_support;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cache;cuda |
| 症状 | crash;slowdown |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: CUDA Error with Qwen3-32B Model When Processing larger tokens it leads to model went to non responsive condition / stability concerns

### Issue 正文摘录

### Your current environment **Environment** vLLM version: 0.8.5 Model: Qwen/Qwen3-32B Kubernetes deployment with 4 GPUs (tensor-parallel-size=4) GPU memory utilization: 0.95 Max model length: 131072 Max sequence length to capture: 131072 **Issue Description** When benchmarking the Qwen3-32B model with llmperf using 100,000 input tokens and 2,000 output tokens, the model crashes with a CUDA error: CUDA error (/workspace/.deps/vllm-flash-attn-src/hopper/flash_fwd_launch_template.h:161): an illegal memory access was encountered INFO: 127.0.0.6:48593 - "GET /health HTTP/1.1" 200 OK ERROR 05-01 05:31:52 [multiproc_worker_utils.py:120] Worker VllmWorkerProcess pid 220 died, exit code: 1 INFO 05-01 05:31:52 [multiproc_worker_utils.py:124] Killing local vLLM worker processes **Observed Behavior** - The model appears to accept requests (showing "POST /v1/chat/completions HTTP/1.1" 200 OK in logs) - However, it doesn't process them properly - no metrics are logged showing token throughput - Eventually, the model crashes with the CUDA illegal memory access error - This requires restarting the model service repeatedly **Expected Behavior** The model should either: - Successfully process the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Usage]: CUDA Error with Qwen3-32B Model When Processing larger tokens it leads to model went to non responsive condition / stability concerns usage;stale ### Your current environment **Environment** vLLM version: 0.8.5...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: ads to model went to non responsive condition / stability concerns usage;stale ### Your current environment **Environment** vLLM version: 0.8.5 Model: Qwen/Qwen3-32B Kubernetes deployment with 4 GPUs (tensor-parallel-si...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: concerns usage;stale ### Your current environment **Environment** vLLM version: 0.8.5 Model: Qwen/Qwen3-32B Kubernetes deployment with 4 GPUs (tensor-parallel-size=4) GPU memory utilization: 0.95 Max model length: 13107...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: CUDA Error with Qwen3-32B Model When Processing larger tokens it leads to model went to non responsive condition / stability concerns usage;stale ### Your current environment **Environment** vLLM version: 0.8.5...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: 31072 Max sequence length to capture: 131072 **Issue Description** When benchmarking the Qwen3-32B model with llmperf using 100,000 input tokens and 2,000 output tokens, the model crashes with a CUDA error: CUDA error (...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
