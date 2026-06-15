# vllm-project/vllm#527: why I use fastchat-vllm to inference vicuna-13B，It took 75 G of video memory(A800, 80G)

| 字段 | 值 |
| --- | --- |
| Issue | [#527](https://github.com/vllm-project/vllm/issues/527) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> why I use fastchat-vllm to inference vicuna-13B，It took 75 G of video memory(A800, 80G)

### Issue 正文摘录

python -m vllm.entrypoints.api_server --model /mnt/data/data/luwei/output/0711/checkpoint-2000/ --tokenizer hf-internal-testing/llama-tokenizer --port 32333

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 75 G of video memory(A800, 80G) python -m vllm.entrypoints.api_server --model /mnt/data/data/luwei/output/0711/checkpoint-2000/ --tokenizer hf-internal-testing/llama-tokenizer --port 32333
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: mnt/data/data/luwei/output/0711/checkpoint-2000/ --tokenizer hf-internal-testing/llama-tokenizer --port 32333

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
