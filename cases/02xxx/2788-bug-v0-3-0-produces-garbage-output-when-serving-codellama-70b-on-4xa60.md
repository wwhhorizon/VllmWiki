# vllm-project/vllm#2788: [Bug] `v0.3.0` produces garbage output when serving CodeLlama-70B on 4xA6000

| 字段 | 值 |
| --- | --- |
| Issue | [#2788](https://github.com/vllm-project/vllm/issues/2788) |
| 状态 | closed |
| 标签 |  |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] `v0.3.0` produces garbage output when serving CodeLlama-70B on 4xA6000

### Issue 正文摘录

![image](https://github.com/vllm-project/vllm/assets/38074777/5f8862cf-4ef8-4bd1-a259-b67aadeabc29) Can be fixed by downgrading to `v0.2.7`.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug] `v0.3.0` produces garbage output when serving CodeLlama-70B on 4xA6000 ![image](https://github.com/vllm-project/vllm/assets/38074777/5f8862cf-4ef8-4bd1-a259-b67aadeabc29) Can be fixed by downgrading to `v0.2.7`.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
