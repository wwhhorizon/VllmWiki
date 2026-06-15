# vllm-project/vllm#23681: [Doc]: clarify support for cpu-based image

| 字段 | 值 |
| --- | --- |
| Issue | [#23681](https://github.com/vllm-project/vllm/issues/23681) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: clarify support for cpu-based image

### Issue 正文摘录

### 📚 The doc issue Goal: _As a vllm user, I want to trust that the vllm team supports the images I'm using in my projects' small CI jobs, so that I do not use untrusted/unmaintained vllm images._ vllm's [CPU-based docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#pre-built-images) instruct users to pull from this URL: ``` gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-repo ``` This is different than the main `vllm-openai` image: ``` docker.io/vllm/vllm-openai:latest ``` It's unclear if users and other projects ought to pull directly from "q9t5s3a7" or if that is something that users should trust. From [previous discussions](https://github.com/vllm-project/vllm/issues/14756), it sounds like something (buildkite?) pushes images to this ECR location automatically, and then something else moves images from ECR to the official Docker Hub location? ### Suggest a potential alternative/fix Suggestion: 1. Can we have an official CPU-based image at https://hub.docker.com/r/vllm/ ? 2. If we do not host the CPU-based image in the `vllm` Docker Hub namespace, please at least update the docs to explain why users should trust this ECR location. ### Before submitting a new is...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: t that the vllm team supports the images I'm using in my projects' small CI jobs, so that I do not use untrusted/unmaintained vllm images._ vllm's [CPU-based docs](https://docs.vllm.ai/en/latest/getting_started/installa...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: o trust that the vllm team supports the images I'm using in my projects' small CI jobs, so that I do not use untrusted/unmaintained vllm images._ vllm's [CPU-based docs](https://docs.vllm.ai/en/latest/getting_started/in...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ?) pushes images to this ECR location automatically, and then something else moves images from ECR to the official Docker Hub location? ### Suggest a potential alternative/fix Suggestion: 1. Can we have an official CPU-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ntained vllm images._ vllm's [CPU-based docs](https://docs.vllm.ai/en/latest/getting_started/installation/cpu.html#pre-built-images) instruct users to pull from this URL: ``` gallery.ecr.aws/q9t5s3a7/vllm-cpu-release-re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
