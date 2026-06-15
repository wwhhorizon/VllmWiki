# vllm-project/vllm#12851: [Bug]: Neuron Dockerfile fails to build due to transformers version conflict

| 字段 | 值 |
| --- | --- |
| Issue | [#12851](https://github.com/vllm-project/vllm/issues/12851) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Neuron Dockerfile fails to build due to transformers version conflict

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 1. Clone the repo locally 2. cd into the local repo directory 3. Try to build the Neuron Dockerfile (`docker build -t vllm-neuron . -f Dockerfile.neuron`) Output from the `docker build ...` command with the relevant portion for the failure: ```sh #17 8.799 INFO: pip is looking at multiple versions of transformers-neuronx to determine which version is compatible with other requirements. This could take a while. #17 8.801 Collecting xgrammar>=0.1.6 (from -r /workspace/vllm/requirements-common.txt (line 24)) #17 8.820 Downloading xgrammar-0.1.10-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 8.859 Downloading xgrammar-0.1.9-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 8.904 Downloading xgrammar-0.1.8-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 8.947 Downloading xgrammar-0.1.7-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 8.988 Downloading xgrammar-0.1.6-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 9.010 ERROR: Cannot install -r /workspace/vllm/requireme...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Neuron Dockerfile fails to build due to transformers version conflict bug ### Your current environment ### 🐛 Describe the bug 1. Clone the repo locally 2. cd into the local repo directory 3. Try to build the Neur...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: ammar-0.1.10-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 8.859 Downloading xgrammar-0.1.9-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl.metadata (2.0 kB) #17 8.904 Dow...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: . #17 9.010 #17 9.010 The conflict is caused by: #17 9.010 The user requested transformers>=4.48.2 #17 9.010 compressed-tensors 0.9.1 depends on transformers #17 9.010 xgrammar 0.1.6 depends on transformers #17 9.010 tr...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 023 ERROR: ResolutionImpossible: for help visit https://pip.pypa.io/en/latest/topics/dependency-resolution/#dealing-with-dependency-conflicts #17 ERROR: process "/bin/sh -c python3 -m pip install -U 'cmake>=3.26' ninja...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
