# vllm-project/vllm#16502: [Feature]: SBSA GH200

| 字段 | 值 |
| --- | --- |
| Issue | [#16502](https://github.com/vllm-project/vllm/issues/16502) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: SBSA GH200

### Issue 正文摘录

### 🚀 The feature, motivation and pitch `` Building vLLM with aarch64 and CUDA (GH200), where the PyTorch wheels are not available on PyPI. Currently, only the PyTorch nightly has wheels for aarch64 with CUDA. You can run pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu124 to install PyTorch nightly, and then build vLLM on top of it. `` PYTORCH: PIP Linux CUDA 12.8 Aarch64 ```bash pip3 install torch==2.7.0 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/test/cu128 ``` NVIDIA: https://pypi.jetson-ai-lab.dev/sbsa/cu128 ### Alternatives _No response_ ### Additional context _No response_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: : SBSA GH200 feature request ### 🚀 The feature, motivation and pitch `` Building vLLM with aarch64 and CUDA (GH200), where the PyTorch wheels are not available on PyPI. Currently, only the PyTorch nightly has wheels for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: request ### 🚀 The feature, motivation and pitch `` Building vLLM with aarch64 and CUDA (GH200), where the PyTorch wheels are not available on PyPI. Currently, only the PyTorch nightly has wheels for aarch64 with CUDA. Y...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature]: SBSA GH200 feature request ### 🚀 The feature, motivation and pitch `` Building vLLM with aarch64 and CUDA (GH200), where the PyTorch wheels are not available on PyPI. Currently, only the PyTorch nightly has w...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: orchvision torchaudio --extra-index-url https://download.pytorch.org/whl/test/cu128 ``` NVIDIA: https://pypi.jetson-ai-lab.dev/sbsa/cu128 ### Alternatives _No response_ ### Additional context _No response_ ### Before su...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
