# vllm-project/vllm#32674: [Feature][P1]: Add OCI Annotations to container images

| 字段 | 值 |
| --- | --- |
| Issue | [#32674](https://github.com/vllm-project/vllm/issues/32674) |
| 状态 | open |
| 标签 | feature request;keep-open |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature][P1]: Add OCI Annotations to container images

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Currently vllm images use the vanilla labels from NVIDIA base images: ``` {"maintainer":"NVIDIA CORPORATION ","org.opencontainers.image.ref.name":"ubuntu","org.opencontainers.image.version":"22.04"} ``` We should add more [OCI annotations](https://specs.opencontainers.org/image-spec/annotations/) to the images as metadata. For example, the project name, version / commit hash used to build, and more. And we should override the maintainer name. There is some similar work in #30593: https://github.com/vllm-project/vllm/pull/30953/changes#diff-d4fc32feaf69e41815eaa8608a1687525d03888f9dc68d35c2ac96453cf6028eR217-R239. We should do it in a unified and consistent way. ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Feature][P1]: Add OCI Annotations to container images feature request;keep-open ### 🚀 The feature, motivation and pitch Currently vllm images use the vanilla labels from NVIDIA base images: ``` {"maintainer":"NVIDIA CO...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: tps://specs.opencontainers.org/image-spec/annotations/) to the images as metadata. For example, the project name, version / commit hash used to build, and more. And we should override the maintainer name. There is some...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature][P1]: Add OCI Annotations to container images feature request;keep-open ### 🚀 The feature, motivation and pitch Currently vllm images use the vanilla labels from NVIDIA base images: ``` {"maintainer":"NVIDIA CO...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
