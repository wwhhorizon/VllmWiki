# vllm-project/vllm#22132: [Bug]: Qwen3 tool call format possibly being clobbered by guided decoding?

| 字段 | 值 |
| --- | --- |
| Issue | [#22132](https://github.com/vllm-project/vllm/issues/22132) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3 tool call format possibly being clobbered by guided decoding?

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm getting very poor quality responses from the new `Qwen/Qwen3-30B-A3B-Instruct-2507-FP8` when tool calling is enabled. Running via docker compose with args: ``` --model unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --tokenizer unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --max-num-seqs 4 --tool-call-parser hermes --enable-auto-tool-choice --served-model-name model --max-model-len 32648 -tp 2 ``` What I'm noticing is, the model strongly prefers to emit multiple tool calls, even when it does not make sense. I have a suspicion it's because of the `guided_decoding` grammar I am seeing in the vllm request log: ``` guided_decoding=GuidedDecodingParams(json={'type': 'array', 'minItems': 1, 'items': {'type': 'object', 'anyOf': [{'properties': {'name': {'type': 'string', 'enum': ['search_web']}, 'parameters': {'properties': {'query': {'type': 'string'}}, 'required': ['query'], 'type': 'object'}}, 'required': ['name', 'parameters']}, {'properties': {'name': {'type': 'string', 'enum': ['visit_url']}, 'parameters': {'properties': {'url': {'type': 'string'}}, 'required': ['url'], 'type': 'object'}}, 'required': ['name', 'parameters']}, {'properties':...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: n3-30B-A3B-Instruct-2507-FP8` when tool calling is enabled. Running via docker compose with args: ``` --model unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --tokenizer unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --max-num-seqs 4...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Qwen3 tool call format possibly being clobbered by guided decoding? bug;stale ### Your current environment ### 🐛 Describe the bug I'm getting very poor quality responses from the new `Qwen/Qwen3-30B-A3B-Instruct-...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: is enabled. Running via docker compose with args: ``` --model unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --tokenizer unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --max-num-seqs 4 --tool-call-parser hermes --enable-auto-tool-cho...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: Qwen3 tool call format possibly being clobbered by guided decoding? bug;stale ### Your current environment ### 🐛 Describe the bug I'm getting very poor quality responses from the new `Qwen/Qwen3-30B-A3B-Instruct-2507-FP...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ry poor quality responses from the new `Qwen/Qwen3-30B-A3B-Instruct-2507-FP8` when tool calling is enabled. Running via docker compose with args: ``` --model unsloth/Qwen3-30B-A3B-Instruct-2507-FP8 --tokenizer unsloth/Q...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
