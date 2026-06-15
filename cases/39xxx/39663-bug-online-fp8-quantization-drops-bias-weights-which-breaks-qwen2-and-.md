# vllm-project/vllm#39663: [Bug]: Online FP8 quantization drops bias weights, which breaks Qwen2 and other models with bias=True

| 字段 | 值 |
| --- | --- |
| Issue | [#39663](https://github.com/vllm-project/vllm/issues/39663) |
| 状态 | open |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;quantization;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Online FP8 quantization drops bias weights, which breaks Qwen2 and other models with bias=True

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When using `--quantization fp8` on a BF16 checkpoint, models with `bias=True` on their linear layers produce garbage. The bias tensors silently fail to load and stay at zero. Qwen2/2.5 is the most visible case since it has `bias=True` on qkv_proj, but this hits any architecture with biased linears (GPT-2, Phi, etc.). **Reproduction** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen2.5-0.5B-Instruct", quantization="fp8", dtype="bfloat16", enforce_eager=True) out = llm.generate(["What is the capital of France?"], SamplingParams(max_tokens=20, temperature=0)) print(out[0].outputs[0].text) # Outputs: "vpn.lua之心_burg.numpy" or similar garbage # Remove quantization="fp8" and it works fine. ``` **Root cause** `initialize_online_processing` in `model_loader/reload/layerwise.py` wraps the weight loader for every tensor not in `SKIP_TENSORS`. Since `"bias"` isn't in that set, the bias parameter's loader gets wrapped by `make_online_process_loader`, which buffers it into the deferred loading pipeline. The bias never gets written to the layer: it stays at zero. Same class of bug as #37334 and #38746 . **Fix** Add `"bias"`...

## 现有链接修复摘要

#37334 [BUG] Exclude SKIP_TENSORS from get_layer_size() + new weight sync example for dpep | #39665 [Bugfix] Skip bias tensors in online FP8 quantization pipeline | #39666 [Bugfix] Add bias to SKIP_TENSORS to fix online FP8 for models with biased linears | #39962 [Bugfix] Skip bias tensors in online FP8 quantization pipeline

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: Online FP8 quantization drops bias weights, which breaks Qwen2 and other models with bias=True bug ### Your current environment ### 🐛 Describe the bug When using `--quantization fp8` on a BF16 checkpoint, models...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: iased linears (GPT-2, Phi, etc.). **Reproduction** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen2.5-0.5B-Instruct", quantization="fp8", dtype="bfloat16", enforce_eager=True) out = llm.generate(["Wh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ost visible case since it has `bias=True` on qkv_proj, but this hits any architecture with biased linears (GPT-2, Phi, etc.). **Reproduction** ```python from vllm import LLM, SamplingParams llm = LLM("Qwen/Qwen2.5-0.5B-...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Online FP8 quantization drops bias weights, which breaks Qwen2 and other models with bias=True bug ### Your current environment ### 🐛 Describe the bug When using `--quantization fp8` on a BF16 checkpoint, models...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ling_logits;speculative_decoding cuda;fp8;operator;quantization;sampling;triton build_error;nan_inf dtype;env_dependency #37334 [BUG] Exclude SKIP_TENSORS from get_layer_size() + new weight sync example for dpep | #3966...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#37334](https://github.com/vllm-project/vllm/pull/37334) | mentioned | 0.45 | [BUG] Exclude SKIP_TENSORS from get_layer_size() + new weight sync example for dpep | er gets written to the layer: it stays at zero. same class of bug as #37334 and #38746 . **fix** add `"bias"` to `skip_tensors` in `vllm/model_executor/model_loader/reload/meta.py… |
| [#39665](https://github.com/vllm-project/vllm/pull/39665) | closes_keyword | 0.95 | [Bugfix] Skip bias tensors in online FP8 quantization pipeline | Fixes #39663 |
| [#39666](https://github.com/vllm-project/vllm/pull/39666) | closes_keyword | 0.95 | [Bugfix] Add bias to SKIP_TENSORS to fix online FP8 for models with biased linears | Fixes #39663. Likely related to #27364 and #24025. ## Test Plan ```bash python -m pytest tests/quantization/test_fp8.py::test_fp8_online_bias_model -xvs ``` New integrat |
| [#39962](https://github.com/vllm-project/vllm/pull/39962) | closes_keyword | 0.95 | [Bugfix] Skip bias tensors in online FP8 quantization pipeline | Fixes #39663. Resubmit of #39665 (auto-closed by my notification cleanup without maintainer review). ## Problem With `--quantization fp8` on BF16 checkpoints, models that registe |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
