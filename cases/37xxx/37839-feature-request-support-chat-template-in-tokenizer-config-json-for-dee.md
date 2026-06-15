# vllm-project/vllm#37839: [Feature Request] Support chat_template in tokenizer_config.json for DeepSeekV32

| 字段 | 值 |
| --- | --- |
| Issue | [#37839](https://github.com/vllm-project/vllm/issues/37839) |
| 状态 | open |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature Request] Support chat_template in tokenizer_config.json for DeepSeekV32

### Issue 正文摘录

## Feature Request: Support chat_template in tokenizer_config.json for DeepSeekV32 ### Description Currently, the DeepSeekV32 tokenizer's chat template is hardcoded in the `apply_chat_template` method of the `DeepseekV32Tokenizer` class. It would be beneficial to allow users to customize the chat template through the `tokenizer_config.json` file, similar to how other tokenizers work in vLLM. ### Current Behavior The chat template logic is hardcoded in `vllm/tokenizers/deepseek_v32.py`, specifically in the `apply_chat_template` method. Users cannot easily modify the chat template without modifying the source code. ### Expected Behavior Users should be able to define a custom chat template in the `tokenizer_config.json` file using the standard `chat_template` field, and the DeepSeekV32 tokenizer should respect this configuration. ### Use Case - Users may want to customize the chat template for specific use cases - Different DeepSeekV32 models might require slightly different template formats - Consistency with other tokenizers that already support chat_template configuration ### Proposed Solution 1. Modify the `DeepseekV32Tokenizer` class to check for a `chat_template` field in the...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature Request] Support chat_template in tokenizer_config.json for DeepSeekV32 ## Feature Request: Support chat_template in tokenizer_config.json for DeepSeekV32 ### Description Currently, the DeepSeekV32 tokenizer's...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _template` method of the `DeepseekV32Tokenizer` class. It would be beneficial to allow users to customize the chat template through the `tokenizer_config.json` file, similar to how other tokenizers work in vLLM. ### Cur...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Feature Request] Support chat_template in tokenizer_config.json for DeepSeekV32 ## Feature Request: Support chat_template in tokenizer_config.json for DeepSeekV32 ### Description Currently, the DeepSeekV32 tokenizer's...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
