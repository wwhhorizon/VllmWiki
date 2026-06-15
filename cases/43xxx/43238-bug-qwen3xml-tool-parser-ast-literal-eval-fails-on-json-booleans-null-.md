# vllm-project/vllm#43238: [Bug]:  qwen3xml_tool_parser: ast.literal_eval fails on JSON booleans/null, causing complex array arguments to be string-encoded instead of native arrays

| 字段 | 值 |
| --- | --- |
| Issue | [#43238](https://github.com/vllm-project/vllm/issues/43238) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:  qwen3xml_tool_parser: ast.literal_eval fails on JSON booleans/null, causing complex array arguments to be string-encoded instead of native arrays

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Description When a tool schema includes an array of objects as a parameter (e.g. questions: array ), the qwen3xml_tool_parser delivers the argument to clients as a JSON-encoded string instead of a native JSON array. Any client that schema-validates tool call arguments receives a type error. The model correctly constructs the array in its reasoning trace — it understands the schema and validates it internally — but the parser fails to convert the value correctly before forwarding to the client. Root Cause In qwen3xml_tool_parser.py, the StreamingXMLToolCallParser._end_element method handles "deferred" parameters (array and object types) by accumulating the raw parameter text and then parsing it at time. The parsing is done with ast.literal_eval: # _end_element, inside `if self.defer_current_parameter:` block parsed_value = ast.literal_eval(raw_for_parse) output_arguments = json.dumps(parsed_value, ensure_ascii=False) ast.literal_eval requires Python literal syntax. Qwen3.6-27B generates standard JSON, which uses lowercase true, false, and null. These are not valid Python literals: >>> import ast >>> ast.literal_eval('[{"multiSelec...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: eval(raw_for_parse) output_arguments = json.dumps(parsed_value, ensure_ascii=False) ast.literal_eval requires Python literal syntax. Qwen3.6-27B generates standard JSON, which uses lowercase true, false, and null. These...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ast.literal_eval raises, the except block runs: except Exception: # Fallback: output as string as-is output_arguments = json.dumps(raw_text, ensure_ascii=False) parsed_value = raw_text json.dumps on a plain string produ...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ectness ci_build;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;fp8;operator;sampling;triton build_error;nan_inf dtype;env_dependency;memory_layout Your cu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: literal_eval: # _end_element, inside `if self.defer_current_parameter:` block parsed_value = ast.literal_eval(raw_for_parse) output_arguments = json.dumps(parsed_value, ensure_ascii=False) ast.literal_eval requires Pyth...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: vLLM with --tool-call-parser qwen3_xml and any Qwen3 model, then send a request with a tool whose schema includes an array-of-objects parameter: curl http://127.0.0.1:8001/v1/chat/completions \ -H "Content-Type: applica...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
