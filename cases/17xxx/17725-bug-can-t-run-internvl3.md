# vllm-project/vllm#17725: [Bug]: Can't run InternVL3

| 字段 | 值 |
| --- | --- |
| Issue | [#17725](https://github.com/vllm-project/vllm/issues/17725) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;quantization;sampling |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Can't run InternVL3

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I've runned model in k8s cluster and recive error ``` KeyError: 'model.layers.0.attention.wqkv.qweight' ``` Also issues in Intern repo - https://github.com/OpenGVLab/InternVL/issues/1021 - https://github.com/OpenGVLab/InternVL/issues/1004 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Can't run InternVL3 bug ### Your current environment ### 🐛 Describe the bug I've runned model in k8s cluster and recive error ``` KeyError: 'model.layers.0.attention.wqkv.qweight' ``` Also issues in Intern repo -...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: nment ### 🐛 Describe the bug I've runned model in k8s cluster and recive error ``` KeyError: 'model.layers.0.attention.wqkv.qweight' ``` Also issues in Intern repo - https://github.com/OpenGVLab/InternVL/issues/1021 - h...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: _kv_cache;distributed_parallel;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;cuda;quantization;sampling crash;slowdown dtype;env_dependency Your current environment
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 004 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: l;frontend_api;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory attention;cuda;quantization;sampling crash;slowdown dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
