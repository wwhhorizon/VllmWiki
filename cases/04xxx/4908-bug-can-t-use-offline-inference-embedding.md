# vllm-project/vllm#4908: [Bug]: Can't use offline inference embedding

| 字段 | 值 |
| --- | --- |
| Issue | [#4908](https://github.com/vllm-project/vllm/issues/4908) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't use offline inference embedding

### Issue 正文摘录

### Your current environment Collecting environment information... /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_cnn_infer.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_cnn_train.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_ops_infer.so.8 /usr/local/cuda-11.3/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.7/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11.7/targets/x86...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: l/cuda-11.7/targets/x86_64-linux/lib/libcudnn_ops_train.so.8 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: True CPU: Architecture: x86_64 CPU op-mode(s): 32-bit, 64-bit Address sizes: 52 bit...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: r current environment Collecting environment information... /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_train.so.8 /usr/local/cuda-11....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nce embedding bug ### Your current environment Collecting environment information... /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_infer.so.8 /usr/local/cuda-11.1/targets/x86_64-linux/lib/libcudnn_adv_train...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: numpy==1.26.4 [pip3] nvidia-nccl-cu12==2.20.5 [pip3] torch==2.3.0 [pip3] triton==2.3.0 [pip3] vllm_nccl_cu12==2.18.1.0.4.0 [conda] numpy 1.26.4 pypi_0 pypi [conda] nvidia-nccl-cu12 2.20.5 pypi_0 pypi [conda] torch
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: k overflow: Not affected Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl Vulnerability Spectre v1: Mitigation; usercopy/swapgs barriers and __user pointer sanitization Vulnerabil...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
