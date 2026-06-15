# vllm-project/vllm#24943: [Bug]:Worker failed with error 'CUDAGraphMode.FULL_AND_PIECEWISE is not supported with FlexAttentionMetadataBuilder backend (support:AttentionCGSupport.NEVER) ; please try cudagraph_mode=PIECEWISE

| 字段 | 值 |
| --- | --- |
| Issue | [#24943](https://github.com/vllm-project/vllm/issues/24943) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:Worker failed with error 'CUDAGraphMode.FULL_AND_PIECEWISE is not supported with FlexAttentionMetadataBuilder backend (support:AttentionCGSupport.NEVER) ; please try cudagraph_mode=PIECEWISE

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm serve Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 8 --max-model-len 32768 --max-num-seqs 64 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8080 --disable-log-requests --served-model-name Qwen3-Next-80B-A3B-Instruct --no-enable-chunked-prefill --enable-prefix-caching --max-num-batched-tokens 9000 --trust-remote-code error: (Worker_TP1 pid=9634) ERROR 09-16 14:11:36 [multiproc_executor.py:654] WorkerProc hit an exception. (Worker_TP4 pid=9637) ERROR 09-16 14:11:36 [multiproc_executor.py:654] WorkerProc hit an exception. (Worker_TP2 pid=9635) ERROR 09-16 14:11:36 [multiproc_executor.py:654] WorkerProc hit an exception. (Worker_TP6 pid=9639) ERROR 09-16 14:11:36 [multiproc_executor.py:654] WorkerProc hit an exception. (Worker_TP3 pid=9636) ERROR 09-16 14:11:36 [multiproc_executor.py:654] WorkerProc hit an exception. (Worker_TP1 pid=9634) ERROR 09-16 14:11:36 [multiproc_executor.py:654] Traceback (most recent call last): (Worker_TP4 pid=9637) ERROR 09-16 14:11:36 [multiproc_executor.py:654] Traceback (most recent call last): (Worker_TP0 pid=9633) ERROR 09-16 14:11:36 [multiproc_executor.py:654] WorkerProc hit an excep...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: port:AttentionCGSupport.NEVER) ; please try cudagraph_mode=PIECEWISE bug;stale ### Your current environment ### 🐛 Describe the bug vllm serve Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 8 --max-model-len 32768 --...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: AGraphMode.FULL_AND_PIECEWISE is not supported with FlexAttentionMetadataBuilder backend (support:AttentionCGSupport.NEVER) ; please try cudagraph_mode=PIECEWISE bug;stale ### Your current environment ### 🐛 Describe the...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: de.FULL_AND_PIECEWISE is not supported with FlexAttentionMetadataBuilder backend (support:AttentionCGSupport.NEVER) ; please try cudagraph_mode=PIECEWISE bug;stale ### Your current environment ### 🐛 Describe the bug vll...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: tale ### Your current environment ### 🐛 Describe the bug vllm serve Qwen3-Next-80B-A3B-Instruct --tensor-parallel-size 8 --max-model-len 32768 --max-num-seqs 64 --gpu-memory-utilization 0.95 --host 0.0.0.0 --port 8080 -...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]:Worker failed with error 'CUDAGraphMode.FULL_AND_PIECEWISE is not supported with FlexAttentionMetadataBuilder backend (support:AttentionCGSupport.NEVER) ; please try cudagraph_mode=PIECEWISE bug;stale ### Your cur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
