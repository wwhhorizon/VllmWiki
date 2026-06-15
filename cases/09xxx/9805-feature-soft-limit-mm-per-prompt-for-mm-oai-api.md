# vllm-project/vllm#9805: [Feature]: soft limit-mm-per-prompt for MM OAI API

| 字段 | 值 |
| --- | --- |
| Issue | [#9805](https://github.com/vllm-project/vllm/issues/9805) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: soft limit-mm-per-prompt for MM OAI API

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When starting a VLM with `--limit-mm-per-prompt ` and `max_pixels` set, vLLM won't start if the model ctx length exceeds the mm limit * max_pixels token usage. However, this is too precautious and now does not enable me to have 10 small images that easily fit into context length when also wanting to support bigger images. ### Alternatives Remove default limit-mm-per-prompt of 1 and only use existing logic when limit-mm-per-prompt is set ### Additional context ```sh WARNING 10-29 17:42:42 model_runner.py:1247] Computed max_num_seqs (min(256, 32768 // 147456)) to be less than 1. Setting it to the minimum value of 1. Process SpawnProcess-1: Traceback (most recent call last): File "/home/ai/.mconda3/envs/vllm/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap self.run() File "/home/ai/.mconda3/envs/vllm/lib/python3.10/multiprocessing/process.py", line 108, in run self._target(*self._args, **self._kwargs) File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/vllm/engine/multiprocessing/engine.py", line 397, in run_mp_engine engine = MQLLMEngine.from_engine_args(engine_args=engine_args, File "/home/ai/.mconda3/envs/vllm/l...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: e request;stale ### 🚀 The feature, motivation and pitch When starting a VLM with `--limit-mm-per-prompt ` and `max_pixels` set, vLLM won't start if the model ctx length exceeds the mm limit * max_pixels token usage. How...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r.py", line 223, in determine_num_available_blocks self.model_runner.profile_run() File "/home/ai/.mconda3/envs/vllm/lib/python3.10/site-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: . However, this is too precautious and now does not enable me to have 10 small images that easily fit into context length when also wanting to support bigger images. ### Alternatives Remove default limit-mm-per-prompt o...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: soft limit-mm-per-prompt for MM OAI API feature request;stale ### 🚀 The feature, motivation and pitch When starting a VLM with `--limit-mm-per-prompt ` and `max_pixels` set, vLLM won't start if the model ctx...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ntrypoints/openai/api_server.py", line 552, in run_server async with build_async_engine_client(args) as engine_client: File "/home/ai/.mconda3/envs/vllm/lib/python3.10/contextlib.py", line 199, in __aenter__ return awai...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
