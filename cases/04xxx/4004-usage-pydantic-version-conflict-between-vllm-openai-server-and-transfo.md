# vllm-project/vllm#4004: [Usage]: pydantic version conflict between vllm openai server and transformers

| 字段 | 值 |
| --- | --- |
| Issue | [#4004](https://github.com/vllm-project/vllm/issues/4004) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: pydantic version conflict between vllm openai server and transformers

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm openai server requires pydantic>=2.0, but transformers requires pydantic<2.0 install pydantic==2.6.4. transformers will encounter an error: RuntimeError: Failed to import transformers.models.cohere.tokenization_cohere_fast because of the following error (look up to see its traceback): 'FieldInfo' object has no attribute 'required' install pyantic==1.10.13 vllm openai server will encounter an error: ImportError: cannot import name 'model_validator' from 'pydantic' (/opt/conda/lib/python3.9/site-packages/pydantic/__init__.cpython-39-x86_64-linux-gnu.so)

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Usage]: pydantic version conflict between vllm openai server and transformers usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm vllm openai server r...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: rs will encounter an error: RuntimeError: Failed to import transformers.models.cohere.tokenization_cohere_fast because of the following error (look up to see its traceback): 'FieldInfo' object has no attribute 'required...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
