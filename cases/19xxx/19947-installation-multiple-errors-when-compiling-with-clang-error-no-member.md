# vllm-project/vllm#19947: [Installation]: Multiple errors when compiling with clang: error: no member named 'min'. fmax

| 字段 | 值 |
| --- | --- |
| Issue | [#19947](https://github.com/vllm-project/vllm/issues/19947) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: Multiple errors when compiling with clang: error: no member named 'min'. fmax

### Issue 正文摘录

### Your current environment ```text (.venv) ) zedr@zaonce 0 ~/src/vllm $ python vllm/collect_env.py Traceback (most recent call last): File "/home/zedr/src/vllm/vllm/collect_env.py", line 17, in from vllm.envs import environment_variables ModuleNotFoundError: No module named 'vllm' ((.venv) ) zedr@zaonce 0 ~/src/vllm $ python ./.venv/lib/python3.12/site-packages/torch/utils/collect_env.py Collecting environment information... PyTorch version: 2.8.0.dev20250621+rocm6.3 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42131-fa1d09cbd OS: Fedora Linux 42 (Workstation Edition) (x86_64) GCC version: (GCC) 15.1.1 20250521 (Red Hat 15.1.1-2) Clang version: 20.1.6 (Fedora 20.1.6-1.fc42) CMake version: version 3.31.6 Libc version: glibc-2.41 Python version: 3.12.11 (main, Jun 4 2025, 00:00:00) [GCC 15.1.1 20250521 (Red Hat 15.1.1-2)] (64-bit runtime) Python platform: Linux-6.14.9-300.fc42.x86_64-x86_64-with-glibc2.41 Is CUDA available: True CUDA runtime version: Could not collect CUDA_MODULE_LOADING set to: LAZY GPU models and configuration: AMD Radeon Graphics (gfx1030) Nvidia driver version: Could not collect cuDNN version: Could not collect HIP runt...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 10: [Installation]: Multiple errors when compiling with clang: error: no member named 'min'. fmax installation;stale ### Your current environment ```text (.venv) ) zedr@zaonce 0 ~/src/vllm $ python vllm/collect_env.py Traceb
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: Collecting environment information... PyTorch version: 2.8.0.dev20250621+rocm6.3 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.42131-fa1d09cbd OS: Fedora Linux 42 (Workstation Edi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: on3.12/site-packages/torch/utils/collect_env.py Collecting environment information... PyTorch version: 2.8.0.dev20250621+rocm6.3 Is debug build: False CUDA used to build PyTorch: N/A ROCM used to build PyTorch: 6.3.4213...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: en compiling with clang: error: no member named 'min'. fmax installation;stale ### Your current environment ```text (.venv) ) zedr@zaonce 0 ~/src/vllm $ python vllm/collect_env.py Traceback (most recent call last): File...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ted Versions of relevant libraries: [pip3] numpy==1.26.4 [pip3] pytorch-triton-rocm==3.3.1+gitc8757738 [pip3] torch==2.8.0.dev20250621+rocm6.3 [pip3] triton==3.2.0+gite5be006a [conda] Could not collect ``` ### How you a...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
