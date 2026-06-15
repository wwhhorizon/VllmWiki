# vllm-project/vllm#12059: [Bug]: Memory profiler does not consider CUDA context memory

| 字段 | 值 |
| --- | --- |
| Issue | [#12059](https://github.com/vllm-project/vllm/issues/12059) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Memory profiler does not consider CUDA context memory

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Issue #10451 highlights a problem in previous memory profiling strategy, and #10511 overhauls the profiler to return the old behavior. Current vLLM takes an initial measurement in `Worker.init_device()` that calculates `self.init_gpu_memory` ([worker.py#L143](https://github.com/vllm-project/vllm/blob/87054a57ab39bad6c7fe8999e7d93566ded713e3/vllm/worker/worker.py#L143)), and uses this as a baseline to calculate the amount of non-torch memory used. The function of this baseline is to be used in the memory profiling as described in [utils.py#L1971](https://github.com/vllm-project/vllm/blob/87054a57ab39bad6c7fe8999e7d93566ded713e3/vllm/utils.py#L1971): > baseline_memory_in_bytes: memory used by all the components other than the current vLLM instance. It contains: memory used by other processes, memory used by another vLLM instance in the same process, etc. It is usually measured before the current vLLM instance initialize the device. And we assume it is constant during the profiling of the current vLLM instance. Using `torch.cuda.mem_get_info()` to compute this baseline violates this assumption. Th...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: currently used with `nvidia-smi`, and then run the following: ```python import torch free, total = torch.cuda.mem_get_info() print(f"Total GPU memory usage: {(total - free) / (1024**2):.2f} MB") ``` The exact discrepanc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: Memory profiler does not consider CUDA context memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Issue #10451 highlights a problem in previous memory profili...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug]: Memory profiler does not consider CUDA context memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Issue #10451 highlights a problem in previous memory profili...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: sider CUDA context memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Issue #10451 highlights a problem in previous memory profiling strategy, and #10511 overhauls t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Memory profiler does not consider CUDA context memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug Issue #10451 highlights a problem in previous memory profili...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
