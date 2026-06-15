# vllm-project/vllm#2381: Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated.

| 字段 | 值 |
| --- | --- |
| Issue | [#2381](https://github.com/vllm-project/vllm/issues/2381) |
| 状态 | closed |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated.

### Issue 正文摘录

Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated. use the following vllm_wrapper: https://github.com/QwenLM/vllm-gptq/blob/main/tests/qwen/vllm_wrapper.py

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated. Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated. use the following vllm_wrapper: https://github.com/QwenLM/vllm-gptq/blob/main/tests/qwen/vllm_wra
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated. Qwen-14B-Chat-Int4 GPTQ model using vLLM is not acceralated. use the following vllm_wrapper: https://github.com/QwenLM/vllm-gptq/blob/main/tests/qwen/vllm_wra...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: he following vllm_wrapper: https://github.com/QwenLM/vllm-gptq/blob/main/tests/qwen/vllm_wrapper.py

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
