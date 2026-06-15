# vllm-project/vllm#41829: [Doc]: scoring.md missing ModernBertForSequenceClassification from supported cross-encoder models

| 字段 | 值 |
| --- | --- |
| Issue | [#41829](https://github.com/vllm-project/vllm/issues/41829) |
| 状态 | closed |
| 标签 | documentation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Doc]: scoring.md missing ModernBertForSequenceClassification from supported cross-encoder models

### Issue 正文摘录

### 📚 The doc issue **Description** The documentation page docs/models/pooling_models/scoring.md is missing [ModernBertForSequenceClassification](vscode-file://vscode-app/d:/InstalledSoftware/Microsoft%20VS%20Code/41dd792b5e/resources/app/out/vs/code/electron-browser/workbench/workbench.html) from the Text-only Cross-encoder Models table under Supported Models > Cross-encoder models. **Evidence** [ModernBertForSequenceClassification] is a fully supported cross-encoder architecture in the vLLM codebase. 1. Implemented in [vllm/model_executor/models/modernbert.py] with [SupportsCrossEncoding]: `class ModernBertForSequenceClassification(nn.Module, SupportsCrossEncoding):` 2. Registered in [_SEQUENCE_CLASSIFICATION_MODELS] in [vllm/model_executor/models/registry.py]: `"ModernBertForSequenceClassification": ( "modernbert", "ModernBertForSequenceClassification", ),` 3. Tested via [test_modernbert_reranker.py]with Alibaba-NLP/gte-reranker-modernbert-base. ### Suggest a potential alternative/fix Add the following row to the Text-only Models table in scoring.md, between [GteNewForSequenceClassification]and [LlamaBidirectionalForSequenceClassification](alphabetical order)。 ### Before submit...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: missing ModernBertForSequenceClassification from supported cross-encoder models documentation ### 📚 The doc issue **Description** The documentation page docs/models/pooling_models/scoring.md is missing [ModernBertForSeq...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: issing [ModernBertForSequenceClassification](vscode-file://vscode-app/d:/InstalledSoftware/Microsoft%20VS%20Code/41dd792b5e/resources/app/out/vs/code/electron-browser/workbench/workbench.html) from the Text-only Cross-e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: [ModernBertForSequenceClassification] is a fully supported cross-encoder architecture in the vLLM codebase. 1. Implemented in [vllm/model_executor/models/modernbert.py] with [SupportsCrossEncoding]: `class ModernBertFor...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ": ( "modernbert", "ModernBertForSequenceClassification", ),` 3. Tested via [test_modernbert_reranker.py]with Alibaba-NLP/gte-reranker-modernbert-base. ### Suggest a potential alternative/fix Add the following row to th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
