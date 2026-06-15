# vllm-project/vllm#15330: [Performance]: poor performance in pipeline parallesm when batch-size is large

| 字段 | 值 |
| --- | --- |
| Issue | [#15330](https://github.com/vllm-project/vllm/issues/15330) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;scheduler_memory |
| 子分类 | throughput |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;slowdown |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: poor performance in pipeline parallesm when batch-size is large

### Issue 正文摘录

### Proposal to improve performance In the case where the lengths of the sent requests are the same, pipeline parallelism should have fewer bubbles, which also means that pipeline parallelism should have a higher throughput than tensor parallelism. However, when I issue requests with a batch size of 400 and a sequence length of 2048, the throughput of the Decode stage in tensor parallelism is nearly three times higher than that in pipeline parallelism. ![Image](https://github.com/user-attachments/assets/c40d96ec-3c99-41c6-85ad-4f7bca36fdae) ### Report of performance regression You can use the following script to reproduce the phenomenon that the performance of the Decode stage in pipeline parallelism is very poor as I mentioned. I sent 400 requests from the client to the started server, and the request configuration is that the input length is 2048 and the maximum output length is 1000. `nsys profile -o report.nsys-rep-pp-4-batch-micro-batch-100-python --trace-fork-before-exec=true --cuda-graph-trace=node --delay 120 --duration 120 --force-overwrite true --python-sampling=true vllm serve Qwen/Qwen2.5-14B-Instruct-1M --load-format dummy --pipeline-parallel-size 4 --no-enable-prefix...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: t is necessary to optimize the CPU overhead of pipeline parallelism. Especially in scenarios where the communication bandwidth between the GPUs is large, it is essential to use pipeline parallelism. ### Misc discussion...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Performance]: poor performance in pipeline parallesm when batch-size is large performance;stale ### Proposal to improve performance In the case where the lengths of the sent requests are the same, pipeline parallelism...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: sent 400 requests from the client to the started server, and the request configuration is that the input length is 2048 and the maximum output length is 1000. `nsys profile -o report.nsys-rep-pp-4-batch-micro-batch-100-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: r performance in pipeline parallesm when batch-size is large performance;stale ### Proposal to improve performance In the case where the lengths of the sent requests are the same, pipeline parallelism should have fewer...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: bubbles, which also means that pipeline parallelism should have a higher throughput than tensor parallelism. However, when I issue requests with a batch size of 400 and a sequence length of 2048, the throughput of the D...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
