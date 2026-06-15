# vllm-project/vllm#7939: [Bug]: Is vllm compatible with torchrun?

| 字段 | 值 |
| --- | --- |
| Issue | [#7939](https://github.com/vllm-project/vllm/issues/7939) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Is vllm compatible with torchrun?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I want to do multi-processing offline inference with each model assigned to 2 GPUs. If there's no vllm, I can do it using `torchrun` with HF models. But when I try to start a `vllm.LLM` in my code, it hangs. I followed [this page](https://docs.vllm.ai/en/latest/getting_started/debugging.html) and set those environment variables. Here is the output ``` INFO 08-28 13:58:51 logger.py:151] Trace frame log is saved to /tmp/vllm/vllm-instance-992d96df3ed145f69a82cd0877a66b1f/VLLM_TRACE_FUNCTION_for_process_17519_thread_140693197510464_at_2024-08-28_13:58:51.235776.log (VllmWorkerProcess pid=17651) WARNING 08-28 13:58:51 logger.py:147] VLLM_TRACE_FUNCTION is enabled. It will record every function executed by Python. This will slow down the code. It is suggested to be used for debugging hang or crashes only. (VllmWorkerProcess pid=17651) INFO 08-28 13:58:51 logger.py:151] Trace frame log is saved to /tmp/vllm/vllm-instance-992d96df3ed145f69a82cd0877a66b1f/VLLM_TRACE_FUNCTION_for_process_17651_thread_140693197510464_at_2024-08-28_13:58:51.235989.log (VllmWorkerProcess pid=17651) INFO 08-28 13:58:52 multiproc_worker_utils.py:215] Worker re...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;crash;slowdown env_dependency Your current environme...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: size=2 rank=0 local_rank=0 distributed_init_method=tcp://127.0.0.1:47579 backend=nccl (VllmWorkerProcess pid=17651) DEBUG 08-28 13:58:52 parallel_state.py:845] world_size=2 rank=1 local_rank=1 distributed_init_method=tc...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: g?) ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cribe the bug I want to do multi-processing offline inference with each model assigned to 2 GPUs. If there's no vllm, I can do it using `torchrun` with HF models. But when I try to start a `vllm.LLM` in my code, it hang...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Is vllm compatible with torchrun? bug;stale ### Your current environment ### 🐛 Describe the bug I want to do multi-processing offline inference with each model assigned to 2 GPUs. If there's no vllm, I can do it...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
