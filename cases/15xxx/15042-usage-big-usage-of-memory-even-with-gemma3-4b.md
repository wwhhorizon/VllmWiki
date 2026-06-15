# vllm-project/vllm#15042: [Usage]: Big usage of memory even with gemma3-4b

| 字段 | 值 |
| --- | --- |
| Issue | [#15042](https://github.com/vllm-project/vllm/issues/15042) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Big usage of memory even with gemma3-4b

### Issue 正文摘录

### Your current environment I am trying to figure why i have so big gpu usage using even the gemma3-4b-it model. I serve like this: ``` vllm serve google/gemma-3-4b-it \ --max-model-len 1024 \ --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --quantization bitsandbytes \ --load-format bitsandbytes \ --host 0.0.0.0 \ --port 8080 ``` and it hits around 15Gb of GPU. With ollama I could run 8B models with around 12-14GB GPU! What am I missing here? If i use `-gpu-memory-utilization 0.7 `, the gpu memory goes down a little bit but I am not sure if I want that? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: it \ --max-model-len 1024 \ --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --quantization bitsandbytes \ --load-format bitsandbytes \ --host 0.0.0.0 \ --port 8080 ``` and it hits around 15Gb
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Usage]: Big usage of memory even with gemma3-4b usage ### Your current environment I am trying to figure why i have so big gpu usage using even the gemma3-4b-it model. I serve like this: ``` vllm serve google/gemma-3-4...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: t? ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. ### Before submitting a new issue... - [x] Make sure you already searched f...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: \ --max-num-seqs 2 \ --dtype bfloat16 \ --device=cuda \ --trust-remote-code \ --quantization bitsandbytes \ --load-format bitsandbytes \ --host 0.0.0.0 \ --port 8080 ``` and it hits around 15Gb of GPU. With ollama I cou...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ! What am I missing here? If i use `-gpu-memory-utilization 0.7 `, the gpu memory goes down a little bit but I am not sure if I want that? ### How would you like to use vllm I want to run inference of a [specific model]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
