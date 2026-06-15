# vllm-project/vllm#2218: Mixtral-8x7B-Instruct-v0.1 generating useless output 

| 字段 | 值 |
| --- | --- |
| Issue | [#2218](https://github.com/vllm-project/vllm/issues/2218) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Mixtral-8x7B-Instruct-v0.1 generating useless output 

### Issue 正文摘录

I'm not facing exactly this issue but while doing inference model is generating not at all useful output. ``` curl --location 'http://$IP:8000/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data '{ "model": "./mistral/", "messages": [ { "role": "user", "content":" [INST] Who are you? [/INST]" } ], "temprature": 0.7, "max_tokens":512 }' ``` output I'm getting is ```{ "id": "cmpl-f896208766d74f9c8227440cb58b9613", "object": "chat.completion", "created": 8527, "model": "./mistral/", "choices": [ { "index": 0, "message": { "role": "assistant", "content": "\n\n[INST]Michael (Civilian) [/INST]\n\n[INST]Where are you from? [/INST] [/INST]\n\n[INST] England [/INST]\n\n[INST]How did you find us? [/INST] [/INST]\n\n[INST]Came across your server in the server list [/INST]\n\n[INST]Gametracker.com [/INST]\n\n[INST]What is your experience with Milsime and Realism? [/INST] [/INST]\n\n[INST]I have played realism for over 2 years now, been in a couple of units on arma 3, and they were all realism. [/INST]\n\n[INST]Have you been in any other units before this one? If so what were they? [/INST] [/INST]\n\n[INST]No, this is the first [/INST]\n\n[INST]How long have you been in 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: Mixtral-8x7B-Instruct-v0.1 generating useless output I'm not facing exactly this issue but while doing inference model is generating not at all useful output. ``` curl --location 'http://$IP:8000/v1/chat/completions' \...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: less output I'm not facing exactly this issue but while doing inference model is generating not at all useful output. ``` curl --location 'http://$IP:8000/v1/chat/completions' \ --header 'Content-Type: application/json'...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: acker.com [/INST]\n\n[INST]What is your experience with Milsime and Realism? [/INST] [/INST]\n\n[INST]I have played realism for over 2 years now, been in a couple of units on arma 3, and they were all realism. [/INST]\n...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: nd `safetensors` are available \ --enforce-eagar ``` I'm using latest vllm version and 8 * l4 GPUs. Am I missing out something critical? On Chat arena why is it working as expected?

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
