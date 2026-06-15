# vllm-project/vllm#8261: [Bug]: num_scheduler_steps > 1, n > 1 raise error

| 字段 | 值 |
| --- | --- |
| Issue | [#8261](https://github.com/vllm-project/vllm/issues/8261) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: num_scheduler_steps > 1, n > 1 raise error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import EngineArgs, LLMEngine, SamplingParams engine_args = EngineArgs(model="Meta-Llama-3-8B-Instruct", swap_space=8, num_scheduler_steps=8, worker_use_ray=True, gpu_memory_utilization=0.85) vllm_engine = LLMEngine.from_engine_args(engine_args) sampling_params = SamplingParams(n=5, temperature=0.8) vllm_engine.add_request("1", "Are you ok? 1 + 1222 = ?", sampling_params) while vllm_engine.has_unfinished_requests(): out = vllm_engine.step() ``` ```log [rank0]: File "/home/linli/anaconda3/envs/vllm/lib/python3.11/site-packages/vllm/model_executor/layers/sampler.py", line 833, in _sample_with_torch [rank0]: sampled_token_ids_tensor[long_sample_indices] = \ [rank0]: ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^ [rank0]: RuntimeError: shape mismatch: value tensor of shape [5] cannot be broadcast to indexing result of shape [1, 1] ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^ [rank0]: RuntimeError: shape mismatch: value tensor of shape [5] cannot be broadcast to indexing result of shape [1, 1] ``` ### Before submitting a new issue... - [X] Make sure...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m import EngineArgs, LLMEngine, SamplingParams engine_args = EngineArgs(model="Meta-Llama-3-8B-Instruct", swap_space=8, num_scheduler_steps=8, worker_use_ray=True,
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: num_scheduler_steps > 1, n > 1 raise error bug ### Your current environment ### 🐛 Describe the bug ```python from vllm import EngineArgs, LLMEngine, SamplingParams engine_args = EngineArgs(model="Meta-Llama-3-8B-...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^ [rank0]: RuntimeError: shape mismatch: value tensor of shape [5] cannot be broadcast to indexing result of shape [1, 1] ``` ### Before submitting a new issue... - [X] Make sur...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: Your current environment ### 🐛 Describe the bug ```python from vllm import EngineArgs, LLMEngine, SamplingParams engine_args = EngineArgs(model="Meta-Llama-3-8B-Instruct", swap_space=8, num_scheduler_steps=8,

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
