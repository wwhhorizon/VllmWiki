# vllm-project/vllm#9602: [Usage]: How to use pdb using the latest version? 

| 字段 | 值 |
| --- | --- |
| Issue | [#9602](https://github.com/vllm-project/vllm/issues/9602) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: How to use pdb using the latest version? 

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when I use `pdb.set_trace()` in the latest code, it crashes. How to use pdb in the latest vllm? ``` Process SpawnProcess-1: Traceback (most recent call last): File "/opt/vllm/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) File "/opt/vllm/vllm/worker/model_runner.py", line 1590, in execute_model hidden_or_intermediate_states = model_executable( File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwargs) File "/opt/vllm/vllm/model_executor/models/llama.py", line 479, in forward model_output = self.model(input_ids, positions, kv_caches, File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1553, in _wrapped_call_impl return self._call_impl(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/torch/nn/modules/module.py", line 1562, in _call_impl return forward_call(*args, **kwar...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cess-1: Traceback (most recent call last): File "/opt/vllm/vllm/worker/model_runner_base.py", line 116, in _wrapper return func(*args, **kwargs) File "/opt/vllm/vllm/worker/model_runner.py", line 1590, in execute_model...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: kv_size], dim=-1) File "/usr/lib/python3.10/bdb.py", line 90, in trace_dispatch return self.dispatch_line(frame) File "/usr/lib/python3.10/bdb.py", line 115, in dispatch_line if self.quitting: raise BdbQuit bdb.BdbQuit...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [Usage]: How to use pdb using the latest version? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when I use `pdb.set_trace()` in the latest...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Usage]: How to use pdb using the latest version? usage;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm when I use `pdb.set_trace()` in the latest...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
