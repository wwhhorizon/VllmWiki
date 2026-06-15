# vllm-project/vllm#15204: [Misc]: why `3B-Instruct-AWQ` takes 16G

| 字段 | 值 |
| --- | --- |
| Issue | [#15204](https://github.com/vllm-project/vllm/issues/15204) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
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

> [Misc]: why `3B-Instruct-AWQ` takes 16G

### Issue 正文摘录

### Anything you want to discuss about vllm. Ubuntu 22, RTX3090. I've ran `vllm 0.8.1` with a very small model of https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-AWQ with below: ``` vllm serve Qwen/Qwen2.5-3B-Instruct-AWQ INFO 03-20 17:28:12 [__init__.py:256] Automatically detected platform cuda. INFO 03-20 17:28:13 [api_server.py:977] vLLM API server version 0.8.1 ``` it works good, but when I looked via `nvidia-smi`, it takes almost 16G: ``` anaconda3/envs/vllm/bin/python 15982MiB ``` and i've changed to a bigger model of https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ but got the same GPU memory usage. Question: why `3B-Instruct-AWQ` takes 16G? why `7B-Instruct-AWQ` takes the same GPU memory? ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: takes 16G usage ### Anything you want to discuss about vllm. Ubuntu 22, RTX3090. I've ran `vllm 0.8.1` with a very small model of https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-AWQ with below: ``` vllm serve Qwen/Qwen2...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: about vllm. Ubuntu 22, RTX3090. I've ran `vllm 0.8.1` with a very small model of https://huggingface.co/Qwen/Qwen2.5-3B-Instruct-AWQ with below: ``` vllm serve Qwen/Qwen2.5-3B-Instruct-AWQ INFO 03-20 17:28:12 [__init__....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: d platform cuda. INFO 03-20 17:28:13 [api_server.py:977] vLLM API server version 0.8.1 ``` it works good, but when I looked via `nvidia-smi`, it takes almost 16G: ``` anaconda3/envs/vllm/bin/python 15982MiB ``` and i've...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ts of frequently asked questions. performance frontend_api;model_support;quantization cuda;quantization env_dependency Anything you want to discuss about vllm.
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: of https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-AWQ but got the same GPU memory usage. Question: why `3B-Instruct-AWQ` takes 16G? why `7B-Instruct-AWQ` takes the same GPU memory? ### Before submitting a new issue......

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
