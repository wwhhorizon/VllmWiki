# vllm-project/vllm#26161: [Bug]: pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig

| 字段 | 值 |
| --- | --- |
| Issue | [#26161](https://github.com/vllm-project/vllm/issues/26161) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 19; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig

### Issue 正文摘录

### Your current environment ``` vllm/engine/arg_utils.py", line 963, in create_model_config return ModelConfig( ^^^^^^^^^^^^ File "/root/miniconda3/lib/python3.12/site-packages/pydantic/_internal/_dataclasses.py", line 127, in __init__ s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance=s) pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig Value error, Expecting value: line 1 column 1 (char 0) [type=value_error, input_value=ArgsKwargs((), {'model': ...rocessor_plugin': None}), input_type=ArgsKwargs] For further information visit https://errors.pydantic.dev/2.12/v/value_error ``` ### 🐛 Describe the bug vllm serve /data/models/MiniCPM-V-4_5/ --dtype auto --max-model-len 4096 --api-key token-abc123 --gpu_memory_utilization 0.9 --trust-remote-code --limit-mm-per-prompt '{"video": 3}' can not running latest model with vllm 0.10.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: g]: pydantic_core._pydantic_core.ValidationError: 1 validation error for ModelConfig bug;stale ### Your current environment ``` vllm/engine/arg_utils.py", line 963, in create_model_config return ModelConfig( ^^^^^^^^^^^...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: or ``` ### 🐛 Describe the bug vllm serve /data/models/MiniCPM-V-4_5/ --dtype auto --max-model-len 4096 --api-key token-abc123 --gpu_memory_utilization 0.9 --trust-remote-code --limit-mm-per-prompt '{"video": 3}' can not...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: e._pydantic_core.ValidationError: 1 validation error for ModelConfig bug;stale ### Your current environment ``` vllm/engine/arg_utils.py", line 963, in create_model_config return ModelConfig( ^^^^^^^^^^^^ File "/root/mi...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: rust-remote-code --limit-mm-per-prompt '{"video": 3}' can not running latest model with vllm 0.10.2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot li...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
