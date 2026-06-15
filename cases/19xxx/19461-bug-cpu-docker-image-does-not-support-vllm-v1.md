# vllm-project/vllm#19461: [Bug]: CPU docker image does not support vLLM v1

| 字段 | 值 |
| --- | --- |
| Issue | [#19461](https://github.com/vllm-project/vllm/issues/19461) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: CPU docker image does not support vLLM v1

### Issue 正文摘录

### Your current environment **Issue Summary** vLLM v1 is not compatible with CPU-only execution, despite the documentation providing instructions for building and running vLLM with a CPU backend. Attempting to run a CPU-only image built via the [official guide](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#pre-built-images) fails with a NotImplementedError when VLLM_USE_V1=1 (which is the default in current versions). ### 🐛 Describe the bug **Steps to Reproduce** Build or pull the vLLM CPU image as described in the [official documentation](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#pre-built-images). Run the container: ``` docker run --model facebook/opt-125m ``` vLLM detects the CPU backend and attempts to initialize v1. The process fails with the following traceback: ``` INFO [__init__.py:243] Automatically detected platform cpu. NotImplementedError: VLLM_USE_V1=1 is not supported with device type=cpu. ``` Full trace below ``` (base) yuhanliu@yuhan-debug:~$ k logs -f vllm-opt125m-deployment-vllm-b5f9fb66d-wxkdb [W611 01:46:45.672078499 OperatorEntry.cpp:154] Warning: Warning only once for all operators, other operators may also b...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: CPU docker image does not support vLLM v1 bug ### Your current environment **Issue Summary** vLLM v1 is not compatible with CPU-only execution, despite the documentation providing instructions for building and ru...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: entation providing instructions for building and running vLLM with a CPU backend. Attempting to run a CPU-only image built via the [official guide](https://docs.vllm.ai/en/stable/getting_started/installation/cpu.html#pr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tion/cpu.html#pre-built-images). Run the container: ``` docker run --model facebook/opt-125m ``` vLLM detects the CPU backend and attempts to initialize v1. The process fails with the following traceback: ``` INFO [__in...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: is the default in current versions). ### 🐛 Describe the bug **Steps to Reproduce** Build or pull the vLLM CPU image as described in the [official documentation](https://docs.vllm.ai/en/stable/getting_started/installatio...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
