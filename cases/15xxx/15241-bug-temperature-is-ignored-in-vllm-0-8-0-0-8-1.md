# vllm-project/vllm#15241: [Bug]: Temperature is ignored in vLLM 0.8.0/0.8.1

| 字段 | 值 |
| --- | --- |
| Issue | [#15241](https://github.com/vllm-project/vllm/issues/15241) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Temperature is ignored in vLLM 0.8.0/0.8.1

### Issue 正文摘录

### Your current environment ### Description In vLLM 0.7 and before, using a high temperature (10) with a random input string **always** returns "max_tokens" number of tokens (random output of the correct length) With a temperature of 0, it returns something similar to "It seems like you've entered a string of characters that doesn't appear to be a meaningful word, phrase, or question." Using the docker image 0.8.0 or 0.8.1, no matter the temperature, it always answers something like "It seems like you've entered a string of characters that doesn't appear to be a meaningful word, phrase, or question." ### Details I tried with multiple models and the temperature seems to be ignored for all of them ### 🐛 Describe the bug ### Reproduction Starting a Docker container with: `docker run --gpus all \ --entrypoint bash \ -v ~/.cache/huggingface:/root/.cache/huggingface \ --ipc=host \ -p 8000:8000 \ -it \ vllm/vllm-openai:v0.7.3` and running ```python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-7B-Instruct --trust-remote-code --max-model-len 32768 --tensor-parallel-size 2 --gpu-memory-utilization 0.95``` on the server-side, and ```import random import string import time...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: doesn't appear to be a meaningful word, phrase, or question." Using the docker image 0.8.0 or 0.8.1, no matter the temperature, it always answers something like "It seems like you've entered a string of characters that...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: eaningful word, phrase, or question." ### Details I tried with multiple models and the temperature seems to be ignored for all of them ### 🐛 Describe the bug ### Reproduction Starting a Docker container with: `docker ru...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
