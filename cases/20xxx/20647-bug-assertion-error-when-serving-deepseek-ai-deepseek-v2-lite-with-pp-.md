# vllm-project/vllm#20647: [Bug]: Assertion error when serving "deepseek-ai/DeepSeek-V2-Lite" with PP in 0.9.2

| 字段 | 值 |
| --- | --- |
| Issue | [#20647](https://github.com/vllm-project/vllm/issues/20647) |
| 状态 | closed |
| 标签 | bug;v1;deepseek |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Assertion error when serving "deepseek-ai/DeepSeek-V2-Lite" with PP in 0.9.2

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```bash uv pip install "vllm==0.9.2" vllm serve deepseek-ai/DeepSeek-V2-Lite \ --trust-remote-code \ --max-model-len=1024 --enforce-eager \ --tensor-parallel-size=2 --pipeline-parallel-size=2 # PP>1 causes error ``` exception: ``` (VllmWorker rank=0 pid=20455) ERROR 07-08 15:41:43 [multiproc_executor.py:487] File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/model_executor/model_loader/utils.py", l ine 64, in initialize_model (VllmWorker rank=0 pid=20455) ERROR 07-08 15:41:43 [multiproc_executor.py:487] return model_class(vllm_config=vllm_config, prefix=prefix) (VllmWorker rank=0 pid=20455) ERROR 07-08 15:41:43 [multiproc_executor.py:487] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (VllmWorker rank=0 pid=20455) ERROR 07-08 15:41:43 [multiproc_executor.py:487] File "/home/ray/anaconda3/lib/python3.11/site-packages/vllm/model_executor/models/deepseek_v2.py", l ine 743, in __init__ (VllmWorker rank=0 pid=20455) ERROR 07-08 15:41:43 [multiproc_executor.py:487] assert isinstance(layer, DeepseekV2DecoderLayer) ``` and `type(layer)` is ` ` likely caused by https://github.com/vllm-project/vllm/pull/18343 ### Before submi...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ### Your current environment ### 🐛 Describe the bug ```bash uv pip install "vllm==0.9.2" vllm serve deepseek-ai/DeepSeek-V2-Lite \ --trust-remote-code \ --max-model-len=1024 --enforce-eager \ --tensor-parallel-size=2 --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 343 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm serve deepseek-ai/DeepSeek-V2-Lite \ --trust-remote-code \ --max-model-len=1024 --enforce-eager \ --tensor-parallel-size=2 --pipeline-parallel-size=2 # PP>1 causes error ``` exception: ``` (VllmWorker rank=0 pid=204...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: 41:43 [multiproc_executor.py:487] assert isinstance(layer, DeepseekV2DecoderLayer) ``` and `type(layer)` is ` ` likely caused by https://github.com/vllm-project/vllm/pull/18343 ### Before submitting a new issue... - [x]...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;nan_inf env_dependency Your current environment

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
