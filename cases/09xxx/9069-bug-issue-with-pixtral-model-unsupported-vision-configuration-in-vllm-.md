# vllm-project/vllm#9069: [Bug]: Issue with Pixtral Model: Unsupported Vision Configuration in vLLM ( AMD amd 7900 xtx)

| 字段 | 值 |
| --- | --- |
| Issue | [#9069](https://github.com/vllm-project/vllm/issues/9069) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization |
| 子分类 | memory |
| Operator 关键词 | cache;cuda;kernel;operator;quantization |
| 症状 | build_error;crash;oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue with Pixtral Model: Unsupported Vision Configuration in vLLM ( AMD amd 7900 xtx)

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#9036 [Model] Support Pixtral models in the HF Transformers format

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Issue with Pixtral Model: Unsupported Vision Configuration in vLLM ( AMD amd 7900 xtx) bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ### Before submitting a new issue...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization cache;cuda;kernel;operator;quantization buil...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: uted_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization cache;cuda;kernel;operator;quantization build_error;crash;oom dtype;env_dependency;memory_layout #9036 [Model] Support Pixtral models...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: m;quantization cache;cuda;kernel;operator;quantization build_error;crash;oom dtype;env_dependency;memory_layout #9036 [Model] Support Pixtral models in the HF Transformers format Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#9036](https://github.com/vllm-project/vllm/pull/9036) | closes_keyword | 0.95 | [Model] Support Pixtral models in the HF Transformers format | FIX #9069 Introduces `PixtralHF`, which is a model implementing HF's format of Pixtral. Based off https://github.com/huggingface/transformers/blob/main/src/transformers/models/p |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
