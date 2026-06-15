# vllm-project/vllm#725: Can vllm support Chat mode？such as human talk ai via Baichuan-13B-Chat model,rather than model.forward()

| 字段 | 值 |
| --- | --- |
| Issue | [#725](https://github.com/vllm-project/vllm/issues/725) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Can vllm support Chat mode？such as human talk ai via Baichuan-13B-Chat model,rather than model.forward()

### Issue 正文摘录

**current output will automatically complete the prompt, which is not what I want** ![image](https://github.com/vllm-project/vllm/assets/57557769/017a1202-c6af-4b43-822c-7b0cfa0ebbb1) **expect output** ![企业微信截图_16916352159786](https://github.com/vllm-project/vllm/assets/57557769/8bc61949-c765-4b9f-a974-b2ae037c970b) I find TGI have the same question，so i expect vLLM can support a Chat mode，we can communicate with the model normally

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Can vllm support Chat mode？such as human talk ai via Baichuan-13B-Chat model,rather than model.forward() **current output will automatically complete the prompt, which is not what I want** ![image](https://github.com/vl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
