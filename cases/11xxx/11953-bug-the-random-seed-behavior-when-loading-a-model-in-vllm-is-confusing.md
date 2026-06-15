# vllm-project/vllm#11953: [Bug]: The random seed behavior when loading a model in vLLM is confusing.

| 字段 | 值 |
| --- | --- |
| Issue | [#11953](https://github.com/vllm-project/vllm/issues/11953) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: The random seed behavior when loading a model in vLLM is confusing.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Description When loading a model in vLLM, the `seed` parameter unintentionally affects the global random states (`random`, `np.random`), which can lead to surprising behavior if the user is not explicitly aware of it. Specifically: 1. If the user does not specify the `seed` parameter, its default value (`0`) is used, and the global random states are set accordingly [here](https://github.com/vllm-project/vllm/blob/7a3a83e3b87f50fe9c0985a5c5bcc1d4cf2e95cd/vllm/platforms/interface.py#L190). 2. This means the behavior of random operations in user code outside vLLM becomes unintentionally fixed, which can cause subtle bugs. For example, if the user assumes that random values (e.g., generated with `random.choice` or `np.random.rand`) will vary across runs, they might encounter identical results across multiple script executions. ### Steps to Reproduce Here is a minimal example illustrating the issue: ```python import random from vllm import LLM # Initialize a vLLM model model = LLM(model="Qwen/Qwen2.5-0.5B-Instruct") # Try generating random numbers print(random.randint(0, 100)) # Outputs the same...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: .random`), which can lead to surprising behavior if the user is not explicitly aware of it. Specifically: 1. If the user does not specify the `seed` parameter, its default value (`0`) is used, and the global random stat...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: The random seed behavior when loading a model in vLLM is confusing. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Description When loading a model in vLLM, the `s...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ter identical results across multiple script executions. ### Steps to Reproduce Here is a minimal example illustrating the issue: ```python import random from vllm import LLM # Initialize a vLLM model model = LLM(model=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
