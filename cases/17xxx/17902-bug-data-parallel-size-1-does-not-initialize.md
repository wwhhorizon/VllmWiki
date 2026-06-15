# vllm-project/vllm#17902: [Bug]: --data-parallel-size > 1 does not initialize

| 字段 | 值 |
| --- | --- |
| Issue | [#17902](https://github.com/vllm-project/vllm/issues/17902) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | race_cond |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --data-parallel-size > 1 does not initialize

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using vllm serve --data-parallel-size=N with `N > 8` (8 is the number of GPUs in the node) results in a hang. ``` vllm serve $MODEL --distributed-executor-backend=ray --data-parallel-size=16 --task=embed & ``` running on a ray cluster on two nodes with 16 GPUs.... ``` INFO 05-09 09:03:06 [parallel_state.py:883] Adjusting world_size=16 rank=0 distributed_init_method=tcp://127.0.0.1:29501 for DP Initialized distributed with 16 devices truncating train samples to be a multiple of 128... Tokenizing and embedding... ERROR 05-09 09:13:07 [worker_base.py:620] Error executing method 'init_device'. This might cause deadlock in distributed execution. ERROR 05-09 09:13:07 [worker_base.py:620] Traceback (most recent call last): ERROR 05-09 09:13:07 [worker_base.py:620] File "/mnt/bb/glaser/grpo/lib/python3.12/site-packages/vllm/worker/worker_base.py", line 612, in execute_method ERROR 05-09 09:13:07 [worker_base.py:620] return run_method(self, method, args, kwargs) ERROR 05-09 09:13:07 [worker_base.py:620] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 05-09 09:13:07 [worker_base.py:620] File "/mnt/bb/glaser/grpo/lib/python3.12/site-packages/v...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: [Bug]: --data-parallel-size > 1 does not initialize bug;stale ### Your current environment ### 🐛 Describe the bug Using vllm serve --data-parallel-size=N with `N > 8` (8 is the number of GPUs in the node) results in a h...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: 1/vllm/config.py#L1642 **Possible workaround**: configure data parallelism via environment variables and do not provide `--data-parallel-size` command line argument ### Before submitting a new issue... - [x] Make sure y...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: e node) results in a hang. ``` vllm serve $MODEL --distributed-executor-backend=ray --data-parallel-size=16 --task=embed & ``` running on a ray cluster on two nodes with 16 GPUs.... ``` INFO 05-09 09:03:06 [parallel_sta...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: 8 is the number of GPUs in the node) results in a hang. ``` vllm serve $MODEL --distributed-executor-backend=ray --data-parallel-size=16 --task=embed & ``` running on a ray cluster on two nodes with 16 GPUs.... ``` INFO...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
