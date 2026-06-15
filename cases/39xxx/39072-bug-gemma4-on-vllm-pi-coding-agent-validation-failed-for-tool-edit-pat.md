# vllm-project/vllm#39072: [Bug]: Gemma4 on vLLM + PI coding agent: Validation failed for tool "edit": - path: must have required property 'path'

| 字段 | 值 |
| --- | --- |
| Issue | [#39072](https://github.com/vllm-project/vllm/issues/39072) |
| 状态 | open |
| 标签 | bug |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;model_support |
| 子分类 | precision |
| Operator 关键词 | operator |
| 症状 | mismatch |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4 on vLLM + PI coding agent: Validation failed for tool "edit": - path: must have required property 'path'

### Issue 正文摘录

### Your current environment Technical Environment: - Model: google/gemma-4-31B-IT - Inference: vLLM (--tool-call-parser gemma4) - Orchestrator: Pi Code Agent - Machine: Nvidia DGX Spark ### 🐛 Describe the bug ### What happened? The Gemma 4 (31B) model, running via vLLM + PI coding agent, is failing to generate valid tool calls for the edit function. While the model successfully provides the edits array (containing oldText and newText), it consistently omits the mandatory path property required by the tool schema. Error Message: Validation failed for tool "edit": - path: must have required property 'path' Root Cause Analysis: The model is generating syntactically correct code diffs but is failing to adhere to the strict JSON schema constraints of the tool definition. This is likely due to a mismatch between the model's output formatting and the vLLM tool parser, or a lack of emphasis on the path parameter in the system instructions. Error ``` Validation failed for tool "edit": - path: must have required property 'path' Received arguments: { "edits": [ { "newText": "<|\"// Supported operators as constants to ensure consistency across lexer, parser, and evaluator.\nconst (\n\tOpAdd...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma4 on vLLM + PI coding agent: Validation failed for tool "edit": - path: must have required property 'path' bug ### Your current environment Technical Environment: - Model: google/gemma-4-31B-IT - Inference:
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 3: JSON schema constraints of the tool definition. This is likely due to a mismatch between the model's output formatting and the vLLM tool parser, or a lack of emphasis on the path parameter in the system instructions. Er...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: \n\t\"abs\": true,\n\t\"floor\": true,\n\t\"ceil\": true,\n}\n\n// Precision settings could be expanded here if rounding were required.\nconst DefaultPrecision = 64<|\"|",
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: SON schema constraints of the tool definition. This is likely due to a mismatch between the model's output formatting and the vLLM tool parser, or a lack of emphasis on the path parameter in the system instructions. Err...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: "apiKey": "dummy", "compat": { "supportsDeveloperRole": false, "supportsReasoningEffort": false }, "models": [ { "id": "google/gemma-4-31B-IT", "contextWindow": 262144 } ] } } } ``` vllm ``` sudo docker run

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
