# vllm-project/vllm#5318: [New Model]: mistralai/Codestral-22B-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#5318](https://github.com/vllm-project/vllm/issues/5318) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [New Model]: mistralai/Codestral-22B-v0.1

### Issue 正文摘录

### The model to consider. Hi. Could you add support to [mistralai/Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1)? Thanks! ### The closest model vllm already supports. https://huggingface.co/meta-llama/CodeLlama-7b-hf https://huggingface.co/mistralai/Mistral-7B-v0.3 ### What's your difficulty of supporting the model you want? Can't load **Codestral-22B-v0.1** using OpenAI server API ```bash ORG="mistralai" MODEL="Codestral-22B-v0.1" API_KEY=XXXXXXXXXXXXXXXXXXXXXX python -m vllm.entrypoints.openai.api_server \ --tokenizer $ORG/$MODEL \ --model $ORG/$MODEL \ --served-model-name $MODEL \ --tensor-parallel-size 4 \ --gpu-memory-utilization 0.9 \ --max-model-len 4096 \ --enforce-eager \ --api-key $API_KEY ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [New Model]: mistralai/Codestral-22B-v0.1 new-model ### The model to consider. Hi. Could you add support to [mistralai/Codestral-22B-v0.1](https://huggingface.co/mistralai/Codestral-22B-v0.1)? Thanks! ### The closest mo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
