# vllm-project/vllm#30595: [Bug]: Unsatisfiable testing dependencies

| 字段 | 值 |
| --- | --- |
| Issue | [#30595](https://github.com/vllm-project/vllm/issues/30595) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unsatisfiable testing dependencies

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug The ``model-hosting-container-standards>=0.1.9`` introduced in [f8151b66fa23f79c470d639f34768eb37709df0a](https://github.com/vllm-project/vllm/pull/29335) is causing dependency errors: ```uv pip install -r requirements/common.txt -r requirements/dev.txt --torch-backend=auto × No solution found when resolving dependencies: ╰─▶ Because model-hosting-container-standards>=0.1.9 depends on starlette>=0.49.1 and only the following versions of model-hosting-container-standards are available: model-hosting-container-standards =0.1.9 depends on starlette>=0.49.1. And because you require model-hosting-container-standards>=0.1.9 and starlette==0.46.2, we can conclude that your requirements are unsatisfiable. ``` ``` × No solution found when resolving dependencies: ╰─▶ Because only the following versions of fastapi[standard] are available: fastapi[standard] =0.40.0, 0.116.0, 0.124.3 , all of: starlette =0.48.0 , fastapi[standard]>=0.115.0, =0.1.9 depends on starlette>=0.49.1, we can conclude that all of: fastapi 0.116.0, 0.124.3 , model-hosting-container-standards>=0.1.9, fastapi[standard]>=0.115.0, =0.115.0, we can conclude that your requir...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: [Bug]: Unsatisfiable testing dependencies bug ### Your current environment ### 🐛 Describe the bug The ``model-hosting-container-standards>=0.1.9`` introduced in [f8151b66fa23f79c470d639f34768eb37709df0a](https://github....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: v pip install -r requirements/common.txt -r requirements/dev.txt --torch-backend=auto × No solution found when resolving dependencies: ╰─▶ Because model-hosting-container-standards>=0.1.9 depends on starlette>=0.49.1 an...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cuda;operator;quantization;sampling;triton build_error;nan_inf env_dependency Your current envir...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ncies bug ### Your current environment ### 🐛 Describe the bug The ``model-hosting-container-standards>=0.1.9`` introduced in [f8151b66fa23f79c470d639f34768eb37709df0a](https://github.com/vllm-project/vllm/pull/29335) is...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
