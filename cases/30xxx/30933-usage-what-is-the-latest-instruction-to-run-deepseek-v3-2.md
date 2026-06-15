# vllm-project/vllm#30933: [Usage]: What is the latest instruction to run DeepSeek V3.2?

| 字段 | 值 |
| --- | --- |
| Issue | [#30933](https://github.com/vllm-project/vllm/issues/30933) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: What is the latest instruction to run DeepSeek V3.2?

### Issue 正文摘录

### Your current environment vLLM 0.12.0 ### How would you like to use vllm I am following the guidelines here https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html for running DeepSeek v3.2. By following the instructions I installed vLLM 0.12.0 on my H200 node. However, when I try to run it with `vllm serve deepseek-ai/DeepSeek-V3.2 --tensor-parallel-size 8 --tokenizer-mode deepseek_v32` it gives an error ``` (APIServer pid=816209) ValueError: No tokenizer registered for tokenizer_mode='deepseek_v32'. ``` If I do not include the `--tokenizer-mode` then the server spins up with no errors, but when I try to send a request, I get another error below ``` (APIServer pid=753941) ERROR 12-18 06:04:47 [serving_chat.py:263] ValueError: As of transformers v4.44, default chat template is no longer allowed, so you must provide a chat template if the tokenizer does not define one. ``` I am wondering if there is an update on the instructions to run DeepSeek V3.2 on vLLM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/l...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: vllm I am following the guidelines here https://docs.vllm.ai/projects/recipes/en/latest/DeepSeek/DeepSeek-V3_2.html for running DeepSeek v3.2. By following the instructions I installed vLLM 0.12.0 on my H200 node. Howev...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: LM. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: -mode` then the server spins up with no errors, but when I try to send a request, I get another error below ``` (APIServer pid=753941) ERROR 12-18 06:04:47 [serving_chat.py:263] ValueError: As of transformers v4.44, def...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: [Usage]: What is the latest instruction to run DeepSeek V3.2? usage ### Your current environment vLLM 0.12.0 ### How would you like to use vllm I am following the guidelines here https://docs.vllm.ai/projects/recipes/en...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
