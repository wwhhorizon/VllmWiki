# vllm-project/vllm#21797: [Bug]: speculative decoding not implemented error

| 字段 | 值 |
| --- | --- |
| Issue | [#21797](https://github.com/vllm-project/vllm/issues/21797) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: speculative decoding not implemented error

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Following the speculative decoding example provided in the [docs](url), I run into a NotImplemented error. Code to reproduce: ``` python -m vllm.entrypoints.openai.api_server \ --host 0.0.0.0 \ --port 8000 \ --download-dir $home_path \ --model facebook/opt-6.7b \ --seed 42 \ -tp 1 \ --gpu_memory_utilization 0.8 \ --speculative_config '{"model": "facebook/opt-125m", "num_speculative_tokens": 5}' ``` Error: ` raise NotImplementedError( NotImplementedError: Speculative decoding with draft model is not supported yet. Please consider using other speculative decoding methods such as ngram, medusa, eagle, or deepseek_mtp.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#22047 [Doc] Added warning of speculating with draft model

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_de...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: speculative decoding not implemented error bug;stale ### Your current environment ### 🐛 Describe the bug Following the speculative decoding example provided in the [docs](url), I run into a NotImplemented error....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: p.` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: --host 0.0.0.0 \ --port 8000 \ --download-dir $home_path \ --model facebook/opt-6.7b \ --seed 42 \ -tp 1 \ --gpu_memory_utilization 0.8 \ --speculative_config '{"model": "facebook/opt-125m", "num_speculative_tokens": 5}...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error env_dependency #22047 [Doc] Added warning of speculating with draft model Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#22047](https://github.com/vllm-project/vllm/pull/22047) | mentioned | 0.6 | [Doc] Added warning of speculating with draft model | .md` and `examples` for a new model. ## Purpose According to [Issue #21797](https://github.com/vllm-project/vllm/issues/21797), speculating with a draft model is not supported in… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
