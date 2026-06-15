# vllm-project/vllm#1918: chatglm3-6b model automatically outputs special token, like <|user|>、<|assistant|>

| 字段 | 值 |
| --- | --- |
| Issue | [#1918](https://github.com/vllm-project/vllm/issues/1918) |
| 状态 | closed |
| 标签 |  |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> chatglm3-6b model automatically outputs special token, like <\|user\|>、<\|assistant\|>

### Issue 正文摘录

I am running multi-turn dialogue program of chatglm3-6b deployed by vllm/entrypoints/openai/api_server.py, the input to vllm service is a history of list[Message], and the model ouputs like this ``` 用户: hi 小亿:how are you? > Hi, I'm XiaoYi. Nice to meet you. How can I help you today? i want to know about the weather in beijing for today. The weather in Beijing is currently sunny with a high of 25 degrees Celsius and a low of 13 degrees Celsius. It's also windy, with a speed of 4-5级。Please note that this information is based on data from earlier this morning and may change by the time you are asking. 用户: ``` and the program wait for another user input. the model automatically outputs special tokens like . it's very weird, how to solve this... and I deployed the service using python: python api_server.py --model="/model/chatglm3-6b" --trust-remote-code . the model already downloaded, the save path is "/model/chatglm3-6b"

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: chatglm3-6b model automatically outputs special token, like <|user|>、<|assistant|> I am running multi-turn dialogue program of chatglm3-6b deployed by vllm/entrypoints/openai/api_server.py, the input to vllm service is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: chatglm3-6b model automatically outputs special token, like <|user|>、<|assistant|> I am running multi-turn dialogue program of chatglm3-6b deployed by vllm/entrypoints/openai/api_server.py, the input to vllm service is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
