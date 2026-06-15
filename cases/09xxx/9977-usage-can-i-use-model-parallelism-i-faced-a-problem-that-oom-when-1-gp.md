# vllm-project/vllm#9977: [Usage]: Can I use model parallelism? I faced a problem that OOM when 1 gpu, even though I have multi-gpu

| 字段 | 值 |
| --- | --- |
| Issue | [#9977](https://github.com/vllm-project/vllm/issues/9977) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 | oom |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Can I use model parallelism? I faced a problem that OOM when 1 gpu, even though I have multi-gpu

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. The model(int4) needs about 20GB CUDA Memory, I have 2 * 3080Ti(2 * 12GB), can I run the model in this machine? ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: `` ### How would you like to use vllm I want to run inference of a [specific model](put link here). I don't know how to integrate it with vllm. The model(int4) needs about 20GB CUDA Memory, I have 2 * 3080Ti(2 * 12GB),...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: l](put link here). I don't know how to integrate it with vllm. The model(int4) needs about 20GB CUDA Memory, I have 2 * 3080Ti(2 * 12GB), can I run the model in this machine? ### Before submitting a new issue... - [X] M...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Usage]: Can I use model parallelism? I faced a problem that OOM when 1 gpu, even though I have multi-gpu usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to us...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Usage]: Can I use model parallelism? I faced a problem that OOM when 1 gpu, even though I have multi-gpu usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to us...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Usage]: Can I use model parallelism? I faced a problem that OOM when 1 gpu, even though I have multi-gpu usage ### Your current environment ```text The output of `python collect_env.py` ``` ### How would you like to us...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
