# vllm-project/vllm#479: Request: NTK rope support

| 字段 | 值 |
| --- | --- |
| Issue | [#479](https://github.com/vllm-project/vllm/issues/479) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Request: NTK rope support

### Issue 正文摘录

Hi, there are some very sucessfull experiements shows that NTK based RoPE can obtain a good extrapolate ability without even finetune. I have test as well, it works well, an 1024 trained model can have a very impressive long context ability with NTK RoPE. Would consider support it as it doesn't requires many changes (maybe)? However, the pos op implement baked in cu op kernel. Currently I can using torch code to judge if context length bigger than 2048 then applying NTK, but isn't would be better if vllm can support it out of box?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: hout even finetune. I have test as well, it works well, an 1024 trained model can have a very impressive long context ability with NTK RoPE. Would consider support it as it doesn't requires many changes (maybe)? However...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: Request: NTK rope support feature request Hi, there are some very sucessfull experiements shows that NTK based RoPE can obtain a good extrapolate ability without even finetune. I have test as well, it works well, an 102
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: oPE can obtain a good extrapolate ability without even finetune. I have test as well, it works well, an 1024 trained model can have a very impressive long context ability with NTK RoPE. Would consider support it as it d...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
