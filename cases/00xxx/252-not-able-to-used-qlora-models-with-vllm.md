# vllm-project/vllm#252: Not able to used qlora models with vllm 

| 字段 | 值 |
| --- | --- |
| Issue | [#252](https://github.com/vllm-project/vllm/issues/252) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Not able to used qlora models with vllm 

### Issue 正文摘录

I have trained falcon 7b model with qlora but the inference time for outputs is too high.So I want to use vllm for increasing the inference time for that I have used a code snippet to load the model path `llm = LLM(model="/content/trained-model/").` But I am getting an error : ``` OSError: /content/trained-model/ does not appear to have a file named config.json. Checkout 'https://huggingface.co//content/trained-model//None' for available files. ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Not able to used qlora models with vllm I have trained falcon 7b model with qlora but the inference time for outputs is too high.So I want to use vllm for increasing the inference time for that I have used a code snippe...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
