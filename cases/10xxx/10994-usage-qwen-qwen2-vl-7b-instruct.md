# vllm-project/vllm#10994: [Usage]: Qwen/Qwen2-VL-7B-Instruct

| 字段 | 值 |
| --- | --- |
| Issue | [#10994](https://github.com/vllm-project/vllm/issues/10994) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Qwen/Qwen2-VL-7B-Instruct

### Issue 正文摘录

### The model to consider. https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting the model you want? i deployed the model using vllm using the below command . vllm serve Qwen/Qwen2-VL-7B-Instruct How could i call this endpoint using curl command ? i used this curl command: curl http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model":"Qwen/Qwen2-VL-7B-Instruct","messages":[{"role":"system","content":"You are Qwen, a vision-language AI assistant created by Alibaba Cloud."},{"role":"user","content":"Describe this image in detail. [Image: '"$(base64 -w 0 /home/azureuser/qwen/test.jpeg)"']"}],"temperature":0.7,"top_p":0.8,"max_tokens":100}' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: Qwen/Qwen2-VL-7B-Instruct usage ### The model to consider. https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct ### The closest model vllm already supports. _No response_ ### What's your difficulty of supporting th...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 0}' ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: cribe this image in detail. [Image: '"$(base64 -w 0 /home/azureuser/qwen/test.jpeg)"']"}],"temperature":0.7,"top_p":0.8,"max_tokens":100}' ### Before submitting a new issue... - [X] Make sure you already searched for re...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
