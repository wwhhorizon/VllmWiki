# vllm-project/vllm#16518: [Bug]: GPU index bug really critical

| 字段 | 值 |
| --- | --- |
| Issue | [#16518](https://github.com/vllm-project/vllm/issues/16518) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPU index bug really critical

### Issue 正文摘录

### Your current environment 0.73 ~ version def init_device(self) -> None: if self.device_config.device.type == "cuda": # torch.distributed.all_reduce does not free the input tensor until # the synchronization point. This causes the memory usage to grow # as the number of all_reduce calls increases. This env var disables # this behavior. # Related issue: # https://discuss.pytorch.org/t/cuda-allocation-lifetime-for-inputs-to-distributed-all-reduce/191573 os.environ["TORCH_NCCL_AVOID_RECORD_STREAMS"] = "1" # This env var set by Ray causes exceptions with graph building. os.environ.pop("NCCL_ASYNC_ERROR_HANDLING", None) self.device = torch.device(f"cuda:{self.local_rank}") # torch.cuda.set_device(self.device) ### This is the problem. Should be deleted when we use accelerator both!!!!!!!!!!!!!!!!!!!!!!!!! _check_if_gpu_supports_dtype(self.model_config.dtype) gc.collect() torch.cuda.empty_cache() torch.cuda.reset_peak_memory_stats() self.baseline_snapshot = MemorySnapshot() else: raise RuntimeError( f"Not support device type: {self.device_config.device}") # Initialize the distributed environment. init_worker_distributed_environment(self.vllm_config, self.rank, self.distributed_init_met...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: index bug really critical bug;stale ### Your current environment 0.73 ~ version def init_device(self) -> None: if self.device_config.device.type == "cuda": # torch.distributed.all_reduce does not free the input tensor u...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: init_device(self) -> None: if self.device_config.device.type == "cuda": # torch.distributed.all_reduce does not free the input tensor until # the synchronization point. This causes the memory usage to grow # as the numb...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: .73 ~ version def init_device(self) -> None: if self.device_config.device.type == "cuda": # torch.distributed.all_reduce does not free the input tensor until # the synchronization point. This causes the memory usage to...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GPU index bug really critical bug;stale ### Your current environment 0.73 ~ version def init_device(self) -> None: if self.device_config.device.type == "cuda": # torch.distributed.all_reduce does not free the inp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: erator both!!!!!!!!!!!!!!!!!!!!!!!!! _check_if_gpu_supports_dtype(self.model_config.dtype) gc.collect() torch.cuda.empty_cache() torch.cuda.reset_peak_memory_stats() self.baseline_snapshot = MemorySnapshot() else:

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
