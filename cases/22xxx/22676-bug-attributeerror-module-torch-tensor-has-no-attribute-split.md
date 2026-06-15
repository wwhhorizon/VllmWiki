# vllm-project/vllm#22676: [Bug]: AttributeError: module 'torch._tensor' has no attribute 'split'

| 字段 | 值 |
| --- | --- |
| Issue | [#22676](https://github.com/vllm-project/vllm/issues/22676) |
| 状态 | closed |
| 标签 | bug;torch.compile;needs reproduction |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: AttributeError: module 'torch._tensor' has no attribute 'split'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug conda create --name LLM python=3.11 --yes conda activate LLM conda install nvidia/label/cuda-12.6.0::cuda --yes conda env config vars set CUDA_HOME=$CONDA_PREFIX conda deactivate conda activate LLM pip install "torch<2.8" torchvision --index-url https://download.pytorch.org/whl/cu126 pip install datasets matplotlib accelerate wandb vllm Issue reproduced with above steps. VLLM unable to initialize with meta-llama/Llama-3.1-8b-Instruct, engine core initialization failed with above merror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ttributeError: module 'torch._tensor' has no attribute 'split' bug;torch.compile;needs reproduction ### Your current environment ### 🐛 Describe the bug conda create --name LLM python=3.11 --yes conda activate LLM conda...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ctivate LLM conda install nvidia/label/cuda-12.6.0::cuda --yes conda env config vars set CUDA_HOME=$CONDA_PREFIX conda deactivate conda activate LLM pip install "torch<2.8" torchvision --index-url https://download.pytor...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: name LLM python=3.11 --yes conda activate LLM conda install nvidia/label/cuda-12.6.0::cuda --yes conda env config vars set CUDA_HOME=$CONDA_PREFIX conda deactivate conda activate LLM pip install "torch<2.8" torchvision...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: g/whl/cu126 pip install datasets matplotlib accelerate wandb vllm Issue reproduced with above steps. VLLM unable to initialize with meta-llama/Llama-3.1-8b-Instruct, engine core initialization failed with above merror #...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
