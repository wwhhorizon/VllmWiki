# vllm-project/vllm#4912: [Misc]:pydantic version conflict between vllm openai server and transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#4912](https://github.com/vllm-project/vllm/issues/4912) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Misc]:pydantic version conflict between vllm openai server and transformers

### Issue 正文摘录

### Anything you want to discuss about vllm. vllm==0.4.2 pydantic==2.7.1 transformers==4.40.1 error: RuntimeError: Failed to import transformers.models.clip.modeling_clip because of the following error (look up to see its traceback): Failed to import transformers.generation.utils because of the following error (look up to see its traceback): 'FieldInfo' object has no attribute 'required'

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Misc]:pydantic version conflict between vllm openai server and transformers installation ### Anything you want to discuss about vllm. vllm==0.4.2 pydantic==2.7.1 transformers==4.40.1 error: RuntimeError: Failed to impo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ransformers==4.40.1 error: RuntimeError: Failed to import transformers.models.clip.modeling_clip because of the following error (look up to see its traceback): Failed to import transformers.generation.utils because of t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
