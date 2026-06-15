# vllm-project/vllm#26774: [Usage]: how to use vllm on CUDA 12.9

| 字段 | 值 |
| --- | --- |
| Issue | [#26774](https://github.com/vllm-project/vllm/issues/26774) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 |  |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: how to use vllm on CUDA 12.9

### Issue 正文摘录

### Your current environment ```text Traceback (most recent call last): File "/vllm-workspace/collect_env.py", line 825, in main() File "/vllm-workspace/collect_env.py", line 804, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/vllm-workspace/collect_env.py", line 799, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/vllm-workspace/collect_env.py", line 619, in get_env_info cuda_module_loading=get_cuda_module_loading_config(), ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/vllm-workspace/collect_env.py", line 540, in get_cuda_module_loading_config torch.cuda.init() File "/usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py", line 339, in init _lazy_init() File "/usr/local/lib/python3.12/dist-packages/torch/cuda/__init__.py", line 372, in _lazy_init torch._C._cuda_init() RuntimeError: No CUDA GPUs are available root@test2222-7dcd6b94b7-wl6w4:/vllm-workspace# python3 --version Python 3.12.1 ``` ### How would you like to use vllm My node CUDA version is 12.9, and the running pod image CUDA variable is 12.8. Will this cause the No CUDA GPUs are available error? Is 12.9 compatible with version 12.8? Should we upgrade the VLLM version...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: are available root@test2222-7dcd6b94b7-wl6w4:/vllm-workspace# python3 --version Python 3.12.1 ``` ### How would you like to use vllm My node CUDA version is 12.9, and the running pod image CUDA variable is 12.8. Will th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Usage]: how to use vllm on CUDA 12.9 usage;stale ### Your current environment ```text Traceback (most recent call last): File "/vllm-workspace/collect_env.py", line 825, in main() File "/vllm-workspace/collect_env.py",...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ine 619, in get_env_info cuda_module_loading=get_cuda_module_loading_config(), ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/vllm-workspace/collect_env.py", line 540, in get_cuda_module_loading_config torch.cuda.init() File "...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: how to use vllm on CUDA 12.9 usage;stale ### Your current environment ```text Traceback (most recent call last): File "/vllm-workspace/collect_env.py", line 825, in main() File "/vllm-workspace/collect_env.py",...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: torch._C._cuda_init() RuntimeError: No CUDA GPUs are available root@test2222-7dcd6b94b7-wl6w4:/vllm-workspace# python3 --version Python 3.12.1 ``` ### How would you like to use vllm My node CUDA version is 12.9, and the...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
