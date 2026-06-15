# vllm-project/vllm#26271: [Bug]: Reproducibility of Gemma-3-270m-it output on A10G gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#26271](https://github.com/vllm-project/vllm/issues/26271) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Reproducibility of Gemma-3-270m-it output on A10G gpu

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug import os os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" import torch import random import numpy as np seed = 42 torch.manual_seed(seed) np.random.seed(seed) random.seed(seed) sampling_params=SamplingParams(temperature=0, max_tokens=256,seed=seed) llm = LLM(model='finetuned-model',dtype='auto',max_model_len=4096) outputs = llm.generate(prompts, sampling_params) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Bug]: Reproducibility of Gemma-3-270m-it output on A10G gpu bug;stale ### Your current environment ### 🐛 Describe the bug import os os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" import torch import random import n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Reproducibility of Gemma-3-270m-it output on A10G gpu bug;stale ### Your current environment ### 🐛 Describe the bug import os os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" import torch import random import n...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: max_tokens=256,seed=seed) llm = LLM(model='finetuned-model',dtype='auto',max_model_len=4096) outputs = llm.generate(prompts, sampling_params) ### Before submitting a new issue... - [x] Make sure you already searched for...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ms) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Reproducibility of Gemma-3-270m-it output on A10G gpu bug;stale ### Your current environment ### 🐛 Describe the bug import os os.environ["VLLM_ENABLE_V1_MULTIPROCESSING"] = "0" import torch import random import n...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
