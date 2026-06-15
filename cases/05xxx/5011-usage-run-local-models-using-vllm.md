# vllm-project/vllm#5011: [Usage]: Run local models using vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#5011](https://github.com/vllm-project/vllm/issues/5011) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Run local models using vLLM

### Issue 正文摘录

### Your current environment I tried running the vLLM using the TheBloke/Mistral-7B-Instruct-v0.1-GGUF with the below command ``` python -m vllm.entrypoints.openai.api_server --model /aimodels/mistral-7b-instruct-v0.1.Q4_K_S.gguf --host 0.0.0.0 --port 5555 --tokenizer=hf-internal-testing/llama-tokenizer --trust-remote-code ``` But got the below error. OSError: It looks like the config file at '/aimodels/mistral-7b-instruct-v0.1.Q4_K_S.gguf' is not a valid JSON file. ### How would you like to use vllm I would like to use the TheBloke/Mistral-7B-Instruct-v0.1-GGUF using vLLM

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Run local models using vLLM usage ### Your current environment I tried running the vLLM using the TheBloke/Mistral-7B-Instruct-v0.1-GGUF with the below command ``` python -m vllm.entrypoints.openai.api_server -...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ruct-v0.1.Q4_K_S.gguf --host 0.0.0.0 --port 5555 --tokenizer=hf-internal-testing/llama-tokenizer --trust-remote-code ``` But got the below error. OSError: It looks like the config file at '/aimodels/mistral-7b-instruct-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
