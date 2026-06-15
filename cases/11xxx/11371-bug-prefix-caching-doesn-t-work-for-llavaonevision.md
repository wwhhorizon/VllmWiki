# vllm-project/vllm#11371: [Bug]: Prefix caching doesn't work for LlavaOneVision

| 字段 | 值 |
| --- | --- |
| Issue | [#11371](https://github.com/vllm-project/vllm/issues/11371) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Prefix caching doesn't work for LlavaOneVision

### Issue 正文摘录

### Your current environment The generated dummy input is video, but the preprocessor tries to get image from the dict, and then it crashes. After I walk around this, the code still fails to run. It complains this: ``` File "/data/test/prefix-caching-vlm/vllm/vllm/v1/engine/core.py", line 264, in run_engine_core engine_core.run_busy_loop() File "/data/test/prefix-caching-vlm/vllm/vllm/v1/engine/core.py", line 302, in run_busy_loop outputs = self.step() File "/data/test/prefix-caching-vlm/vllm/vllm/v1/engine/core.py", line 125, in step output = self.model_executor.execute_model(scheduler_output) File "/data/test/prefix-caching-vlm/vllm/vllm/v1/executor/uniproc_executor.py", line 72, in execute_model output = self.worker.execute_model(scheduler_output) File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) File "/data/test/prefix-caching-vlm/vllm/vllm/v1/worker/gpu_worker.py", line 203, in execute_model output = self.model_runner.execute_model(scheduler_output) File "/usr/local/lib/python3.10/dist-packages/torch/utils/_contextlib.py", line 116, in decorate_context return func(*args, **kwargs) File "/data/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ails to run. It complains this: ``` File "/data/test/prefix-caching-vlm/vllm/vllm/v1/engine/core.py", line 264, in run_engine_core engine_core.run_busy_loop() File "/data/test/prefix-caching-vlm/vllm/vllm/v1/engine/core...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Prefix caching doesn't work for LlavaOneVision bug;stale ### Your current environment The generated dummy input is video, but the preprocessor tries to get image from the dict, and then it crashes. After I walk a...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: is, the code still fails to run. It complains this: ``` File "/data/test/prefix-caching-vlm/vllm/vllm/v1/engine/core.py", line 264, in run_engine_core engine_core.run_busy_loop() File "/data/test/prefix-caching-vlm/vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
