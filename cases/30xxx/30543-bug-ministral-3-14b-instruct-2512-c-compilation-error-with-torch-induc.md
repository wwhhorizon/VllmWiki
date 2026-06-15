# vllm-project/vllm#30543: [Bug]: Ministral-3-14B-Instruct-2512 C++ Compilation Error with Torch Inductor and Batch Generation Failure with enforce_eager=False

| 字段 | 值 |
| --- | --- |
| Issue | [#30543](https://github.com/vllm-project/vllm/issues/30543) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Ministral-3-14B-Instruct-2512 C++ Compilation Error with Torch Inductor and Batch Generation Failure with enforce_eager=False

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Bug 1: C++ Compilation Error with Torch Inductor Description After upgrading from vLLM 0.11.0 (torch 2.8.0) to vLLM 0.12.0 (torch 2.9.0), the model fails to run with a C++ compilation error from torch inductor. Error Message ``` cc1plus: error: CPU you selected does not support x86-64 instruction set cc1plus: error: '-fcf-protection=full' is not supported for this target ``` Root Cause The error occurs during torch dynamo compilation when using: - tensor_parallel_size > 1 - logprobs in SamplingParams Reproduction Code ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_dir = "/path/to/Ministral-3-14B-Instruct-2512" msgs = [ # {"role": "system", "content": " "}, {"role": "system", "content": """You are solving a Sodoku puzzle.\nFill in the empty cells (marked with _) with numbers 1-9 such that:\n1. Each row contains all numbers 1-9 exactly once\n2. Each column contains all numbers 1-9 exactly once\n3. Each 3x3 subgrid contains all numbers 1-9 exactly once\n4. The grid is 0-indexed (i.e., the top-left cell is (0,0), the bottom-right cell is (8,8))\nYou need to complete the task within 30 step...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: e > 1 - logprobs in SamplingParams Reproduction Code ```python from vllm import LLM, SamplingParams from transformers import AutoTokenizer model_dir = "/path/to/Ministral-3-14B-Instruct-2512" msgs = [ # {"role": "system...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: grading from vLLM 0.11.0 (torch 2.8.0) to vLLM 0.12.0 (torch 2.9.0), the model fails to run with a C++ compilation error from torch inductor. Error Message ``` cc1plus: error: CPU you selected does not support x86-64 in...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Torch Inductor and Batch Generation Failure with enforce_eager=False bug;stale ### Your current environment ### 🐛 Describe the bug Bug 1: C++ Compilation Error with Torch Inductor Description After upgrading from vLLM 0...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
