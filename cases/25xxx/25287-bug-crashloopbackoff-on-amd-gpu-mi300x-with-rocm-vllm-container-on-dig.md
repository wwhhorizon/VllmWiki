# vllm-project/vllm#25287: [Bug]: CrashLoopBackOff on AMD GPU (MI300x) with rocm/vllm Container on DigitalOcean Kubernetes

| 字段 | 值 |
| --- | --- |
| Issue | [#25287](https://github.com/vllm-project/vllm/issues/25287) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;hardware_porting;quantization |
| 子分类 | install |
| Operator 关键词 | fp8 |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: CrashLoopBackOff on AMD GPU (MI300x) with rocm/vllm Container on DigitalOcean Kubernetes

### Issue 正文摘录

Attempting to deploy the rocm/vllm container on a DigitalOcean Kubernetes (DOKS) cluster with AMD MI300x GPUs and are encountering a persistent CrashLoopBackOff error. We are currently unable to get application logs due to a platform-level issue, but we have isolated the problem to the vllm serve command itself. Environment: * Platform: DigitalOcean Kubernetes (DOKS) * Kubernetes Version: v1.33.1 * GPU Node: DigitalOcean gpu-mi300x1-192gb-devcloud (AMD MI300x) * Container Image: docker.io/rocm/vllm:latest * Deployment Method: Kubernetes StatefulSet ### 🐛 Describe the bug Problem Description: The container starts, but the vllm serve process exits with a non-zero exit code almost immediately, causing the pod to enter a crash loop. Debugging Steps Taken: We have successfully resolved several preceding infrastructure issues: 1. AMD Device Plugin: The default DOKS GPU node was missing the amd.com/gpu resource. We installed the official AMD Device Plugin DaemonSet and patched it with the necessary toleration (amd.com/gpu:NoSchedule) to get it running. 2. CSI Driver: The node was also missing the DigitalOcean storage driver. We re-installed the dobs-csi-node DaemonSet and patched it with...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: vironment: * Platform: DigitalOcean Kubernetes (DOKS) * Kubernetes Version: v1.33.1 * GPU Node: DigitalOcean gpu-mi300x1-192gb-devcloud (AMD MI300x) * Container Image: docker.io/rocm/vllm:latest * Deployment Method: Kub...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: CrashLoopBackOff on AMD GPU (MI300x) with rocm/vllm Container on DigitalOcean Kubernetes bug;rocm Attempting to deploy the rocm/vllm container on a DigitalOcean Kubernetes (DOKS) cluster with AMD MI300x GPUs and...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: : The crash occurs even with a minimal command: vllm serve Qwen/Qwen3-4B-FP8 --host 0.0.0.0 --port 8000. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatb...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ge: docker.io/rocm/vllm:latest * Deployment Method: Kubernetes StatefulSet ### 🐛 Describe the bug Problem Description: The container starts, but the vllm serve process exits with a non-zero exit code almost immediately,...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: 4. Arguments: The crash occurs even with a minimal command: vllm serve Qwen/Qwen3-4B-FP8 --host 0.0.0.0 --port 8000. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and ask...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
