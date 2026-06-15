# vllm-project/vllm#8438: [Doc]:  Add Kubernetes (K8s) Deployment Documentation for vLLM with GPUs

| 字段 | 值 |
| --- | --- |
| Issue | [#8438](https://github.com/vllm-project/vllm/issues/8438) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]:  Add Kubernetes (K8s) Deployment Documentation for vLLM with GPUs

### Issue 正文摘录

### 📚 The doc issue ### Context: I am currently managing H100 GPUs using Kubernetes (K8s). However, I’ve noticed that the vLLM documentation only provides deployment instructions for Docker, which is quite different from K8s. This creates a gap for users like me who rely on K8s for managing our infrastructure. ### Issue: Lack of Kubernetes (K8s) deployment documentation for vLLM. Existing documentation focuses solely on Docker, leaving out crucial information for K8s users. The differences between Docker and K8s make it challenging for users to adapt the Docker-based instructions for a K8s environment. ### Proposal: I suggest expanding the current vLLM documentation to include detailed instructions for deploying vLLM in a Kubernetes (K8s) environment. This should cover: Setting up the environment to manage GPUs using K8s. Step-by-step deployment instructions tailored for K8s. Configuration and optimization tips specific to K8s. ### Additional Details: As a K8s user managing H100 GPUs, I am willing to contribute by sharing more details on how to handle these tasks. This could include: Sample YAML files for deployment. Configuration tips and best practices. Troubleshooting common is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ed that the vLLM documentation only provides deployment instructions for Docker, which is quite different from K8s. This creates a gap for users like me who rely on K8s for managing our infrastructure. ### Issue: Lack o...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: documentation ### 📚 The doc issue ### Context: I am currently managing H100 GPUs using Kubernetes (K8s). However, I’ve noticed that the vLLM documentation only provides deployment instructions for Docker, which is quite...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: . Existing documentation focuses solely on Docker, leaving out crucial information for K8s users. The differences between Docker and K8s make it challenging for users to adapt the Docker-based instructions for a K8s env...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
