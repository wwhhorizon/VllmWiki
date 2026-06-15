# vllm-project/vllm#39341: [Bug]: `max_num_batched_tokens=1` raises unhandled `IndexError`

| 字段 | 值 |
| --- | --- |
| Issue | [#39341](https://github.com/vllm-project/vllm/issues/39341) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
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

> [Bug]: `max_num_batched_tokens=1` raises unhandled `IndexError`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, max_num_batched_tokens=1, ) ``` EngineCore stderr: ``` File ".../vllm/compilation/piecewise_backend.py", line 356, in __call__ runtime_shape = args[self.sym_shape_indices[0]] ~~~~~~~~~~~~~~~~~~~~~~^^^ IndexError: list index out of range ``` ### Expected Add a validity checker at construction time. The backend assumes self.sym_shape_indices has a valid index into args for whatever batch size it's running, but for a single-token batch this is empty/out-of-range. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: current environment ### 🐛 Describe the bug ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, max_num_batched_tokens=1, ) ``` EngineCore stderr: ``` File ".../vllm/compilation/piec...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: s=1, ) ``` EngineCore stderr: ``` File ".../vllm/compilation/piecewise_backend.py", line 356, in __call__ runtime_shape = args[self.sym_shape_indices[0]] ~~~~~~~~~~~~~~~~~~~~~~^^^ IndexError: list index out of range ```...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ge. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 🐛 Describe the bug ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, max_num_batched_tokens=1, ) ``` EngineCore stderr: ``` File ".../vllm/compilation/piecewise_backend.py", line...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: xError` bug ### Your current environment ### 🐛 Describe the bug ### Reproduce ```python import vllm vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, max_num_batched_tokens=1, ) ``` EngineCore stderr: ``` File ".../...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
