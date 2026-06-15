# vllm-project/vllm#6932: [Feature Request]: Support INT4 for MiniCPM-Llama3-V-2_5

| 字段 | 值 |
| --- | --- |
| Issue | [#6932](https://github.com/vllm-project/vllm/issues/6932) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request]: Support INT4 for MiniCPM-Llama3-V-2_5

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ```python [rank0]: Traceback (most recent call last): [rank0]: File "/home/work/minicpm_test/minicpm_vllm.py", line 9, in [rank0]: llm = LLM( [rank0]: File "/home/work/vllm-main/vllm/entrypoints/llm.py", line 155, in __init__ [rank0]: self.llm_engine = LLMEngine.from_engine_args( [rank0]: File "/home/work/vllm-main/vllm/engine/llm_engine.py", line 441, in from_engine_args [rank0]: engine = cls( [rank0]: File "/home/work/vllm-main/vllm/engine/llm_engine.py", line 251, in __init__ [rank0]: self.model_executor = executor_class( [rank0]: File "/home/work/vllm-main/vllm/executor/executor_base.py", line 47, in __init__ [rank0]: self._init_executor() [rank0]: File "/home/work/vllm-main/vllm/executor/gpu_executor.py", line 36, in _init_executor [rank0]: self.driver_worker.load_model() [rank0]: File "/home/work/vllm-main/vllm/worker/worker.py", line 139, in load_model [rank0]: self.model_runner.load_model() [rank0]: File "/home/work/vllm-main/vllm/worker/model_runner.py", line 722, in load_model [rank0]: self.model = get_model(model_config=self.model_config, [rank0]: File "/home/work/vllm-...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature Request]: Support INT4 for MiniCPM-Llama3-V-2_5 feature request ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ```python [rank0]: Traceback (most recent ca...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: [Feature Request]: Support INT4 for MiniCPM-Llama3-V-2_5 feature request ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ```python [rank0]: Traceback (most recent ca...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature Request]: Support INT4 for MiniCPM-Llama3-V-2_5 feature request ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug ```python [rank0]: Traceback (most recent ca...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: : Traceback (most recent call last): [rank0]: File "/home/work/minicpm_test/minicpm_vllm.py", line 9, in [rank0]: llm = LLM( [rank0]: File "/home/work/vllm-main/vllm/entrypoints/llm.py", line 155, in __init__ [rank0]: s...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
