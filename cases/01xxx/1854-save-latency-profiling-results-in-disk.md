# vllm-project/vllm#1854: Save latency profiling results in disk

| 字段 | 值 |
| --- | --- |
| Issue | [#1854](https://github.com/vllm-project/vllm/issues/1854) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Save latency profiling results in disk

### Issue 正文摘录

How about something like this: ```python model_name = args.model.replace("/", "-") profile_logdir_name = os.path.join( args.profile_logdir, f"{model_name}_tp-{args.tensor_parallel_size}_input-len{args.input_len}_output-len{args.output_len}_batch-size{args.batch_size}" .lstrip("-")) with torch.profiler.profile( activities=[ torch.profiler.ProfilerActivity.CPU, torch.profiler.ProfilerActivity.CUDA ], on_trace_ready=torch.profiler.tensorboard_trace_handler( profile_logdir_name), with_stack=True): ... ``` that way a JSON trace file will be saved which can be analyzed with tensorboard/perfetto (super useful!). `profile_logdir` will need to be added to CLI args. _Originally posted by @Yard1 in https://github.com/vllm-project/vllm/issues/1839#issuecomment-1832836922_

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: Save latency profiling results in disk How about something like this: ```python model_name = args.model.replace("/", "-") profile_logdir_name = os.path.join( args.profile_logdir, f"{model_name}_tp-{args.tensor_paralle
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 839#issuecomment-1832836922_ performance model_support cuda slowdown env_dependency How about something like this:
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: h.profiler.ProfilerActivity.CPU, torch.profiler.ProfilerActivity.CUDA ], on_trace_ready=torch.profiler.tensorboard_trace_handler( profile_logdir_name), with_stack=True): ... ``` that way a JSON trace file will be saved...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: tency profiling results in disk How about something like this: ```python model_name = args.model.replace("/", "-") profile_logdir_name = os.path.join( args.profile_logdir, f"{model_name}_tp-{args.tensor_parallel_size}_i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
