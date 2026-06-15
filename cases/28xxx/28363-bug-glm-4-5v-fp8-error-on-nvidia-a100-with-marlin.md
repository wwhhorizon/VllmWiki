# vllm-project/vllm#28363: [Bug]: GLM-4.5V-FP8 error on NVIDIA A100 with Marlin

| 字段 | 值 |
| --- | --- |
| Issue | [#28363](https://github.com/vllm-project/vllm/issues/28363) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;fp8;gemm;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;memory_layout;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GLM-4.5V-FP8 error on NVIDIA A100 with Marlin

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.5V-FP8 --tensor-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --reasoning-parser glm45 --enable-auto-tool-choice --tool-call-parser glm45 --max-num-seqs 128 --gpu-memory-utilization 0.95 --max-model-len 65536 --allowed-local-media-path '/' --media-io-kwargs '{"video": {"num_frames": -1}}'` Error on nightly `934a9c3b79e6cb860a8d23b7f317a5f63adf0fae` for [GLM-4.5V-FP8](https://huggingface.co/zai-org/GLM-4.5V-FP8) on NVIDIA A100 with Marlin (which allows using FP8 W8A8 quantized models). Open above for the logs. `RuntimeError: Worker failed with error 'Invalid thread config: thread_m_blocks = 1, thread_k = -1, thread_n = -1, num_threads = -1 for MKN = [2048, 5472, 4096] and num_bits = 8, prob_m_split = 2048, group_size = -1, has_act_order = 0, is_k_full = 1, has_zp = 0, is_zp_float = 0, max_shared_mem_new = 166912', please check the stack trace above for the root cause` ### Before submitting a new issue... - [x] Make sure you already searched for relev...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: i.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/huggingface/hub --model zai-org/GLM-4.5V-FP8 --tensor-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --reaso...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. correctness attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;multimodal_vlm;quantization;sampling_logits;scheduler_me...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: GLM-4.5V-FP8 error on NVIDIA A100 with Marlin bug ### Your current environment ### 🐛 Describe the bug `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/hug...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: GLM-4.5V-FP8 error on NVIDIA A100 with Marlin bug ### Your current environment ### 🐛 Describe the bug `python3 -m vllm.entrypoints.openai.api_server --port 5000 --host 0.0.0.0 --download-dir /workspace/.cache/hug...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: M-4.5V-FP8 --tensor-parallel-size 2 --trust-remote-code --enable-chunked-prefill --enable-prefix-caching --reasoning-parser glm45 --enable-auto-tool-choice --tool-call-parser glm45 --max-num-seqs 128 --gpu-memory-utiliz...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
