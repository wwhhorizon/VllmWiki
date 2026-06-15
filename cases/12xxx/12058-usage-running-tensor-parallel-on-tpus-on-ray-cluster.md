# vllm-project/vllm#12058: [Usage]: Running Tensor Parallel on TPUs on Ray Cluster

| 字段 | 值 |
| --- | --- |
| Issue | [#12058](https://github.com/vllm-project/vllm/issues/12058) |
| 状态 | closed |
| 标签 | usage;tpu;ray |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 |  |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Running Tensor Parallel on TPUs on Ray Cluster

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` The output of `python collect_env.py` (test_hf_qwen pid=17527, ip=10.130.4.26) Environment Information: (test_hf_qwen pid=17527, ip=10.130.4.26) Collecting environment information... (test_hf_qwen pid=17527, ip=10.130.4.26) PyTorch version: 2.6.0.dev20241126+cpu (test_hf_qwen pid=17527, ip=10.130.4.26) Is debug build: False (test_hf_qwen pid=17527, ip=10.130.4.26) CUDA used to build PyTorch: None (test_hf_qwen pid=17527, ip=10.130.4.26) ROCM used to build PyTorch: N/A (test_hf_qwen pid=17527, ip=10.130.4.26) (test_hf_qwen pid=17527, ip=10.130.4.26) OS: Ubuntu 22.04.4 LTS (x86_64) (test_hf_qwen pid=17527, ip=10.130.4.26) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 (test_hf_qwen pid=17527, ip=10.130.4.26) Clang version: 14.0.0-1ubuntu1.1 (test_hf_qwen pid=17527, ip=10.130.4.26) CMake version: version 3.31.2 (test_hf_qwen pid=17527, ip=10.130.4.26) Libc version: glibc-2.35 (test_hf_qwen pid=17527, ip=10.130.4.26) (test_hf_qwen pid=17527, ip=10.130.4.26) Python version: 3.11.9 (main, Apr 19 2024, 16:48:06) [GCC 11.2.0] (64-bit runtime) (test_hf_qwen pid=17527, ip=10.130.4.26) Python platform: Linux-5.19....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: ironment information... (test_hf_qwen pid=17527, ip=10.130.4.26) PyTorch version: 2.6.0.dev20241126+cpu (test_hf_qwen pid=17527, ip=10.130.4.26) Is debug build: False (test_hf_qwen pid=17527, ip=10.130.4.26) CUDA used t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: t of `python collect_env.py` The output of `python collect_env.py` (test_hf_qwen pid=17527, ip=10.130.4.26) Environment Information: (test_hf_qwen pid=17527, ip=10.130.4.26) Collecting environment information... (test_h...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: 130.4.26) Is debug build: False (test_hf_qwen pid=17527, ip=10.130.4.26) CUDA used to build PyTorch: None (test_hf_qwen pid=17527, ip=10.130.4.26) ROCM used to build PyTorch: N/A (test_hf_qwen pid=17527, ip=10.130.4.26)...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Not affected (test_hf_qwen pid=17527, ip=10.130.4.26) Vulnerability Mmio stale data: Not affected (test_hf_qwen pid=17527, ip=10.130.4.26) Vulnerability Retbleed: Mitigation; untrained return thunk; SMT enabled with STI...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: p3] transformers==4.47.1 (test_hf_qwen pid=17527, ip=10.130.4.26) [pip3] triton==3.1.0 (test_hf_qwen pid=17527, ip=10.130.4.26) [conda] numpy 1.26.4 pypi_0 pypi (test_hf_qwen pid=17527, ip=10.130.4.26) [conda] nvidia-cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
