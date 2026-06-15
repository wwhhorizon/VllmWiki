# vllm-project/vllm#11615: [Installation]: Hitting issues while trying to build vllm image using Dockerfile.rocm (v0.6.2)

| 字段 | 值 |
| --- | --- |
| Issue | [#11615](https://github.com/vllm-project/vllm/issues/11615) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: Hitting issues while trying to build vllm image using Dockerfile.rocm (v0.6.2)

### Issue 正文摘录

### Your current environment Running docker build on ubuntu server. Facing following error: ![image](https://github.com/user-attachments/assets/12e75246-2c48-4751-9484-d0182cceff50) I checked https://download.pytorch.org/whl/nightly/torch/ But required wheel file: torch==2.6.0.dev20240918 and torchvision==0.20.0.dev20240918 is not present. ### How you are installing vllm docker build -f Dockerfile.rocm -t vllm-rocm:0.6.2 . ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Installation]: Hitting issues while trying to build vllm image using Dockerfile.rocm (v0.6.2) installation ### Your current environment Running docker build on ubuntu server. Facing following error: ![image](https://gi
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ation]: Hitting issues while trying to build vllm image using Dockerfile.rocm (v0.6.2) installation ### Your current environment Running docker build on ubuntu server. Facing following error: ![image](https://github.com...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
