# vllm-project/vllm#864: Hello!I want to use 16 * A10(16 * a10) to inference Llama2-70B（fp16）

| 字段 | 值 |
| --- | --- |
| Issue | [#864](https://github.com/vllm-project/vllm/issues/864) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Hello!I want to use 16 * A10(16 * a10) to inference Llama2-70B（fp16）

### Issue 正文摘录

I have 16 GPUs in one machine. ![image](https://github.com/vllm-project/vllm/assets/74184102/30156193-f876-4914-bc1d-0a080026978e) This erro appears in other project when I use 16 * A10(16 * 23G) to inference Llama2-70B： ![image](https://github.com/vllm-project/vllm/assets/74184102/71c50bfb-7415-49e1-b8b0-adca4418d970) I ask many people to solve this problem,but failed. I know 8 gpu can work it! But I need to increase the prompt of llama2, the 8 GPU is not enough! Do you have some ideas. In this project，can you solve it？Thanks！

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: Hello!I want to use 16 * A10(16 * a10) to inference Llama2-70B（fp16） I have 16 GPUs in one machine. ![image](https://github.com/vllm-project/vllm/assets/74184102/30156193-f876-4914-bc1d-0a080026978e) This erro appears i...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
