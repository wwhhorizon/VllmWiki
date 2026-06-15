# vllm-project/vllm#35464: [Bug]: Fix GLM-OCR text_config model_type handling

| 字段 | 值 |
| --- | --- |
| Issue | [#35464](https://github.com/vllm-project/vllm/issues/35464) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Fix GLM-OCR text_config model_type handling

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Fix GLM-OCR config parsing: Avoid duplicate model_type kwargs when instantiating sub-configs Replace invalid chatglm fallback with glm_ocr_text, matching model config and vLLM registry Code diff (core idea) Diff Copy code diff --git a/vllm/transformers_utils/configs/glm_ocr.py b/vllm/transformers_utils/configs/glm_ocr.py @@ -75,8 +75,9 @@ class GlmOcrConfig(PretrainedConfig): if isinstance(text_config, dict): from transformers import AutoConfig - model_type = text_config.get("model_type", "chatglm") - self.text_config = AutoConfig.for_model(model_type, **text_config) + text_config = dict(text_config) + model_type = text_config.pop("model_type", "glm_ocr_text") + self.text_config = AutoConfig.for_model(model_type, **text_config) elif text_config is None: from transformers import AutoConfig - self.text_config = AutoConfig.for_model("chatglm") + self.text_config = AutoConfig.for_model("glm_ocr_text") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots o...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: if isinstance(text_config, dict): from transformers import AutoConfig - model_type = text_config.get("model_type", "chatglm") - self.text_config = AutoConfig.for_model(model_type, **text_config) + text_config = dict(tex...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: model_type kwargs when instantiating sub-configs Replace invalid chatglm fallback with glm_ocr_text, matching model config and vLLM registry Code diff (core idea) Diff Copy code diff --git a/vllm/transformers_utils/conf...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: t") ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Fix GLM-OCR text_config model_type handling bug;stale ### Your current environment ### 🐛 Describe the bug Fix GLM-OCR config parsing: Avoid duplicate model_type kwargs when instantiating sub-configs Replace inval...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: Fix GLM-OCR text_config model_type handling bug;stale ### Your current environment ### 🐛 Describe the bug Fix GLM-OCR config parsing: Avoid duplicate model_type kwargs when instantiating sub-configs Replace inval...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
