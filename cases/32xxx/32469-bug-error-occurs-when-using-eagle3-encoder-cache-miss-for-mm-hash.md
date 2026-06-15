# vllm-project/vllm#32469: [Bug]: Error occurs when using Eagle3: Encoder cache miss for {mm_hash}

| 字段 | 值 |
| --- | --- |
| Issue | [#32469](https://github.com/vllm-project/vllm/issues/32469) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Error occurs when using Eagle3: Encoder cache miss for {mm_hash}

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using speculative decoding (EAGLE3) together with multimodal (MM) inputs, the model may attempt to access MM encoder cache entries using speculative positions, and hit Encoder cache miss assertions. My model is Qwen2.5-VL-72b and the draft model is trained via SpecForge. This happens even when all requests are processed serially, with no concurrency. And I noticed that thie occurs only when start_pos = num_computed_tokens + num_scheduled_tokens - 1. The detailed tracback shown below: `(Worker_TP1 pid=120245) ERROR 01-16 17:46:35 [multiproc_executor.py:815] WorkerProc hit an exception. (Worker_TP1 pid=120245) ERROR 01-16 17:46:35 [multiproc_executor.py:815] Traceback (most recent call last): (Worker_TP1 pid=120245) ERROR 01-16 17:46:35 [multiproc_executor.py:815] File "/home/disk3/hzh/python-env/python-3.10.12-vllm0.11.2/lib/python3.10/site-packages/vllm/v1/executor/multiproc_executor.py", line 810, in worker_busy_loop (Worker_TP1 pid=120245) ERROR 01-16 17:46:35 [multiproc_executor.py:815] output = func(*args, **kwargs) (Worker_TP1 pid=120245) ERROR 01-16 17:46:35 [multiproc_executor.py:815] File "/home/disk3/hzh/python-env/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Describe the bug When using speculative decoding (EAGLE3) together with multimodal (MM) inputs, the model may attempt to access MM encoder cache entries using speculative positions, and hit Encoder cache miss assertions...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;gemm;operator;trito...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: bug ### Your current environment ### 🐛 Describe the bug When using speculative decoding (EAGLE3) together with multimodal (MM) inputs, the model may attempt to access MM encoder cache entries using speculative positions...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ing;model_support;multimodal_vlm;speculative_decoding cuda;gemm;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
