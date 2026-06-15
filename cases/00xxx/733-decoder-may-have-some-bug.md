# vllm-project/vllm#733: decoder may have some bug

| 字段 | 值 |
| --- | --- |
| Issue | [#733](https://github.com/vllm-project/vllm/issues/733) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> decoder may have some bug

### Issue 正文摘录

## this is something wrong when using GPTBigCodeForCausalLM model in decoder，while using greedy method. ### basemodel starcoderbase-15b huggingface ### prompt： `/**\n * Write typescript function to find the minimum cost path to reach (m, n) from (0, 0) for the given cost matrix cost[][] and a position (m, n) in cost[][].\n * \n * Examples:\n * >>> min_cost([[1, 2, 3], [4, 8, 2], [1, 5, 3]], 2, 2)\n * >>> 8\n * >>> min_cost([[2, 3, 4], [5, 9, 3], [2, 6, 4]], 2, 2)\n * >>> 12\n * >>> min_cost([[3, 4, 5], [6, 10, 4], [3, 7, 5]], 2, 2)\n * >>> 16\n */\nconst min_cost = function (cost: Array >, m: number, n: number) : number {\n` ### vllm generate result: `\t>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>` #### greedy config ` sam...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: ave some bug ## this is something wrong when using GPTBigCodeForCausalLM model in decoder，while using greedy method. ### basemodel starcoderbase-15b huggingface ### prompt： `/**\n * Write typescript function to find the...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: decoder may have some bug ## this is something wrong when using GPTBigCodeForCausalLM model in decoder，while using greedy method. ### basemodel starcoderbase-15b huggingface ### prompt： `/**\n * Write typescript functi

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
