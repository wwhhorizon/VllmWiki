# vllm-project/vllm#31501: [Bug]: --stream-interval > 1 causes tool call arguments to be empty/lost

| 字段 | 值 |
| --- | --- |
| Issue | [#31501](https://github.com/vllm-project/vllm/issues/31501) |
| 状态 | open |
| 标签 | stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: --stream-interval > 1 causes tool call arguments to be empty/lost

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `--stream-interval` with a value greater than 1, tool call arguments are lost/truncated to empty `{}` in the SSE streaming output. **Expected behavior:** Tool calls should include their full arguments regardless of stream-interval setting. **Actual behavior:** Tool calls are emitted with `"arguments":"{}"` (empty), causing downstream tool execution to fail with "missing required property" errors. #### Reproduction Server command: ```bash vllm serve lukealonso/MiniMax-M2-NVFP4 \ --stream-interval 20 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --tensor-parallel-size 2 \ --max-model-len 196608 \ --kv-cache-dtype fp8_e4m3 ``` Any request with tool calling will produce SSE chunks like: ```json {"delta":{"tool_calls":[{ "id":"call_671d09eec36e4902bd17e065", "function":{ "arguments":"{}", "name":"filesystem_repos__ListDir" }, "type":"function", "index":0 }]}} ``` The `arguments` field is empty `"{}"` instead of containing the actual arguments like `{"dir": "."}`. #### Evidence from raw SSE capture With `--stream-interval 20`, every tool call has empty arguments: ``` Turn 1: "arguments":"{}" → Validation erro...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: # Reproduction Server command: ```bash vllm serve lukealonso/MiniMax-M2-NVFP4 \ --stream-interval 20 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --tensor-parallel-size 2 \ --max-model-len 196608 \ --kv...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. development attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization cuda build_error dtype;env_dependency Your current environm...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: \ --tool-call-parser minimax_m2 \ --tensor-parallel-size 2 \ --max-model-len 196608 \ --kv-cache-dtype fp8_e4m3 ``` Any request with tool calling will produce SSE chunks like: ```json {"delta":{"tool_calls":[{ "id":"cal...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: --stream-interval > 1 causes tool call arguments to be empty/lost stale ### Your current environment ### 🐛 Describe the bug When using `--stream-interval` with a value greater than 1, tool call arguments are lost...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
