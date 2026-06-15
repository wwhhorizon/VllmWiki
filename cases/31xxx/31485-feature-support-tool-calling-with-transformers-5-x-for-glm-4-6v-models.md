# vllm-project/vllm#31485: [Feature]: Support Tool Calling with transformers 5.x for GLM-4.6V Models

| 字段 | 值 |
| --- | --- |
| Issue | [#31485](https://github.com/vllm-project/vllm/issues/31485) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;model_support;multimodal_vlm;quantization |
| 子分类 | install |
| Operator 关键词 | fp8;gemm |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support Tool Calling with transformers 5.x for GLM-4.6V Models

### Issue 正文摘录

### 🚀 The feature, motivation and pitch Sorry but please allow me to use some AI to summary my findings and request **Request:** Add support for tool calling (`glm45` parser) when using transformers 5.x with GLM-4.6V models. **Current Limitation:** GLM-4.6V models require transformers 5.0.0rc1 for vision/multimodal support, but vLLM v0.13's tool calling parser (`glm45`) is incompatible with transformers 5.x, forcing users to choose between tool calling OR vision. ## Environment - **vLLM Version:** v0.13.0 - **Model:** `zai-org/GLM-4.6V-FP8`, `zai-org/GLM-4.6V-Flash` - **Transformers 4.56.0:** Tool calling works, vision not supported - **Transformers 5.0.0rc1:** Vision works, tool calling broken - **Tool Call Parser:** `glm45` - **GPU:** 2x NVIDIA RTX 6000 Pro (96GB each) ## Current Behavior ### With transformers 4.56.0 (Tool Calling Works) ```bash vllm serve zai-org/GLM-4.6V-FP8 \ --tool-call-parser glm45 \ --limit-mm-per-prompt '{"image": 0, "video": 0}' ``` Response includes `tool_calls`: ```json { "choices": [{ "message": { "tool_calls": [{ "id": "call_abc", "function": { "name": "get_weather", "arguments": "{\"location\": \"Tokyo\"}" } }] } }] } ``` ### With transformers 5.0.0...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: tool calling parser (`glm45`) is incompatible with transformers 5.x, forcing users to choose between tool calling OR vision. ## Environment - **vLLM Version:** v0.13.0 - **Model:** `zai-org/GLM-4.6V-FP8`, `zai-org/GLM-4...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: Environment - **vLLM Version:** v0.13.0 - **Model:** `zai-org/GLM-4.6V-FP8`, `zai-org/GLM-4.6V-Flash` - **Transformers 4.56.0:** Tool calling works, vision not supported - **Transformers 5.0.0rc1:** Vision works, tool c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Feature]: Support Tool Calling with transformers 5.x for GLM-4.6V Models feature request ### 🚀 The feature, motivation and pitch Sorry but please allow me to use some AI to summary my findings and request **Request:**...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tool calling broken - **Tool Call Parser:** `glm45` - **GPU:** 2x NVIDIA RTX 6000 Pro (96GB each) ## Current Behavior ### With transformers 4.56.0 (Tool Calling Works) ```bash vllm serve zai-org/GLM-4.6V-FP8 \ --tool-ca...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ment ci_build;frontend_api;model_support;multimodal_vlm;quantization fp8;gemm dtype 🚀 The feature, motivation and pitch

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
