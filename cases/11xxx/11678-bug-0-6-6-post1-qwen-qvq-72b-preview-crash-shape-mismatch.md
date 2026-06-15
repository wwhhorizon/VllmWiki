# vllm-project/vllm#11678: [Bug]: 0.6.6.post1 Qwen/QVQ-72B-Preview crash: shape mismatch

| 字段 | 值 |
| --- | --- |
| Issue | [#11678](https://github.com/vllm-project/vllm/issues/11678) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support |
| 子分类 | shape_align |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: 0.6.6.post1 Qwen/QVQ-72B-Preview crash: shape mismatch

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - It looks similar to this https://github.com/vllm-project/vllm/issues/10686 - cmd ```bash vllm \ serve \ Qwen/QVQ-72B-Preview \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.9 \ --enable-chunked-prefill \ --enable-prefix-caching \ --host 0.0.0.0 ``` - error ```bash (VllmWorkerProcess pid=8972) ERROR 01-02 15:19:29 multiproc_worker_utils.py:236] Exception in worker VllmWorkerProcess while processing method start_worker_execution_loop. (VllmWorkerProcess pid=8972) ERROR 01-02 15:19:29 multiproc_worker_utils.py:236] Traceback (most recent call last): (VllmWorkerProcess pid=8972) ERROR 01-02 15:19:29 multiproc_worker_utils.py:236] File "/data/miniconda3/envs/llamafactory/lib/python3.11/site-packages/vllm/worker/model_runner_base.py", line 116, in _wrapper (VllmWorkerProcess pid=8972) ERROR 01-02 15:19:29 multiproc_worker_utils.py:236] return func(*args, **kwargs) (VllmWorkerProcess pid=8972) ERROR 01-02 15:19:29 multiproc_worker_utils.py:236] ^^^^^^^^^^^^^^^^^^^^^ (VllmWorkerProcess pid=8972) ERROR 01-02 15:19:29 multiproc_worker_utils.py:236] File "/data/miniconda3/envs/llamafactory/lib/p...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: 0.6.6.post1 Qwen/QVQ-72B-Preview crash: shape mismatch bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - It looks similar to this https://github.com/vllm-project/vllm/i...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. correctness ci_build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;crash;mismatch env_dependency;shape Your current env...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: 0.6.6.post1 Qwen/QVQ-72B-Preview crash: shape mismatch bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - It looks similar to this https://github.com/vllm-project/vllm/i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: _build;distributed_parallel;hardware_porting;model_support cuda;operator;triton build_error;crash;mismatch env_dependency;shape Your current environment
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: [Bug]: 0.6.6.post1 Qwen/QVQ-72B-Preview crash: shape mismatch bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug - It looks similar to this https://github.com/vllm-project/vllm/i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
