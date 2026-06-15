# vllm-project/vllm#39610: [Bug]: [Regression] MiniMax-M2.7/Qwen3.5 and other FP8 models fail on A100/Ampere with nightly while loading correctly on v0.19.0

| 字段 | 值 |
| --- | --- |
| Issue | [#39610](https://github.com/vllm-project/vllm/issues/39610) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cache;cuda;fp8;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: [Regression] MiniMax-M2.7/Qwen3.5 and other FP8 models fail on A100/Ampere with nightly while loading correctly on v0.19.0

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug MiniMax-M2.7, a native FP8 model, fails on A100 (which uses Marlin weight-only quantization) but conversely works on v0.19.0. Workaround: Use `v0.19.0` for now. Seems to be happening for other Qwen FP8 models too, and potentially also NVFP4 models. https://github.com/vllm-project/vllm/issues/26431#issuecomment-4230498606 Image: `vllm/vllm-openai:minimax27-cu130` `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model MiniMaxAI/MiniMax-M2.7 --api-server-count 8 --tensor-parallel-size 4 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --max-num-seqs 128 --gpu-memory-utilization 0.95 --max-model-len 196608 --max-num-batched-tokens 16384 --enable-auto-tool-choice --tool-call-parser minimax_m2 --reasoning-parser minimax_m2` Key message: ``` (EngineCore pid=380) ERROR 04-12 05:43:37 [core.py:1110] File "/usr/local/lib/python3.12/dist-packages/vllm/v1/executor/multiproc_executor.py", line 399, in get_response (EngineCore pid=380) ERROR 04-12 05:43:37 [core.py:1110] raise RuntimeError( (EngineCore pid=380) ERROR 04-12 05:43:37 [core.py:1110] Ru...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: [Bug]: [Regression] MiniMax-M2.7/Qwen3.5 and other FP8 models fail on A100/Ampere with nightly while loading correctly on v0.19.0 bug ### Your current environment ### 🐛 Describe the bug MiniMax-M2.7, a native FP8 model,...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: [Regression] MiniMax-M2.7/Qwen3.5 and other FP8 models fail on A100/Ampere with nightly while loading correctly on v0.19.0 bug ### Your current environment ### 🐛 Describe the bug MiniMax-M2.7, a native FP8 model,...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding cache;cuda...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: [Regression] MiniMax-M2.7/Qwen3.5 and other FP8 models fail on A100/Ampere with nightly while loading correctly on v0.19.0 bug ### Your current environment ### 🐛 Describe the bug MiniMax-M2.7, a native FP8 model,...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: EngineCore pid=380) ERROR 04-12 05:43:37 [core.py:1110] def _w8a8_triton_block_scaled_mm( (EngineCore pid=380) ERROR 04-12 05:43:37 [core.py:1110] ^ (EngineCore pid=380) ERROR 04-12 05:43:37 [core.py:1110] ValueError("t...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
