# vllm-project/vllm#44200: [Bug]: Qwen3-VL EVS video pruning crashes with CPU/CUDA device mismatch in _create_final_video_embeddings

| 字段 | 值 |
| --- | --- |
| Issue | [#44200](https://github.com/vllm-project/vllm/issues/44200) |
| 状态 | open |
| 标签 |  |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | wrong_output |
| Operator 关键词 | cuda;sampling |
| 症状 | crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: Qwen3-VL EVS video pruning crashes with CPU/CUDA device mismatch in _create_final_video_embeddings

### Issue 正文摘录

### Your current environment - vLLM: `0.22.0` (release) - PyTorch: `2.11.0+cu130` - GPU: A800-80GB (also applies to A100 class) - Model: `Qwen/Qwen3-VL-4B-Instruct` ### 🐛 Describe the bug When serving **Qwen3-VL with `video_pruning_rate > 0`** (Efficient Video Sampling / EVS) and a **video** input, generation crashes during the multimodal encoder step with a CPU/CUDA device mismatch: ``` RuntimeError: Expected all tensors to be on the same device, but got index is on cpu, different from other tensors on cuda:0 (when checking argument in method wrapper_CUDA__index_select) ``` Traceback (abridged): ``` vllm/v1/worker/gpu_model_runner.py: _execute_mm_encoder -> model.embed_multimodal (qwen3_vl.py:2704) -> _postprocess_video_embeds_evs (qwen3_vl.py:2240) -> _create_final_video_embeddings (qwen3_vl.py:2293) -> get_language_model().embed_input_ids(repl_token_ids) -> vocab_parallel_embedding.py:484 forward RuntimeError: ... index is on cpu, different from other tensors on cuda:0 ``` This is **independent of speculative decoding** — it reproduces with plain `LLM.generate()`. ### Root cause In `Qwen3VLForConditionalGeneration._create_final_video_embeddings` (`vllm/model_executor/models/qwe...

## 现有链接修复摘要

#33607 [Bugfix] Fix EVS implementation for Qwen3 VL | #34246 [Core] Simplify multimodal masking | #44202 [Bugfix] Restore device placement for repl_token_ids in Qwen3-VL EVS video embeddings

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: be the bug When serving **Qwen3-VL with `video_pruning_rate > 0`** (Efficient Video Sampling / EVS) and a **video** input, generation crashes during the multimodal encoder step with a CPU/CUDA device mismatch: ``` Runti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: Qwen3-VL EVS video pruning crashes with CPU/CUDA device mismatch in _create_final_video_embeddings ### Your current environment - vLLM: `0.22.0` (release) - PyTorch: `2.11.0+cu130` - GPU: A800-80GB (also applies...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-VL EVS video pruning crashes with CPU/CUDA device mismatch in _create_final_video_embeddings ### Your current environment - vLLM: `0.22.0` (release) - PyTorch: `2.11.0+cu130` - GPU: A800-80GB (also applies...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: pu, different from other tensors on cuda:0 ``` This is **independent of speculative decoding** — it reproduces with plain `LLM.generate()`. ### Root cause In `Qwen3VLForConditionalGeneration._create_final_video_embeddin...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 2: [Bug]: Qwen3-VL EVS video pruning crashes with CPU/CUDA device mismatch in _create_final_video_embeddings ### Your current environment - vLLM: `0.22.0` (release) - PyTorch: `2.11.0+cu130` - GPU: A800-80GB (also applies...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#33607](https://github.com/vllm-project/vllm/pull/33607) | mentioned | 0.45 | [Bugfix] Fix EVS implementation for Qwen3 VL | does not. this likely escaped ci because the evs unit tests added in #33607 exercise mrope recomputation on cpu tensors, so a missing device on a token-id tensor passes the test b… |
| [#34246](https://github.com/vllm-project/vllm/pull/34246) | mentioned | 0.45 | [Core] Simplify multimodal masking | eaching here ``` ### suggested fix (1 line, mirrors #39029 / reverts #34246 for this file) ```python device = video_embeddings.device repl_token_ids = torch.tensor(video_repl.full… |
| [#44202](https://github.com/vllm-project/vllm/pull/44202) | closes_keyword | 0.95 | [Bugfix] Restore device placement for repl_token_ids in Qwen3-VL EVS video embeddings | Fixes #44200 ## Purpose Fixes a CPU/CUDA device-mismatch crash when running **Qwen3-VL with `video_pruning_rate > 0`** (Efficient Video Sampling / EVS) on video input: ``` Runti |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
