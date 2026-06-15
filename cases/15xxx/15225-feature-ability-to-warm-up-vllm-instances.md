# vllm-project/vllm#15225: [Feature]: Ability to warm up vLLM instances

| 字段 | 值 |
| --- | --- |
| Issue | [#15225](https://github.com/vllm-project/vllm/issues/15225) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api |
| 子分类 | env_compat |
| Operator 关键词 | cuda |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Ability to warm up vLLM instances

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Starting a new vLLM instance can take a long time. A vLLM cold start (all caches cleared) can take up to 19s before initializing the device: (log trimmed for clarity) ``` $ vllm serve Qwen/Qwen2.5-1.5B-Instruct INFO 03-20 14:26:54 [__init__.py:256] Automatically detected platform cuda. INFO 03-20 14:26:55 [api_server.py:981] vLLM API server version 0.8.2.dev24+ge3f813c33 ... INFO 03-20 14:27:07 [utils.py:123] waiting for EngineCore to be initialized <---- added log ... INFO 03-20 14:27:13 [uniproc_executor.py:46] about to initialize device <---- added log ``` Processes creation, config initialization, python modules importation, all contributes to the relatively long starting time. It would be great if we could warm up vLLM instances to reduce the starting time when it is actually needed. The booting sequence can continue after a API call. ### Alternatives Start vLLM and call `/sleep`. This is less efficient and sometimes not possible when the GPU is fully utilized by another process. ### Additional context There are various scenarios for which this feature can useful. For instance we would like to scale up quickly the number of instances in...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: d platform cuda. INFO 03-20 14:26:55 [api_server.py:981] vLLM API server version 0.8.2.dev24+ge3f813c33 ... INFO 03-20 14:27:07 [utils.py:123] waiting for EngineCore to be initialized <---- added log ... INFO 03-20 14:2...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: t INFO 03-20 14:26:54 [__init__.py:256] Automatically detected platform cuda. INFO 03-20 14:26:55 [api_server.py:981] vLLM API server version 0.8.2.dev24+ge3f813c33 ... INFO 03-20 14:27:07 [utils.py:123] waiting for Eng...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: re initializing the device: (log trimmed for clarity) ``` $ vllm serve Qwen/Qwen2.5-1.5B-Instruct INFO 03-20 14:26:54 [__init__.py:256] Automatically detected platform cuda. INFO 03-20 14:26:55 [api_server.py:981] vLLM...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Feature]: Ability to warm up vLLM instances feature request;stale ### 🚀 The feature, motivation and pitch Starting a new vLLM instance can take a long time. A vLLM cold start (all caches cleared) can take up to 19s bef...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: enarios for which this feature can useful. For instance we would like to scale up quickly the number of instances in respond to a burst of requests. In the example above, 19s is a significant amount of time and in some...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
