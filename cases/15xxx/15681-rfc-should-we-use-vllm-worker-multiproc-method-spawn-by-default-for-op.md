# vllm-project/vllm#15681: [RFC]: should we use `VLLM_WORKER_MULTIPROC_METHOD=spawn` by default for openai-compatible api server ?

| 字段 | 值 |
| --- | --- |
| Issue | [#15681](https://github.com/vllm-project/vllm/issues/15681) |
| 状态 | closed |
| 标签 | RFC |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | runtime_err |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [RFC]: should we use `VLLM_WORKER_MULTIPROC_METHOD=spawn` by default for openai-compatible api server ?

### Issue 正文摘录

### Motivation. I’ve recently encountered this error: ``` RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method ``` And I always have to specify `VLLM_WORKER_MULTIPROC_METHOD=spawn` to bypass the issue, so I investigated the cause. vllm forces `VLLM_WORKER_MULTIPROC_METHOD=spawn` when `torch.cuda.is_initialized()` is True, but that’s not enough. In PyTorch, when the main process runs `poison_fork` and then forks a subprocess, the subprocess's `in_bad_fork` gets set to true. Therefore, when the subprocess attempts to reinitialize CUDA, it throws an error. https://github.com/pytorch/pytorch/blob/v2.6.0/torch/csrc/cuda/Module.cpp#L63-L79 However, `poison_fork` doesn't only run during `torch._C._cuda_init`. It also runs during `torch._C._cuda_getDeviceCount` and `torch._C._cuda_getArchFlags`. So if we use the fork method, we can't call methods like `torch.cuda.is_available()` or `torch.cuda.device_count()` in the main process. Even though we can ensure these methods don’t create subprocesses before execution within the vllm library, we can’t guarantee that all dependencies won’t (for example, `is_flash_att...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: sing, you must use the 'spawn' start method ``` And I always have to specify `VLLM_WORKER_MULTIPROC_METHOD=spawn` to bypass the issue, so I investigated the cause. vllm forces `VLLM_WORKER_MULTIPROC_METHOD=spawn` when `...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: recently encountered this error: ``` RuntimeError: Cannot re-initialize CUDA in forked subprocess. To use CUDA with multiprocessing, you must use the 'spawn' start method ``` And I always have to specify `VLLM_WORKER_MU...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: so runs during `torch._C._cuda_getDeviceCount` and `torch._C._cuda_getArchFlags`. So if we use the fork method, we can't call methods like `torch.cuda.is_available()` or `torch.cuda.device_count()` in the main process....
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. development frontend_api cuda env_dependency Motivation.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
