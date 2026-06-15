# vllm-project/vllm#19203: [Bug]: Docker, v0.9.0.1, Gemma3-4B, "Unsupported conversion from f16 to f16" on Nvidia T4

| 字段 | 值 |
| --- | --- |
| Issue | [#19203](https://github.com/vllm-project/vllm/issues/19203) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Docker, v0.9.0.1, Gemma3-4B, "Unsupported conversion from f16 to f16" on Nvidia T4

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Trying to run [Gemma3-4B](https://huggingface.co/google/gemma-3-4b-it) with following k8s manifest: ```yaml ... runtimeClassName: nvidia containers: - name: gemma3-4b-container image: goharbor.ai.xxxxxxx.cn/dockerhub/vllm/vllm-openai:latest command: - sh - -c - | python3 -m vllm.entrypoints.openai.api_server \ --model /root/.cache/huggingface \ --served-model-name Gemma3-4B \ --dtype half \ --tensor-parallel-size=4 \ --pipeline-parallel-size=1 \ --enable-chunked-prefill \ --api_key 1YmSn-------------C \ --disable-custom-all-reduce \ --gpu-memory-utilization 0.95 \ --max-model-len 128000 \ --max-num-seqs 128 \ --limit-mm-per-prompt images=5,videos=2 \ --enforce-eager ... ``` The pod launches successfully, with following noticeable logs though: ```text (VllmWorkerProcess pid=188) WARNING 06-05 02:10:05 [profiling.py:247] The sequence length used for profiling (max_num_batched_tokens / max_num_seqs = 256) is too short to hold the multi-modal embeddings in the worst case (261 tokens in total, out of which {'image': 256} are reserved for multi-modal embeddings). This may cause certain multi-modal inputs to fail during inference, even...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Docker, v0.9.0.1, Gemma3-4B, "Unsupported conversion from f16 to f16" on Nvidia T4 bug ### Your current environment ### 🐛 Describe the bug Trying to run [Gemma3-4B](https://huggingface.co/google/gemma-3-4b-it) wi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Bug]: Docker, v0.9.0.1, Gemma3-4B, "Unsupported conversion from f16 to f16" on Nvidia T4 bug ### Your current environment ### 🐛 Describe the bug Trying to run [Gemma3-4B](https://huggingface.co/google/gemma-3-4b-it) wi...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: --pipeline-parallel-size=1 \ --enable-chunked-prefill \ --api_key 1YmSn-------------C \ --disable-custom-all-reduce \ --gpu-memory-utilization 0.95 \ --max-model-len 128000 \ --max-num-s
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ocked #shared = #ttg.swizzled_shared #shared1 = #ttg.swizzled_shared #smem = #ttg.shared_memory module attributes {"ttg.num-ctas" = 1 : i32, "ttg.num-warps" = 4 : i32, ttg.target = "cuda:75", "ttg.threads-per-warp" = 32...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n outputs. You'll still be able to use a slow processor with `use_fast=False`. INFO 06-05 02:10:51 [chat_utils.py:419] Detected the chat template content format to be 'openai'. You can set `--chat-template-content-forma...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
