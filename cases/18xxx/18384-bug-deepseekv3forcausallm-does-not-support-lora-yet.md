# vllm-project/vllm#18384: [Bug]: DeepseekV3ForCausalLM does not support LoRA yet

| 字段 | 值 |
| --- | --- |
| Issue | [#18384](https://github.com/vllm-project/vllm/issues/18384) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: DeepseekV3ForCausalLM does not support LoRA yet

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug [rank0]: Traceback (most recent call last): [rank0]: File "/lustre/grp/wxqlab/hongb/code/deepseek/LLaMA-Factory/scripts/vllm_infer.py", line 326, in [rank0]: fire.Fire(vllm_infer) [rank0]: File "/lustre/grp/wxqlab/hongb/miniconda3/envs/deepseek_sc_llamafactory/lib/python3.11/site-packages/fire/core.py", line 135, in Fire [rank0]: component_trace = _Fire(component, args, parsed_flag_args, context, name) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/lustre/grp/wxqlab/hongb/miniconda3/envs/deepseek_sc_llamafactory/lib/python3.11/site-packages/fire/core.py", line 468, in _Fire [rank0]: component, remaining_args = _CallAndUpdateTrace( [rank0]: ^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/lustre/grp/wxqlab/hongb/miniconda3/envs/deepseek_sc_llamafactory/lib/python3.11/site-packages/fire/core.py", line 684, in _CallAndUpdateTrace [rank0]: component = fn(*varargs, **kwargs) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^ [rank0]: File "/lustre/grp/wxqlab/hongb/code/deepseek/LLaMA-Factory/scripts/vllm_infer.py", line 300, in vllm_infer [rank0]: results = asyncio.run(async_generate_parallel(engine_args, inputs, sampling_params, l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: cent call last): [rank0]: File "/lustre/grp/wxqlab/hongb/code/deepseek/LLaMA-Factory/scripts/vllm_infer.py", line 326, in [rank0]: fire.Fire(vllm_infer) [rank0]: File "/lustre/grp/wxqlab/hongb/miniconda3/envs/deepseek_s...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: DeepseekV3ForCausalLM does not support LoRA yet bug;stale ### Your current environment ### 🐛 Describe the bug [rank0]: Traceback (most recent call last): [rank0]: File "/lustre/grp/wxqlab/hongb/code/deepseek/LLaM...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ripts/vllm_infer.py", line 300, in vllm_infer [rank0]: results = asyncio.run(async_generate_parallel(engine_args, inputs, sampling_params, lora_request=lora_request)) [rank0]: ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: it? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
