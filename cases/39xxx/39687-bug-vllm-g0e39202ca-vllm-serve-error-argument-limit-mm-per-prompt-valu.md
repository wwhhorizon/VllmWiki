# vllm-project/vllm#39687: [Bug]: vllm(g0e39202ca) vllm serve: error: argument --limit-mm-per-prompt: Value image=4,audio=1 cannot be converted to <function

| 字段 | 值 |
| --- | --- |
| Issue | [#39687](https://github.com/vllm-project/vllm/issues/39687) |
| 状态 | open |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;gemm;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm(g0e39202ca) vllm serve: error: argument --limit-mm-per-prompt: Value image=4,audio=1 cannot be converted to <function

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I run the following command by following docs https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#full-featured-server-launch command and error message: ``` $ VLLM_USE_MODELSCOPE=true \ vllm serve RedHatAI/gemma-4-31B-it-FP8_BLOCK \ --port 8000 \ --tensor-parallel-size 4 \ --max-model-len 120000 \ --reasoning-parser gemma4 \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.93 \ --limit-mm-per-prompt image=4,audio=1 \ --max-num-seqs 1 usage: vllm serve [model_tag] [options] vllm serve: error: argument --limit-mm-per-prompt: Value image=4,audio=1 cannot be converted to . ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 现有链接修复摘要

#39802 [Frontend] Improve parse_type error message for JSON dict CLI args

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: the following command by following docs https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#full-featured-server-launch command and error message: ``` $ VLLM_USE_MODELSCOPE=true \ vllm serve RedHatAI/gemm...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: age: ``` $ VLLM_USE_MODELSCOPE=true \ vllm serve RedHatAI/gemma-4-31B-it-FP8_BLOCK \ --port 8000 \ --tensor-parallel-size 4 \ --max-model-len 120000 \ --reasoning-parser gemma4 \ --enable-auto-tool-choice \ --tool-call-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: by following docs https://docs.vllm.ai/projects/recipes/en/latest/Google/Gemma4.html#full-featured-server-launch command and error message: ``` $ VLLM_USE_MODELSCOPE=true \ vllm serve RedHatAI/gemma-4-31B-it-FP8_BLOCK \...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ion;sampling_logits;speculative_decoding cuda;fp8;gemm;operator;sampling;triton build_error;nan_inf dtype;env_dependency #39802 [Frontend] Improve parse_type error message for JSON dict CLI args Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39802](https://github.com/vllm-project/vllm/pull/39802) | closes_keyword | 0.95 | [Frontend] Improve parse_type error message for JSON dict CLI args | Fixes #39687. When a dict-typed CLI argument such as `--limit-mm-per-prompt` receives an invalid value (e.g. the legacy `key=val,key=val` form that was removed in #20969), `parse_ |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
