# vllm-project/vllm#1620: Upgraded openai-python (v0->v1) refuses argumment "repetition_penalty"

| 字段 | 值 |
| --- | --- |
| Issue | [#1620](https://github.com/vllm-project/vllm/issues/1620) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Upgraded openai-python (v0->v1) refuses argumment "repetition_penalty"

### Issue 正文摘录

I notice that about 2 weeks ago [vllm](https://github.com/vllm-project/vllm) has merged pr about "repetition_penalty" aligned with huggingface. (refer to [pr 1424](https://github.com/vllm-project/vllm/pull/1424)) However, openai-python also graded to v1 several days ago. In this important commit, openai refuses the unknown argument repetition_penalty. The following is the detail error. ` xxx/examples/openai_chatcompletion_client.py", line 72, in chat_completion = client.chat.completions.create( File "/opt/conda/lib/python3.10/site-packages/openai/_utils/_utils.py", line 299, in wrapper return func(*args, **kwargs) TypeError: Completions.create() got an unexpected keyword argument 'repetition_penalty'` I also havereported this issue to openai (https://github.com/openai/openai-python/issues/767) and I wonder if there is any solution in vllm side.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: 24)) However, openai-python also graded to v1 several days ago. In this important commit, openai refuses the unknown argument repetition_penalty. The following is the detail error. ` xxx/examples/openai_chatcompletion_c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: vllm-project/vllm) has merged pr about "repetition_penalty" aligned with huggingface. (refer to [pr 1424](https://github.com/vllm-project/vllm/pull/1424)) However, openai-python also graded to v1 several days ago. In th...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
