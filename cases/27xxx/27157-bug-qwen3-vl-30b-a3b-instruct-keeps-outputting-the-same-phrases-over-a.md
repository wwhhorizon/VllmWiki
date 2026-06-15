# vllm-project/vllm#27157: [Bug]: Qwen3-VL-30B-A3B-Instruct keeps outputting the same phrases over and over

| 字段 | 值 |
| --- | --- |
| Issue | [#27157](https://github.com/vllm-project/vllm/issues/27157) |
| 状态 | open |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL-30B-A3B-Instruct keeps outputting the same phrases over and over

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I'm using the latest Docker image for vLLM 0.11.0 running Qwen3-VL-30B-A3B-Instruct on an RTX Pro 6000 Blackwell on Ubuntu 24.04: ```#!/bin/bash docker run --rm --runtime nvidia --gpus all \ -v /opt/models:/opt/models \ -p 8000:8000 \ --ipc=host \ vllm/vllm-openai:latest-x86_64 \ --max-num-seq 3 \ --max-model-len 162144 \ --model /opt/models/Qwen3-VL-30B-A3B-Instruct ``` In many situations the model will keep outputting the same phrase over and over after some time. Usually it takes some turns between the user and the LLM to manifest, but I eventually found a way to replicate it somewhat reliably in a single prompt: https://gist.github.com/kozanryusui/65b1b3b702e8b84b1d0fbe402a5ab239 The prompt is a copypaste of the Wikipedia article on the characters in One Piece and asking the model to identify the most prolific Japanese voice actors. It will start generating text normally and then eventually get stuck repeating the same character name over and over again (see gist link for results). This was tested using Open WebUI. I have also seen this behavior when connecting from a custom application via the OpenAI API. In this case after...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: est Docker image for vLLM 0.11.0 running Qwen3-VL-30B-A3B-Instruct on an RTX Pro 6000 Blackwell on Ubuntu 24.04: ```#!/bin/bash docker run --rm --runtime nvidia --gpus all \ -v /opt/models:/opt/models \ -p 8000:8000 \ -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: our current environment ### 🐛 Describe the bug I'm using the latest Docker image for vLLM 0.11.0 running Qwen3-VL-30B-A3B-Instruct on an RTX Pro 6000 Blackwell on Ubuntu 24.04: ```#!/bin/bash docker run --rm --runtime n...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-VL-30B-A3B-Instruct keeps outputting the same phrases over and over bug ### Your current environment ### 🐛 Describe the bug I'm using the latest Docker image for vLLM 0.11.0 running Qwen3-VL-30B-A3B-Instruc...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: anged from the model defaults. I also tried different model and KV cache quants without any notable changes. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the c...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ) were changed from the model defaults. I also tried different model and KV cache quants without any notable changes. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
