# vllm-project/vllm#44154: BUG: ValueError (not enough values to unpack) when logits processor FQCN is missing ':' separator

| 字段 | 值 |
| --- | --- |
| Issue | [#44154](https://github.com/vllm-project/vllm/issues/44154) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> BUG: ValueError (not enough values to unpack) when logits processor FQCN is missing ':' separator

### Issue 正文摘录

## What breaks When a user passes a logits processor as a string FQCN (fully-qualified class name) that is missing the required colon separator — for example \`\"mymodule.MyCustomLogitsProcessor\"\` instead of \`\"mymodule:MyCustomLogitsProcessor\"\` — \`_load_logitsprocs_by_fqcns\` in \`vllm/v1/sample/logits_processor/__init__.py\` crashes with a confusing Python unpack error rather than a user-friendly message. ## Trigger Pass any string without \`:\` to \`logits_processors\` in \`LLM\` or via the API, e.g.: \`\`\`python llm = LLM(model="...", logits_processors=["mymodule.MyCustomLogitsProcessor"]) \`\`\` ## Traceback \`\`\` File "vllm/v1/sample/logits_processor/__init__.py", line 128, in _load_logitsprocs_by_fqcns module_path, qualname = logitproc.split(":") ^^^^^^^^^^^^^^^^^^^^^ ValueError: not enough values to unpack (expected 2, got 1) \`\`\` ## Root cause Line 128 does \`logitproc.split(":")\` with no guard for the case where the string contains no colon. The docstring documents the required \` : \` syntax but the code performs no validation before the unpack. ## Expected behavior A clear \`ValueError\` explaining the required format, e.g. \`"Logits processor FQCN 'mymodule...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ts_processors\` in \`LLM\` or via the API, e.g.: \`\`\`python llm = LLM(model="...", logits_processors=["mymodule.MyCustomLogitsProcessor"]) \`\`\` ## Traceback \`\`\` File "vllm/v1/sample/logits_processor/__init__.py",...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
