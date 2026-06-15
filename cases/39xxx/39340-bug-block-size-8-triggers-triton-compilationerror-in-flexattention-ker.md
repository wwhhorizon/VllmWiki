# vllm-project/vllm#39340: [Bug]: `block_size=8` triggers Triton CompilationError in FlexAttention kernel; other backends correctly reject

| 字段 | 值 |
| --- | --- |
| Issue | [#39340](https://github.com/vllm-project/vllm/issues/39340) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: `block_size=8` triggers Triton CompilationError in FlexAttention kernel; other backends correctly reject

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `block_size=8` causes vLLM to select FLEX_ATTENTION (without the user requesting it). Init succeeds. The first `generate()` crashes. The EngineCore stderr shows `torch._inductor.exc.InductorError: CompilationError` deep inside the FlexAttention `forward_inner` Triton kernel. In addition, FLASH_ATTN, TRITON_ATTN, FLASHINFER all reject `block_size=8` cleanly with a `ValueError` at backend selection time. FLEX_ATTENTION silently accepts it and crashes later in Triton codegen. ### Reproduce ```python import vllm llm = vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, block_size=8, ) llm.generate(["hello"], vllm.SamplingParams(max_tokens=1)) ``` EngineCore stderr: ``` torch._inductor.exc.InductorError: CompilationError: at 146:20: ... acc, l_i, m_i = forward_inner( ^ ``` ### Expected `LLM(...)` raises `ValueError` at construction time when `block_size` is below the FlexAttention kernel's minimum. For example, add a `block_size >= {minimal value}` to the flexattention backend selector. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corn...

## 现有链接修复摘要

#39385 [Bugfix] Validate block_size in FlexAttention at construction time | #39807 [Bugfix] FlexAttention: reject block_size < 16

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ccepts it and crashes later in Triton codegen. ### Reproduce ```python import vllm llm = vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, block_size=8, ) llm.generate(["hello"], vllm.SamplingParams(max_tokens=1)) `...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: `block_size=8` triggers Triton CompilationError in FlexAttention kernel; other backends correctly reject bug ### Your current environment ### 🐛 Describe the bug `block_size=8` causes vLLM to select FLEX_ATTENTION...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: or. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: iton codegen. ### Reproduce ```python import vllm llm = vllm.LLM( model="Qwen/Qwen3-0.6B", max_model_len=512, block_size=8, ) llm.generate(["hello"], vllm.SamplingParams(max_tokens=1)) ``` EngineCore stderr: ``` torch._...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: g `block_size=8` causes vLLM to select FLEX_ATTENTION (without the user requesting it). Init succeeds. The first `generate()` crashes. The EngineCore stderr shows `torch._inductor.exc.InductorError: CompilationError` de...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39385](https://github.com/vllm-project/vllm/pull/39385) | closes_keyword | 0.95 | [Bugfix] Validate block_size in FlexAttention at construction time | Fixes #39340 ## Test plan - `LLM(model="Qwen/Qwen3-0.6B", max_model_len=512, block_size=8)` with FlexAttention selected should now raise `ValueError` at construction with a clear |
| [#39807](https://github.com/vllm-project/vllm/pull/39807) | closes_keyword | 0.95 | [Bugfix] FlexAttention: reject block_size < 16 | Fixes #39340 ## Duplicate check - `gh issue view 39340 --comments` — no one has claimed this issue, no in-progress work. - `gh pr list --state open --search "39340 in:body"` — |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
