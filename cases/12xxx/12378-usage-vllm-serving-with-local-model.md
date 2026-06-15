# vllm-project/vllm#12378: [Usage]: vLLM serving with local model

| 字段 | 值 |
| --- | --- |
| Issue | [#12378](https://github.com/vllm-project/vllm/issues/12378) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: vLLM serving with local model

### Issue 正文摘录

### Your current environment Both ways failed with vllm 0.6.6. I have a local directory ```/myhome/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-1.5B```, where I store a huggingface model. I am trying to use vllm to deploy this model. I have tried two ways: The first way: ``` HF_HOME=/myhome/huggingface vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B --model deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B ``` The second way: ``` python -m vllm.entrypoints.openai.api_server --model /myhome/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-1.5B ``` both way it returns the same error `huggingface_hub.errors.HFValidationError: Repo id must be in the form 'repo_name' or 'namespace/repo_name': '/myhome/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-1.5B'. Use repo_type argument if needed` Seems both related issues doesn't help for this version of vllm. https://github.com/vllm-project/vllm/issues/1131 https://github.com/vllm-project/vllm/issues/2924 ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you al...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: vLLM serving with local model usage ### Your current environment Both ways failed with vllm 0.6.6. I have a local directory ```/myhome/huggingface/hub/models--deepseek-ai--DeepSeek-R1-Distill-Qwen-1.5B```, wher...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ype argument if needed` Seems both related issues doesn't help for this version of vllm. https://github.com/vllm-project/vllm/issues/1131 https://github.com/vllm-project/vllm/issues/2924 ### How would you like to use vl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: lm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
