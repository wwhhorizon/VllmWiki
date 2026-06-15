# vllm-project/vllm#13405: [Bug]: is_async_output_supported     raise NotImplementedError

| 字段 | 值 |
| --- | --- |
| Issue | [#13405](https://github.com/vllm-project/vllm/issues/13405) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: is_async_output_supported     raise NotImplementedError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug vllm=0.7.2，transformers=4.49.0.dev0，model=Qwen2.5-VL-7B，use vllm load Qwen2.5-VL-7B and inference , then raise the error: Traceback (most recent call last): File "/mnt/public02/usr/yinzheng/llmforlowbadmarketing/llms/Qwen/vllm_infer.py", line 152, in fire.Fire(vllm_infer) File "/usr/local/lib/python3.10/dist-packages/fire/core.py", line 135, in Fire component_trace = _Fire(component, args, parsed_flag_args, context, name) File "/usr/local/lib/python3.10/dist-packages/fire/core.py", line 468, in _Fire component, remaining_args = _CallAndUpdateTrace( File "/usr/local/lib/python3.10/dist-packages/fire/core.py", line 684, in _CallAndUpdateTrace component = fn(*varargs, **kwargs) File "/mnt/public02/usr/yinzheng/llmforlowbadmarketing/llms/Qwen/vllm_infer.py", line 140, in vllm_infer results = LLM(**engine_args).generate(inputs, sampling_params, lora_request=lora_request) File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1051, in inner return fn(*args, **kwargs) File "/usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py", line 242, in __init__ self.llm_engine = self.engine_class.from_engine_args( File "/usr/...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ironment ### 🐛 Describe the bug vllm=0.7.2，transformers=4.49.0.dev0，model=Qwen2.5-VL-7B，use vllm load Qwen2.5-VL-7B and inference , then raise the error: Traceback (most recent call last): File "/mnt/public02/usr/yinzhe...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ror ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: results = LLM(**engine_args).generate(inputs, sampling_params, lora_request=lora_request) File "/usr/local/lib/python3.10/dist-packages/vllm/utils.py", line 1051, in inner return fn(*args, **kwargs) File "/usr/local/lib...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
