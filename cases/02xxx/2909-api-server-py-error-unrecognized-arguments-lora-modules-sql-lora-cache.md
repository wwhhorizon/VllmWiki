# vllm-project/vllm#2909: api_server.py: error: unrecognized arguments: --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/

| 字段 | 值 |
| --- | --- |
| Issue | [#2909](https://github.com/vllm-project/vllm/issues/2909) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> api_server.py: error: unrecognized arguments: --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/

### Issue 正文摘录

run codes below `python -m vllm.entrypoints.api_server \ --model meta-llama/Llama-2-7b-hf \ --enable-lora \ --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/` raise an error: api_server.py: error: unrecognized arguments: --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rver.py: error: unrecognized arguments: --lora-modules sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/ run codes below `python -m vllm.entrypoints.api_server \ --model meta-llama/Llama-2-7b-hf...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: les sql-lora=~/.cache/huggingface/hub/models--yard1--llama-2-7b-sql-lora-test/ run codes below `python -m vllm.entrypoints.api_server \ --model meta-llama/Llama-2-7b-hf \ --enable-lora \ --lora-modules sql-lora=~/.cache...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
