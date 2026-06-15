# vllm-project/vllm#21307: [Bug]: qwen tool bug

| 字段 | 值 |
| --- | --- |
| Issue | [#21307](https://github.com/vllm-project/vllm/issues/21307) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: qwen tool bug

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug when running `vllm/vllm-openai:v0.9.1` docker image with following args: ``` --model Qwen/Qwen3-235B-A22B-GPTQ-Int4 --api-key xyz --tensor-parallel-size 4 --disable-log-requests --guided-decoding-backend auto --rope-scaling '{"rope_type":"yarn","factor": 4.0, "original_max_position_embeddings": 32768}' --max-model-len 131072 --max_num_batched_tokens 256 --enable-expert-parallel --speculative-config '{"method": "ngram", "num_speculative_tokens": 5, "prompt_lookup_max": 5, "prompt_lookup_min": 1}' --reasoning-parser qwen3 --enable-auto-tool-choice --tool-call-parser hermes ``` tool calls are often truncated, we managed to patch this using very hacky method of adding placeholder field into the tool call and partially parsing json result: ```python properties = { "city": { "type": "string", "description": "The city to find the weather for, e.g. 'San Francisco'", }, "state": { "type": "string", "description": "the two-letter abbreviation for the state that the city is" " in, e.g. 'CA' which would mean 'California'", }, "unit": { "type": "string", "description": "The unit to fetch the temperature in", "enum": ["celsius", "fahrenheit"],...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: qwen tool bug bug;stale ### Your current environment ### 🐛 Describe the bug when running `vllm/vllm-openai:v0.9.1` docker image with following args: ``` --model Qwen/Qwen3-235B-A22B-GPTQ-Int4 --api-key xyz --tenso
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: qwen tool bug bug;stale ### Your current environment ### 🐛 Describe the bug when running `vllm/vllm-openai:v0.9.1` docker image with following args: ``` --model Qwen/Qwen3-235B-A22B-GPTQ-Int4 --api-key xyz --tens...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ey xyz --tensor-parallel-size 4 --disable-log-requests --guided-decoding-backend auto --rope-scaling '{"rope_type":"yarn","factor": 4.0, "original_max_position_embeddings": 32768}' --max-model-len 131072 --max_num_batch...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nment ### 🐛 Describe the bug when running `vllm/vllm-openai:v0.9.1` docker image with following args: ``` --model Qwen/Qwen3-235B-A22B-GPTQ-Int4 --api-key xyz --tensor-parallel-size 4 --disable-log-requests --guided-dec...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ocker image with following args: ``` --model Qwen/Qwen3-235B-A22B-GPTQ-Int4 --api-key xyz --tensor-parallel-size 4 --disable-log-requests --guided-decoding-backend auto --rope-scaling '{"rope_type":"yarn","factor": 4.0,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
