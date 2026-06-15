# vllm-project/vllm#15636: [Bug]: Outlines broken on vLLM 0.8+

| 字段 | 值 |
| --- | --- |
| Issue | [#15636](https://github.com/vllm-project/vllm/issues/15636) |
| 状态 | closed |
| 标签 | bug;structured-output;unstale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Outlines broken on vLLM 0.8+

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Please see the downstream issue in Outlines for additional context: https://github.com/dottxt-ai/outlines/issues/1517. Essentially, I am getting the error ``` ValueError: vLLM V1 does not support per request user provided logits processors. ``` even though I am on vLLM 0.8. I'm curious why I'm getting a vLLM v1-related error message on a non-v1 tag? MWE: ```python from outlines import models, generate from pydantic import BaseModel model = models.vllm("microsoft/Phi-3-mini-4k-instruct") class Example(BaseModel): name: str description: str prompt = "France: " generator = generate.json(model, Example) response = generator(prompt) print(response) ``` Requirements: ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: v1-related error message on a non-v1 tag? MWE: ```python from outlines import models, generate from pydantic import BaseModel model = models.vllm("microsoft/Phi-3-mini-4k-instruct") class Example(BaseModel): name: str d...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: ention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits attention;cache;cuda;quantization;sampling;triton build_error;crash dtype;env_dependency;shape Your current environme...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: : ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), whic...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Outlines broken on vLLM 0.8+ bug;structured-output;unstale ### Your current environment ### 🐛 Describe the bug Please see the downstream issue in Outlines for additional context: https://github.com/dottxt-ai/outl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ;quantization;sampling_logits attention;cache;cuda;quantization;sampling;triton build_error;crash dtype;env_dependency;shape Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
