# vllm-project/vllm#6807: [Bug][ROCm] The embedding layer does not support long inputs

| 字段 | 值 |
| --- | --- |
| Issue | [#6807](https://github.com/vllm-project/vllm/issues/6807) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm] The embedding layer does not support long inputs

### Issue 正文摘录

### Your current environment 8xMI300x machine using the docker image built with `Dockerfile.rocm`. Versions of relevant libraries: [pip3] mypy==1.7.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [pip3] optree==0.9.1 [pip3] pytorch-triton-rocm==3.0.0+21eae954ef [pip3] torch==2.5.0.dev20240710+rocm6.1 [pip3] torchaudio==2.4.0.dev20240710+rocm6.1 [pip3] torchvision==0.20.0.dev20240710+rocm6.1 [pip3] transformers==4.43.2 [pip3] triton==3.0.0 [conda] No relevant packages ROCM Version: 6.1.40093-bd86f1708 Neuron SDK Version: N/A vLLM Version: 0.5.3.post1 vLLM Build Flags: CUDA Archs: Not Set; ROCm: Disabled; Neuron: Disabled GPU Topology: Could not collect ### 🐛 Describe the bug ```python import torch import torch.nn as nn with torch.inference_mode(): NUM_TOKENS = 128 * 1024 HIDDEN_SIZE = 16 * 1024 VOCAB_SIZE = 128 * 1024 DTYPE = torch.bfloat16 x = torch.randint(VOCAB_SIZE, (NUM_TOKENS,), dtype=torch.int64, device="cuda") embedding = nn.Embedding(VOCAB_SIZE, HIDDEN_SIZE, dtype=DTYPE, device="cuda") y = embedding(x) torch.cuda.synchronize() ``` The above script raises the following error: ``` return torch.embedding(weight, input, padding_idx, scale_grad_by_freq, sparse) RuntimeErro...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: inputs bug;rocm ### Your current environment 8xMI300x machine using the docker image built with `Dockerfile.rocm`. Versions of relevant libraries: [pip3] mypy==1.7.0 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.26.4 [p...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 7: [Bug][ROCm] The embedding layer does not support long inputs bug;rocm ### Your current environment 8xMI300x machine using the docker image built with `Dockerfile.rocm`. Versions of relevant libraries: [pip3] mypy==1.7.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: = 128 * 1024 HIDDEN_SIZE = 16 * 1024 VOCAB_SIZE = 128 * 1024 DTYPE = torch.bfloat16 x = torch.randint(VOCAB_SIZE, (NUM_TOKENS,), dtype=torch.int64, device="cuda") embedding = nn.Embedding(VOCAB_SIZE, HIDDEN_SIZE, dtype=...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: tensions==1.0.0 [pip3] numpy==1.26.4 [pip3] optree==0.9.1 [pip3] pytorch-triton-rocm==3.0.0+21eae954ef [pip3] torch==2.5.0.dev20240710+rocm6.1 [pip3] torchaudio==2.4.0.dev20240710+rocm6.1 [pip3] torchvision==0.20.0.dev2...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ss ci_build;frontend_api;hardware_porting cuda;kernel;triton build_error;mismatch dtype;env_dependency;race_condition Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
