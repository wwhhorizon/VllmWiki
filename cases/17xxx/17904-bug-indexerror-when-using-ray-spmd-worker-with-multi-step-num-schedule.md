# vllm-project/vllm#17904: [Bug]:  IndexError when using Ray-SPMD Worker with Multi-Step (--num-scheduler-steps > 1)

| 字段 | 值 |
| --- | --- |
| Issue | [#17904](https://github.com/vllm-project/vllm/issues/17904) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  IndexError when using Ray-SPMD Worker with Multi-Step (--num-scheduler-steps > 1)

### Issue 正文摘录

### Your current environment ～ ### 🐛 Describe the bug ### Description Running vLLM in **Ray-SPMD Worker** mode (`VLLM_USE_RAY_SPMD_WORKER=1`) together with **Multi-Step scheduling** (`--num-scheduler-steps 8`) crashes with an `IndexError` inside `MultiStepModelRunner.execute_model`. The error occurs while advancing to the next step: `model_input.cached_outputs[-1]` is empty, so accessing `[-1]` raises. ### Reproduction ```bash # single-GPU example; same happens with more GPUs export VLLM_USE_RAY_SPMD_WORKER=1 export VLLM_USE_RAY_COMPILED_DAG =1 python -m vllm.entrypoints.openai.api_server \ --model Qwen2.5-7B-Instruct \ --tensor-parallel-size 1 \ --distributed-executor-backend \ ray \ --num-scheduler-steps 8 ``` Full stack trace (excerpt): ``` self.worker._execute_model_spmd(execute_model_req, File ".../vllm/worker/worker.py", line 399, in _execute_model_spmd output = super()._execute_model_spmd(execute_model_req, File ".../vllm/worker/worker_base.py", line 383, in _execute_model_spmd return self.model_runner.execute_model( File ".../vllm/worker/multi_step_model_runner.py", line 508, in execute_model model_input, model_input.cached_outputs[-1].sampler_output) IndexError: list inde...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: `--num-scheduler-steps 8`) crashes with an `IndexError` inside `MultiStepModelRunner.execute_model`. The error occurs while advancing to the next step: `model_input.cached_outputs[-1]` is empty, so accessing `[-1]` rais...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: side `MultiStepModelRunner.execute_model`. The error occurs while advancing to the next step: `model_input.cached_outputs[-1]` is empty, so accessing `[-1]` raises. ### Reproduction ```bash # single-GPU example; same ha...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: IndexError when using Ray-SPMD Worker with Multi-Step (--num-scheduler-steps > 1) bug;ray;stale ### Your current environment ～ ### 🐛 Describe the bug ### Description Running vLLM in **Ray-SPMD Worker** mode (`VLL...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: n2.5-7B-Instruct \ --tensor-parallel-size 1 \ --distributed-executor-backend \ ray \ --num-scheduler-steps 8 ``` Full stack trace (excerpt): ``` self.worker._execute_model_spmd(execute_model_req, File ".../vllm/worker/w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ul. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
