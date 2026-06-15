# vllm-project/vllm#20991: [Bug]: Hermes tool call parser: pops empty list

| 字段 | 值 |
| --- | --- |
| Issue | [#20991](https://github.com/vllm-project/vllm/issues/20991) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Hermes tool call parser: pops empty list

### Issue 正文摘录

### Your current environment 4xH100-80GiB CLI Args: ``` # Inference - --model - Qwen/Qwen3-235B-A22B-FP8 - --gpu-memory-utilization - "0.90" - --disable-custom-all-reduce - --rope-scaling.rope_type - "yarn" - --rope-scaling.factor - 4 - --rope-scaling.original_max_position_embeddings - 32768 - --max-model-len - "131072" - --tensor-parallel-size - "4" # Function calling - --enable-auto-tool-choice - --tool-call-parser - hermes # Server - --host - "0.0.0.0" - --disable-log-requests ``` ### 🐛 Describe the bug Pops from an empty list in the Hermes tool call parser. ``` IndexError: pop from empty list File "/usr/local/lib/python3.12/dist-packages/partial_json_parser/core/myelin.py", line 50, in fix_fast _i, _char = stack.pop() File "/usr/local/lib/python3.12/dist-packages/partial_json_parser/core/api.py", line 22, in ensure_json head, tail = fix_fast(json_string, allow_partial) File "/usr/local/lib/python3.12/dist-packages/partial_json_parser/core/api.py", line 15, in parse_json return parser(ensure_json(json_string, allow_partial, use_fast_fix)) File "/usr/local/lib/python3.12/dist-packages/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py", line 241, in extract_tool_calls cu...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: l call parser: pops empty list bug;stale ### Your current environment 4xH100-80GiB CLI Args: ``` # Inference - --model - Qwen/Qwen3-235B-A22B-FP8 - --gpu-memory-utilization - "0.90" - --disable-custom-all-reduce - --rop...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: environment 4xH100-80GiB CLI Args: ``` # Inference - --model - Qwen/Qwen3-235B-A22B-FP8 - --gpu-memory-utilization - "0.90" - --disable-custom-all-reduce - --rope-scaling.rope_type - "yarn" - --rope-scaling.factor
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Hermes tool call parser: pops empty list bug;stale ### Your current environment 4xH100-80GiB CLI Args: ``` # Inference - --model - Qwen/Qwen3-235B-A22B-FP8 - --gpu-memory-utilization - "0.90" - --disable-custom-a...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ``` # Inference - --model - Qwen/Qwen3-235B-A22B-FP8 - --gpu-memory-utilization - "0.90" - --disable-custom-all-reduce - --rope-scaling.rope_type - "yarn" - --rope-scaling.factor - 4 - --rope-scaling.orig
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
