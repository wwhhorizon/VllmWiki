# vllm-project/vllm#1604: qwen-14b-chat in vllm when the num of input tokens more than 3000 ,generation is so bad and repetitive

| 字段 | 值 |
| --- | --- |
| Issue | [#1604](https://github.com/vllm-project/vllm/issues/1604) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> qwen-14b-chat in vllm when the num of input tokens more than 3000 ,generation is so bad and repetitive

### Issue 正文摘录

qwen-14b-chat when the num of input tokens more than 3000 ,generation is so bad and repetitive,but HF's result is good. The generation result: ` 依据，其，3 依据，22003 依据，3 29 依据，3、3 依据，3 10004848848 依据，其 依据，33888 依据，888888888，判决，84848 08，依据，88880028222000，888 ��8 依据，8 依据，8 依据，848 依据 依据，人民法院，0888888 依据，8 依据，3 依据，8 依据，8 依据8 33 依据，3 依据848 依据88 依据，0 、48 12 2 依据，8 依据88 依据，8 依据，8 依据88 88 领848 依据88 玠288 依据，8 依据，8 人民法院，8 人民法院，其 依据，其3 88 3 人民法院，8 依据8 依据，2 依据8 8 依据8 依据8 依据8 8 88 8 8 依据8 8 额8 8 8 依据8 依据 8 依据8 依据 8 8 8 、88 人民法院 人民法院，8 8 依据，人民法院，4 人民法院，88 8 人民法院， 8 8 8 8 人民法院，人民法院，对8 颠 人民法院 人民法院8 人民法院 人民法院，人民法院88 人民法院 人民法院，人民法院88 人民法院，8 人民法院 人民法院，88 人民法院 人民法院，48 人民法院，48 人民法院 人民法院，人民法院，人民法院 人民法院 人民法院 人民法院 人民法院 人民法院，人民法院 人民法院，人民法院 依据8 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 依据 人民法院 人民法院 人民法院 依据 人民法院 人民法院，人民法院，人民法院 人民法院 人民法院 人民法院8 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院，人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院888 人民法院 人民法院8 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院 人民法院...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: qwen-14b-chat in vllm when the num of input tokens more than 3000 ,generation is so bad and repetitive qwen-14b-chat when the num of input tokens more than 3000 ,generation is so bad and repetitive,but HF's result is goo

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
