# vllm-project/vllm#10589: [Bug] Streaming output error of tool calling has still not been resolved.



| 字段 | 值 |
| --- | --- |
| Issue | [#10589](https://github.com/vllm-project/vllm/issues/10589) |
| 状态 | closed |
| 标签 |  |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] Streaming output error of tool calling has still not been resolved.  

### Issue 正文摘录

I used the [hermes_tool_parser.py](https://github.com/vllm-project/vllm/blob/main/vllm/entrypoints/openai/tool_parsers/hermes_tool_parser.py) as `tool-parser-plugin` and registered the parser as `hermes_patched`, but still have the same problem. Already referred to #9874 #10395 #10398 ``` Traceback (most recent call last): File "/app/hermes_tool_parser.py", line 228, in extract_tool_calls_streaming function_name: Union[str, None] = current_tool_call.get("name") ^^^^^^^^^^^^^^^^^^^^^ AttributeError: 'NoneType' object has no attribute 'get' Error trying to handle streaming tool call. Traceback (most recent call last): File "/app/hermes_tool_parser.py", line 292, in extract_tool_calls_streaming args_delta_start_loc = cur_arguments_json.index(delta_text) \ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ValueError: substring not found ``` Here is how I start vllm service with the latest package: ``` python3 -m vllm.entrypoints.openai.api_server \ --model /app/Qwen2.5-72B-Instruct-AWQ \ --port 7415 \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.95 \ --max-model-len 64000 \ --enforce-eager \ --disable_custom_all_reduce \ --enable-auto-tool-choice \ --tool-parser-plugin /app/hermes_tool_pa...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: he latest package: ``` python3 -m vllm.entrypoints.openai.api_server \ --model /app/Qwen2.5-72B-Instruct-AWQ \ --port 7415 \ --tensor-parallel-size 2 \ --gpu-memory-utilization 0.95 \ --max-model-len 64000 \ --enforce-e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: hermes_patched \ --chat-template /app/qwen.jinja ``` I also tried using Docker image `v0.6.3.post1` `v0.6.4` `v0.6.4.post1` _Originally posted by @Sala8888 in https://github.com/vllm-project/vllm/pull/10398#issuecomment...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ror: substring not found ``` Here is how I start vllm service with the latest package: ``` python3 -m vllm.entrypoints.openai.api_server \ --model /app/Qwen2.5-72B-Instruct-AWQ \ --port 7415 \ --tensor-parallel-size 2 \...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
