# vllm-project/vllm#39380: Gemma4 streaming tool call corrupts decimal numbers (X.Y → X.0Y)

| 字段 | 值 |
| --- | --- |
| Issue | [#39380](https://github.com/vllm-project/vllm/issues/39380) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Gemma4 streaming tool call corrupts decimal numbers (X.Y → X.0Y)

### Issue 正文摘录

## Bug Summary Gemma4 streaming tool call arguments corrupt decimal numbers by inserting `0` after the decimal point: `0.45` → `0.045`, `1.1` → `1.01`. Non-streaming works correctly. ## Environment - vLLM: 0.19.1rc1.dev46+gc5e3454e5 (nightly, Apr 6 2026) - Model: google/gemma-4-31B-it (BF16, TP=4) - GPU: 4x RTX A6000 48GB - Server flags: `--enable-auto-tool-choice --tool-call-parser gemma4` ## Reproduction ### Streaming (BROKEN) \`\`\`bash curl -s http://localhost:8000/v1/chat/completions \ -H "Content-Type: application/json" \ -d '{ "model": "gemma4-31b-it", "messages": [{"role": "user", "content": "Values: a=0.45, b=1.1, c=0.92, d=3000. Call the tool with these exact values."}], "tools": [{"type": "function", "function": {"name": "test_numbers", "parameters": {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}, "c": {"type": "number"}, "d": {"type": "number"}}, "required": ["a", "b", "c", "d"]}}}], "temperature": 0.0, "stream": true }' \`\`\` **Expected**: `{"a": 0.45, "b": 1.1, "c": 0.92, "d": 3000}` **Actual**: `{"a": 0.045, "b": 1.01, "c": 0.092, "d": 3000}` ### Non-streaming (CORRECT) Same request with `"stream": false` returns correct values....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Gemma4 streaming tool call corrupts decimal numbers (X.Y → X.0Y) ## Bug Summary Gemma4 streaming tool call arguments corrupt decimal numbers by inserting `0` after the decimal point: `0.45` → `0.045`, `1.1` → `1.01`. No...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Gemma4 streaming tool call corrupts decimal numbers (X.Y → X.0Y) ## Bug Summary Gemma4 streaming tool call arguments corrupt decimal numbers by inserting `0` after the decimal point: `0.45` → `0.045`, `1.1` → `1.01`. No
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 1.dev46+gc5e3454e5 (nightly, Apr 6 2026) - Model: google/gemma-4-31B-it (BF16, TP=4) - GPU: 4x RTX A6000 48GB - Server flags: `--enable-auto-tool-choice --tool-call-parser gemma4` ## Reproduction ### Streaming (BROKEN)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ghtly, Apr 6 2026) - Model: google/gemma-4-31B-it (BF16, TP=4) - GPU: 4x RTX A6000 48GB - Server flags: `--enable-auto-tool-choice --tool-call-parser gemma4` ## Reproduction ### Streaming (BROKEN) \`\`\`bash curl -s htt...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "d": 3000}` ### Non-streaming (CORRECT) Same request with `"stream": false` returns correct values. ## Pattern | Input | Streaming output | Pattern | |-------|-----------------|---------| | 0.45 | 0.045 | 0 inserted aft...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
