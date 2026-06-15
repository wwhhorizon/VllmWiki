# vllm-project/vllm#2789: model continue conversation 

| 字段 | 值 |
| --- | --- |
| Issue | [#2789](https://github.com/vllm-project/vllm/issues/2789) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> model continue conversation 

### Issue 正文摘录

Hi! I have additional ###Instruction: and ###Response: for this instruction from model. I mean that model continues conversation and add additional Instruction and after that response on this instruction I use vllm alpaca.template for model : https://huggingface.co/TheBloke/MLewd-ReMM-L2-Chat-20B-AWQ . In model card described this type of template I tried to use ###Instruction: in stop attribute but it doesn't help me to solve problem

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: model continue conversation Hi! I have additional ###Instruction: and ###Response: for this instruction from model. I mean that model continues conversation and add additional Instruction and after that response on

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
