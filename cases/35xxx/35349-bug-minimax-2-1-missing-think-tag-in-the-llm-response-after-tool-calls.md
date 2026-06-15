# vllm-project/vllm#35349: [Bug]: MiniMax-2.1: Missing `<think>` tag in the LLM response after tool calls succeed.

| 字段 | 值 |
| --- | --- |
| Issue | [#35349](https://github.com/vllm-project/vllm/issues/35349) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MiniMax-2.1: Missing `<think>` tag in the LLM response after tool calls succeed.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug **Description** When using the reasoning parser with tool calls enabled, the tag is missing in the LLM response after a tool call successfully returns. This causes the reasoning segment following the tool result to appear without the wrapper. **Current Behavior** The response flow currently looks like this: ``` user ↓ reasoning ↓ tool_call ↓ tool_result ↓ reasoning ↓ response ``` After the tool result is returned, the model continues generating reasoning content, but the opening tag is missing. **Expected Behavior** The reasoning after the tool result should be wrapped with a new block: ``` user ↓ reasoning ↓ tool_call ↓ tool_result ↓ reasoning ↓ response ``` This would keep the reasoning structure consistent and easier to parse. **Reproduction** The model server is started with the following command: ```shell CUDA_VISIBLE_DEVICES=3,4,5,6 python3 -m vllm.entrypoints.openai.api_server \ --model MiniMax/MiniMax-M2.1 \ --trust-remote-code \ --tensor-parallel-size 4 \ --enable-auto-tool-choice \ --tool-call-parser minimax_m2 \ --max-model-len 100000 \ --reasoning-parser minimax_m2_append_think ``` ```python from openai import OpenAI...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: \ --reasoning-parser minimax_m2_append_think ``` ```python from openai import OpenAI client = OpenAI( base_url="http://localhost:8000/v1", api_key=" " ) resp = client.chat.completions.create( model="MiniMax/MiniMax-M2.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: tion** The model server is started with the following command: ```shell CUDA_VISIBLE_DEVICES=3,4,5,6 python3 -m vllm.entrypoints.openai.api_server \ --model MiniMax/MiniMax-M2.1 \ --trust-remote-code \ --tensor-parallel...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: or** The reasoning after the tool result should be wrapped with a new block: ``` user ↓ reasoning ↓ tool_call ↓ tool_result ↓ reasoning ↓ response ``` This would keep the reasoning structure consistent and easier to par...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: porting;model_support;sampling_logits;speculative_decoding cuda;sampling;triton build_error;nan_inf env_dependency;memory_layout Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ult ↓ reasoning ↓ response ``` After the tool result is returned, the model continues generating reasoning content, but the opening tag is missing. **Expected Behavior** The reasoning after the tool result should be wra...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
