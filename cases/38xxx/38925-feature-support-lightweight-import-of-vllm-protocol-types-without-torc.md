# vllm-project/vllm#38925: [Feature]: Support lightweight import of vllm protocol types without torch dependency

| 字段 | 值 |
| --- | --- |
| Issue | [#38925](https://github.com/vllm-project/vllm/issues/38925) |
| 状态 | open |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | cold_start |
| Operator 关键词 | cuda;triton |
| 症状 | crash |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Feature]: Support lightweight import of vllm protocol types without torch dependency

### Issue 正文摘录

## Motivation Projects in the llm-d ecosystem (and likely others) need to import vllm protocol types, config dataclasses, and rendering utilities but do **not** run inference. For example, the [llm-d-kv-cache UDS tokenizer service](https://github.com/llm-d/llm-d-kv-cache/tree/main/services/uds_tokenizer) is a lightweight gRPC sidecar that only imports: ```python from vllm.config import VllmConfig from vllm.config.device import DeviceConfig from vllm.engine.arg_utils import AsyncEngineArgs from vllm.entrypoints.openai.chat_completion.protocol import ChatCompletionRequest from vllm.entrypoints.openai.completion.protocol import CompletionRequest from vllm.entrypoints.openai.engine.protocol import ErrorResponse from vllm.entrypoints.openai.models.protocol import BaseModelPath from vllm.entrypoints.openai.models.serving import OpenAIModelRegistry from vllm.entrypoints.openai.engine.serve.render.serving import OpenAIServingRender from vllm.plugins.io_processors import get_io_processor from vllm.renderers import renderer_from_config ``` These are pure Python pydantic models, dataclasses, and rendering logic. No GPU, no CUDA, no inference engine. ## Problem Any `from vllm. import ...` tri...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: [Feature]: Support lightweight import of vllm protocol types without torch dependency ## Motivation Projects in the llm-d ecosystem (and likely others) need to import vllm protocol types, config dataclasses, and renderi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: rts crash without torch 3. **The full vllm dep tree** (torch, CUDA libs, triton, flashinfer, nvidia-*, etc.) must be installed even in lightweight sidecars that never touch a GPU Additionally, even beyond `env_override....
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ure Python pydantic models, dataclasses, and rendering logic. No GPU, no CUDA, no inference engine. ## Problem Any `from vllm. import ...` triggers this import chain: ``` vllm/__init__.py (line 14) -> import vllm.env_ov...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: llm-d ecosystem (and likely others) need to import vllm protocol types, config dataclasses, and rendering utilities but do **not** run inference. For example, the [llm-d-kv-cache UDS tokenizer service](https://github.co...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: ad of `__init__.py`**: more invasive, touches more files, higher risk of regressions. - **`VLLM_NO_TORCH` environment variable**: explicit opt-out, but adds a knob users have to discover. The guard approach is minimal,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
