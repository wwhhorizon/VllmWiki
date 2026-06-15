# vllm-project/vllm#2557: AsyncLLMengine maybe have bugs?

| 字段 | 值 |
| --- | --- |
| Issue | [#2557](https://github.com/vllm-project/vllm/issues/2557) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> AsyncLLMengine maybe have bugs?

### Issue 正文摘录

Has anyone encountered this situation： I use greedy search. set temperature=1e-9 when I use LLMengine, the model's output is OK. when I use AsyncLLMengine, the model's output is different from 'LLMengine's'. In my test dataset, these two situation‘output are mostly the same. other parts is different why? Is my settings incorrect? I use entrypoints code api_server.py

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: e maybe have bugs? Has anyone encountered this situation： I use greedy search. set temperature=1e-9 when I use LLMengine, the model's output is OK. when I use AsyncLLMengine, the model's output is different from 'LLMeng...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: on： I use greedy search. set temperature=1e-9 when I use LLMengine, the model's output is OK. when I use AsyncLLMengine, the model's output is different from 'LLMengine's'. In my test dataset, these two situation‘output...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cLLMengine, the model's output is different from 'LLMengine's'. In my test dataset, these two situation‘output are mostly the same. other parts is different why? Is my settings incorrect? I use entrypoints code api_serv...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
