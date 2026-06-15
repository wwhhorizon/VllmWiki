# vllm-project/vllm#20209: [Bug]: When enable speculative decoding, sleep cannot work

| 字段 | 值 |
| --- | --- |
| Issue | [#20209](https://github.com/vllm-project/vllm/issues/20209) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: When enable speculative decoding, sleep cannot work

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi, when I try to implement speculative decoding in verl, I find that .sleep(leve=1) cannot work. [rank0]: Traceback (most recent call last): [rank0]: File "/scratch/yh5961/RL-Spec/verl/verl/workers/rollout/vllm_rollout/SD.py", line 19, in [rank0]: llm.sleep(level=1) [rank0]: File "/scratch/yh5961/pyenv/verl/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 1322, in sleep [rank0]: self.llm_engine.sleep(level=level) [rank0]: File "/scratch/yh5961/pyenv/verl/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 1860, in sleep [rank0]: self.model_executor.sleep(level=level) [rank0]: File "/scratch/yh5961/pyenv/verl/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 207, in sleep [rank0]: self.collective_rpc("sleep", kwargs=dict(level=level)) [rank0]: File "/scratch/yh5961/pyenv/verl/lib/python3.10/site-packages/vllm/executor/uniproc_executor.py", line 57, in collective_rpc [rank0]: answer = run_method(self.driver_worker, method, args, kwargs) [rank0]: File "/scratch/yh5961/pyenv/verl/lib/python3.10/site-packages/vllm/utils.py", line 2667, in run_method [rank0]: raise NotImplementedError(f"Method {me...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: When enable speculative decoding, sleep cannot work bug;stale ### Your current environment ### 🐛 Describe the bug Hi, when I try to implement speculative decoding in verl, I find that .sleep(leve=1) cannot work....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ()) ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ckages/vllm/engine/llm_engine.py", line 1860, in sleep [rank0]: self.model_executor.sleep(level=level) [rank0]: File "/scratch/yh5961/pyenv/verl/lib/python3.10/site-packages/vllm/executor/executor_base.py", line 207, in...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
