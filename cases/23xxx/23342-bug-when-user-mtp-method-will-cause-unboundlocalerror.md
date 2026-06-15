# vllm-project/vllm#23342: [Bug]: when user MTP method will cause UnboundLocalError

| 字段 | 值 |
| --- | --- |
| Issue | [#23342](https://github.com/vllm-project/vllm/issues/23342) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: when user MTP method will cause UnboundLocalError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When use the following command starts MTP service，error occurred: ``` VLLM_USE_V1=1 \ python -m vllm.entrypoints.openai.api_server \ --port 8500 \ --dtype bfloat16 \ --trust-remote-code \ --model baidu/ERNIE-4.5-21B-A3B-PT \ --served-model-name ERNIE-4.5-21B \ --speculative-config '{"method": "ernie_mtp","model": "/root/paddlejob/zhouchong/ERNIE-4.5-21B-A3B-PT" ,"num_speculative_tokens": 1}' ``` it because when use mtp method, "hidden_states" is not defined ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;model_support;speculative_decoding cuda build_error dtype;env_dependency Your current environment
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ python -m vllm.entrypoints.openai.api_server \ --port 8500 \ --dtype bfloat16 \ --trust-remote-code \ --model baidu/ERNIE-4.5-21B-A3B-PT \ --served-model-name ERNIE-4.5-21B \ --speculative-config '{"method": "ernie_mt...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: --port 8500 \ --dtype bfloat16 \ --trust-remote-code \ --model baidu/ERNIE-4.5-21B-A3B-PT \ --served-model-name ERNIE-4.5-21B \ --speculative-config '{"method": "ernie_mtp","model": "/root/paddlejob/zhouchong/ERNIE-4.5-...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: when user MTP method will cause UnboundLocalError bug;stale ### Your current environment ### 🐛 Describe the bug When use the following command starts MTP service，error occurred: ``` VLLM_USE_V1=1 \ python -m vllm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
