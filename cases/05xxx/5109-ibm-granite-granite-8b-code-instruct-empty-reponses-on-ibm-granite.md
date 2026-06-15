# vllm-project/vllm#5109: [ibm-granite/granite-8b-code-instruct]: Empty reponses on ibm-granite  

| 字段 | 值 |
| --- | --- |
| Issue | [#5109](https://github.com/vllm-project/vllm/issues/5109) |
| 状态 | closed |
| 标签 | new-model |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [ibm-granite/granite-8b-code-instruct]: Empty reponses on ibm-granite  

### Issue 正文摘录

### The model to consider. https://huggingface.co/ibm-granite/granite-3b-code-instruct https://huggingface.co/ibm-granite/granite-8b-code-instruct ### The closest model vllm already supports. https://huggingface.co/ibm-granite/granite-20b-code-instruct https://huggingface.co/ibm-granite/granite-34b-code-instruct ### What's your difficulty of supporting the model you want? Chat completion produces **empty responses** when loading OpenAI API with ibm-granite 3b and 8b code-instruct models. 20b and 34b models produce expected responses. **Output** ![Screenshot 2024-05-29 173200](https://github.com/vllm-project/vllm/assets/4145857/fcc31555-3be6-4dab-80b1-94812f8ddbb8) **VLLM startup script** ```bash MODEL="ibm-granite/granite-8b-code-instruct" API_KEY="XXXXXXXXXXXX" python -m vllm.entrypoints.openai.api_server \ --tokenizer $MODEL \ --model $MODEL \ --served-model-name granite-8b \ --gpu-memory-utilization 0.9 \ --enforce-eager \ --api-key $API_KEY ```

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: m-granite/granite-8b-code-instruct]: Empty reponses on ibm-granite new-model ### The model to consider. https://huggingface.co/ibm-granite/granite-3b-code-instruct https://huggingface.co/ibm-granite/granite-8b-code-inst...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
