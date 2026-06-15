# vllm-project/vllm#37941: [Usage]: Using RIXL Connector on AMD GPU

| 字段 | 值 |
| --- | --- |
| Issue | [#37941](https://github.com/vllm-project/vllm/issues/37941) |
| 状态 | open |
| 标签 | rocm;usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Using RIXL Connector on AMD GPU

### Issue 正文摘录

### Your current environment I have successfully used the Mooncake connector on AMD GPUs, and now I'm trying to use the Nixl connector for PD disaggregation. I am in an air-gapped environment, so building Docker images is quite difficult. 1. Is there any prebuilt Docker image based on this Dockerfile? https://github.com/vllm-project/vllm/blob/main/docker/Dockerfile.rocm 2. The documentation states: For ROCm platform, the base ROCm docker file includes RIXL and ucx already. https://docs.vllm.ai/en/stable/features/nixl_connector_usage/#prerequisites But I tested vllm/vllm-openai-rocm:latest, but rixl is not installed (ModuleNotFoundError). Could anyone clarify whether the official Docker images include RIXL or not? 3. Is NixlConnector on ROCm intended to support communication with NVIDIA GPUs (cross-vendor), or only AMD-to-AMD?

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: l connector for PD disaggregation. I am in an air-gapped environment, so building Docker images is quite difficult. 1. Is there any prebuilt Docker image based on this Dockerfile? https://github.com/vllm-project/vllm/bl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [Usage]: Using RIXL Connector on AMD GPU rocm;usage ### Your current environment I have successfully used the Mooncake connector on AMD GPUs, and now I'm trying to use the Nixl connector for PD disaggregation. I am in a...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ocs.vllm.ai/en/stable/features/nixl_connector_usage/#prerequisites But I tested vllm/vllm-openai-rocm:latest, but rixl is not installed (ModuleNotFoundError). Could anyone clarify whether the official Docker images incl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
