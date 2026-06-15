# vllm-project/vllm#3188: TypeError: TextGenerationStreamResponse.__init__() got an unexpected keyword argument 'index'

| 字段 | 值 |
| --- | --- |
| Issue | [#3188](https://github.com/vllm-project/vllm/issues/3188) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> TypeError: TextGenerationStreamResponse.__init__() got an unexpected keyword argument 'index'

### Issue 正文摘录

I ran it using the code on the official website, but encountered an error. May I ask what the reason is？ from huggingface_hub import InferenceClient client = InferenceClient(model="http://127.0.0.1:8080") # resp = client.text_generation(prompt="who are you", stream=True) for token in client.text_generation("who are you?",stream=True): print(token) error: TypeError: TextGenerationStreamResponse.__init__() got an unexpected keyword argument 'index'

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: n unexpected keyword argument 'index' I ran it using the code on the official website, but encountered an error. May I ask what the reason is？ from huggingface_hub import InferenceClient client = InferenceClient(model="...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: al website, but encountered an error. May I ask what the reason is？ from huggingface_hub import InferenceClient client = InferenceClient(model="http://127.0.0.1:8080") # resp = client.text_generation(prompt="who are you...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
