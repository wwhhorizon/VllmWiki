# vllm-project/vllm#20079: [Bug]: Build from source - MAX_JOBS is very confusing and unintuitive

| 字段 | 值 |
| --- | --- |
| Issue | [#20079](https://github.com/vllm-project/vllm/issues/20079) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Build from source - MAX_JOBS is very confusing and unintuitive

### Issue 正文摘录

### Your current environment . ### 🐛 Describe the bug I have been confused about why building vllm from source was stuck using a single compiler thread despite setting MAX_JOBS from anywhere from 8 to 32 threads. Looking into the code it turns out that it gets divided by the number of NVCC_THREADS: https://github.com/vllm-project/vllm/blob/v0.9.1/setup.py#L92-L130 ```python class cmake_build_ext(build_ext): # A dict of extension directories that have been configured. did_config: dict[str, bool] = {} # # Determine number of compilation jobs and optionally nvcc compile threads. # def compute_num_jobs(self): # `num_jobs` is either the value of the MAX_JOBS environment variable # (if defined) or the number of CPUs available. num_jobs = envs.MAX_JOBS if num_jobs is not None: num_jobs = int(num_jobs) logger.info("Using MAX_JOBS=%d as the number of jobs.", num_jobs) else: try: # os.sched_getaffinity() isn't universally available, so fall # back to os.cpu_count() if we get an error here. num_jobs = len(os.sched_getaffinity(0)) except AttributeError: num_jobs = os.cpu_count() nvcc_threads = None if _is_cuda() and get_nvcc_cuda_version() >= Version("11.2"): # `nvcc_threads` is either the va...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Build from source - MAX_JOBS is very confusing and unintuitive bug;stale ### Your current environment . ### 🐛 Describe the bug I have been confused about why building vllm from source was stuck using a single com...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: num_jobs = os.cpu_count() nvcc_threads = None if _is_cuda() and get_nvcc_cuda_version() >= Version("11.2"): # `nvcc_threads` is either the value of the NVCC_THREADS # environment variable (if defined) or 1. # when it is...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: gger.info("Using MAX_JOBS=%d as the number of jobs.", num_jobs) else: try: # os.sched_getaffinity() isn't universally available, so fall # back to os.cpu_count() if we get an error here. num_jobs = len(os.sched_getaffin...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ild_ext(build_ext): # A dict of extension directories that have been configured. did_config: dict[str, bool] = {} # # Determine number of compilation jobs and optionally nvcc compile threads. # def compute_num_jobs(self...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Bug]: Build from source - MAX_JOBS is very confusing and unintuitive bug;stale ### Your current environment . ### 🐛 Describe the bug I have been confused about why building vllm from source was stuck using a single comp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
