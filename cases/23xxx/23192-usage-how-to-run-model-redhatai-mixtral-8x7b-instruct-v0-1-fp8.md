# vllm-project/vllm#23192: [Usage]: How to run model - `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8`

| 字段 | 值 |
| --- | --- |
| Issue | [#23192](https://github.com/vllm-project/vllm/issues/23192) |
| 状态 | closed |
| 标签 | usage;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: How to run model - `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8`

### Issue 正文摘录

### Your current environment Using docker image - `vllm/vllm-openai:v0.9.1` ### How would you like to use vllm I'm trying to run `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8` on 8 H100 machine. Following is the command used: ``` vllm serve RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8 --port 8910 --host 0.0.0.0 --tensor-parallel-size 8 --served-model-name Mixtral-8x7B-Instruct-v0.1-FP8 --no-enable-prefix-caching ``` But I get the error: ``` ValueError: Free memory on device (5.31/79.18 GiB) on startup is less than desired GPU memory utilization (0.9, 71.26 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. ``` I've attached the complete log for your reference. Please tell me how to run this correctly. Thanks. [mixstral_8h100.log.txt](https://github.com/user-attachments/files/21860152/mixstral_8h100.log.txt) ### Edit: I get the same error while trying to run `nvidia/Llama-3.1-70B-Instruct-FP8`. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: -8x7B-Instruct-v0.1-FP8` usage;stale ### Your current environment Using docker image - `vllm/vllm-openai:v0.9.1` ### How would you like to use vllm I'm trying to run `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8` on 8 H100 m...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Usage]: How to run model - `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8` usage;stale ### Your current environment Using docker image - `vllm/vllm-openai:v0.9.1` ### How would you like to use vllm I'm trying to run `RedHatA...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: e vllm I'm trying to run `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8` on 8 H100 machine. Following is the command used: ``` vllm serve RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8 --port 8910 --host 0.0.0.0 --tensor-parallel-si...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Usage]: How to run model - `RedHatAI/Mixtral-8x7B-Instruct-v0.1-FP8` usage;stale ### Your current environment Using docker image - `vllm/vllm-openai:v0.9.1` ### How would you like to use vllm I'm trying to run `RedHatA...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: : Free memory on device (5.31/79.18 GiB) on startup is less than desired GPU memory utilization (0.9, 71.26 GiB). Decrease GPU memory utilization or reduce GPU memory used by other processes. ``` I've attached the compl...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
