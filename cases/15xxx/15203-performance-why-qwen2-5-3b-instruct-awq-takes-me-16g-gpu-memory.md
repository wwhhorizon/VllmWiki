# vllm-project/vllm#15203: [Performance]: why Qwen2.5-3B-Instruct-AWQ takes me 16G GPU memory?

| 字段 | 值 |
| --- | --- |
| Issue | [#15203](https://github.com/vllm-project/vllm/issues/15203) |
| 状态 | closed |
| 标签 | performance |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: why Qwen2.5-3B-Instruct-AWQ takes me 16G GPU memory?

### Issue 正文摘录

### Proposal to improve performance Ubuntu 22, RTX3090. I've ran `vllm 0.8.1` with a very small model of https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-AWQ with below: ``` vllm serve Qwen/Qwen2.5-3B-Instruct-AWQ INFO 03-20 17:28:12 [__init__.py:256] Automatically detected platform cuda. INFO 03-20 17:28:13 [api_server.py:977] vLLM API server version 0.8.1 ``` it works good, but when I looked via `nvidia-smi`, it takes almost 16G: ``` anaconda3/envs/vllm/bin/python 15982MiB ``` and i've changed to a bigger model of https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ but got the same GPU memory usage. Question: why `3B-Instruct-AWQ` takes 16G? why `7B-Instruct-AWQ` takes the same GPU memory? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The output of `python collect_env.py` ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: GPU memory? performance ### Proposal to improve performance Ubuntu 22, RTX3090. I've ran `vllm 0.8.1` with a very small model of https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-AWQ with below: ``` vllm serve Qwen/Qwen2....
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Performance]: why Qwen2.5-3B-Instruct-AWQ takes me 16G GPU memory? performance ### Proposal to improve performance Ubuntu 22, RTX3090. I've ran `vllm 0.8.1` with a very small model of https://huggingface.co/Qwen/Qwen2....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d platform cuda. INFO 03-20 17:28:13 [api_server.py:977] vLLM API server version 0.8.1 ``` it works good, but when I looked via `nvidia-smi`, it takes almost 16G: ``` anaconda3/envs/vllm/bin/python 15982MiB ``` and i've...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: `7B-Instruct-AWQ` takes the same GPU memory? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) ```text The ou...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ts of frequently asked questions. performance frontend_api;model_support;quantization cuda;quantization env_dependency Proposal to improve performance

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
