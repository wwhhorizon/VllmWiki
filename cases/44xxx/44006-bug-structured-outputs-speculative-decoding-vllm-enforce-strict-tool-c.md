# vllm-project/vllm#44006: [Bug]: [structured outputs] speculative decoding + `VLLM_ENFORCE_STRICT_TOOL_CALLING=1` failed to advance FSM

| 字段 | 值 |
| --- | --- |
| Issue | [#44006](https://github.com/vllm-project/vllm/issues/44006) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;moe;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [structured outputs] speculative decoding + `VLLM_ENFORCE_STRICT_TOOL_CALLING=1` failed to advance FSM

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When xgrammar's strict tool calling mode (`VLLM_ENFORCE_STRICT_TOOL_CALLING=1`) is set along with speculative decoding, it often errors out with 500 internal server error for any tool call request. ## Reproducer I have used qwen3.5 here, but deepseek v4 w/ mtp on would also suffer the same error. ```shell export VLLM_ENFORCE_STRICT_TOOL_CALLING=1 vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --reasoning-parser qwen3 \ --enable-auto-tool-choice \ --tool-call-parser qwen3_coder \ --enable-log-requests ``` Then we just need to send any tool calling payload - for Qwen3.5 xgrammar state advance failure raises for ~40% of time, if it does not raise at once try several times. ```python client = OpenAI(max_retries=0) tool_list = [ { "type": "function", "function": { "name": "get_weather", "description": "현재 날씨 정보를 가져옵니다", "parameters": { "type": "object", "properties": { "location": { "type": "string", "description": "한국어로 된 도시 이름, 예: '서울', '부산', '뉴욕'", }, "unit": { "type": "string", "enum": ["celsius", "fahre...

## 现有链接修复摘要

#44392 [Bugfix][Core] Filter reasoning boundary tokens before structured-output FSM advance

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: rnal server error for any tool call request. ## Reproducer I have used qwen3.5 here, but deepseek v4 w/ mtp on would also suffer the same error. ```shell export VLLM_ENFORCE_STRICT_TOOL_CALLING=1 vllm serve Qwen/Qwen3.5...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: okens=261710, min_tokens=0, logprobs=None, prompt_logprobs=None, skip_special_tokens=True, spaces_between_special_tokens=True, structured_outputs=StructuredOutputsParams(json=None, regex=None, choice=None, grammar=None,...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ort VLLM_ENFORCE_STRICT_TOOL_CALLING=1 vllm serve Qwen/Qwen3.5-397B-A17B-FP8 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --re...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ative decoding + `VLLM_ENFORCE_STRICT_TOOL_CALLING=1` failed to advance FSM bug ### Your current environment ### 🐛 Describe the bug When xgrammar's strict tool calling mode (`VLLM_ENFORCE_STRICT_TOOL_CALLING=1`) is set...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: rve Qwen/Qwen3.5-397B-A17B-FP8 \ --tensor-parallel-size 8 \ --enable-expert-parallel \ --speculative-config.method mtp \ --speculative-config.num_speculative_tokens 1 \ --reasoning-parser qwen3 \ --enable-auto-tool-choi...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#44392](https://github.com/vllm-project/vllm/pull/44392) | closes_keyword | 0.95 | [Bugfix][Core] Filter reasoning boundary tokens before structured-output FSM advance | Fixes [#44006](https://github.com/vllm-project/vllm/issues/44006). When MTP speculative decoding, VLLM_ENFORCE_STRICT_TOOL_CALLING=1, and a reasoning model with tool calling are |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
