# vllm-project/vllm#37079: [Bug]: Native Tool Calling collapses reasoning quality when any Tool/Function/Filter is enabled (vLLM auto-tool-choice backend)

| 字段 | 值 |
| --- | --- |
| Issue | [#37079](https://github.com/vllm-project/vllm/issues/37079) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Native Tool Calling collapses reasoning quality when any Tool/Function/Filter is enabled (vLLM auto-tool-choice backend)

### Issue 正文摘录

### Summary When `Native Tool Calling` is enabled in OpenWebUI, reasoning quality drops sharply as soon as **any** Tool, Function, or Filter is active in OWUI, even if no tool is actually needed for the prompt. This appears to be a request-shaping issue in OWUI native tool mode, vllm jinjia 2 or Qwen3.5 tokenizer_config. likely related to payload construction and/or tool schema injection, rather than a model-only issue. Test date: March 14, 2026. ### Environment - OpenWebUI version: [please fill from `/_app/version.json`] - Deployment: Docker - Backend: vLLM OpenAI-compatible API - vLLM image: `vllm/vllm-openai:v0.17.1-cu130` - Docker Compose version: `v5.0.2` - Main model: `Kbenkhaled/Qwen3.5-27B-NVFP4` - Reasoning parser: `qwen3` - Tool parser tested: `qwen3_coder`, `hermes` - Native Tool Calling in OWUI: enabled during failing runs vLLM command used in the failing mode: ```yaml command: - Kbenkhaled/Qwen3.5-27B-NVFP4 // or Qwen/Qwen3.5-27B - --host - "0.0.0.0" - --max-model-len - "100000" - --reasoning-parser - qwen3 - --enable-auto-tool-choice - --tool-call-parser - qwen3_coder - --gpu-memory-utilization - "0.50" - --max-cudagraph-capture-size - "256" ``` Also tested with `--t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: el-only issue. Test date: March 14, 2026. ### Environment - OpenWebUI version: [please fill from `/_app/version.json`] - Deployment: Docker - Backend: vLLM OpenAI-compatible API - vLLM image: `vllm/vllm-openai:v0.17.1-c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to be a request-shaping issue in OWUI native tool mode, vllm jinjia 2 or Qwen3.5 tokenizer_config. likely related to payload construction and/or tool schema injection, rather than a model-only issue. Test date: March 14...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: - Docker Compose version: `v5.0.2` - Main model: `Kbenkhaled/Qwen3.5-27B-NVFP4` - Reasoning parser: `qwen3` - Tool parser tested: `qwen3_coder`, `hermes` - Native Tool Calling in OWUI: enabled during failing runs vLLM c...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: d/or tool schema injection, rather than a model-only issue. Test date: March 14, 2026. ### Environment - OpenWebUI version: [please fill from `/_app/version.json`] - Deployment: Docker - Backend: vLLM OpenAI-compatible...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: quality when any Tool/Function/Filter is enabled (vLLM auto-tool-choice backend) bug ### Summary When `Native Tool Calling` is enabled in OpenWebUI, reasoning quality drops sharply as soon as **any** Tool, Function, or...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
