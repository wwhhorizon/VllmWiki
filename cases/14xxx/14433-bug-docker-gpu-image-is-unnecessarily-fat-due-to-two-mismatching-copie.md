# vllm-project/vllm#14433: [Bug]: Docker GPU image is unnecessarily fat due to two (mismatching) copies of CUDA runtime libraries

| 字段 | 值 |
| --- | --- |
| Issue | [#14433](https://github.com/vllm-project/vllm/issues/14433) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker GPU image is unnecessarily fat due to two (mismatching) copies of CUDA runtime libraries

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The current (v0.7.3) Docker GPU image contains two copies of CUDA runtime libraries. For example: ```console $ docker run --rm -it --entrypoint "" vllm/vllm-openai:v0.7.3 find / -name 'libcublas.so*' -not -path /root/.cache/uv /usr/local/lib/python3.12/dist-packages/nvidia/cublas/lib/libcublas.so.12 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcublas.so /usr/local/cuda-12.1/targets/x86_64-linux/lib/stubs/libcublas.so /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcublas.so.12 /usr/local/cuda-12.1/targets/x86_64-linux/lib/libcublas.so.12.1.0.26 /root/.cache/uv/archive-v0/-KWKPTFUBTDIMe_pZFAMD/nvidia/cublas/lib/libcublas.so.12 ``` (I'm ignoring `/root/.cache/uv`, as #13611 fixed the cache path issue but is not included in the v0.7.3 release.) Notice that there are two installations of CUDA at `/usr/local/lib/python3.12/dist-packages/nvidia/**` and `/usr/local/cuda-12.1/**`. That's because the [image is based on `nvidia/cuda:${CUDA_VERSION}-devel-ubuntu22.04`](https://github.com/vllm-project/vllm/blob/cc10281498fc2a6eb804274dcf22e6cb766f7aa7/Dockerfile#L166C6-L166C51), which contains CUDA libraries at `/usr/local/cuda-12.1/**`...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Docker GPU image is unnecessarily fat due to two (mismatching) copies of CUDA runtime libraries bug;stale ### Your current environment ### 🐛 Describe the bug The current (v0.7.3) Docker GPU image contains two cop...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Docker GPU image is unnecessarily fat due to two (mismatching) copies of CUDA runtime libraries bug;stale ### Your current environment ### 🐛 Describe the bug The current (v0.7.3) Docker GPU image contains two cop...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: sarily fat due to two (mismatching) copies of CUDA runtime libraries bug;stale ### Your current environment ### 🐛 Describe the bug The current (v0.7.3) Docker GPU image contains two copies of CUDA runtime libraries. For...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: Docker GPU image is unnecessarily fat due to two (mismatching) copies of CUDA runtime libraries bug;stale ### Your current environment ### 🐛 Describe the bug The current (v0.7.3) Docker GPU image contains two cop...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
