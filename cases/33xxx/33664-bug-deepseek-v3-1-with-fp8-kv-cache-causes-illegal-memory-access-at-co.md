# vllm-project/vllm#33664: [Bug]: DeepSeek-V3.1 with fp8 KV Cache causes illegal memory access at concurrency ≥ 5 in `serve_benchmark`

| 字段 | 值 |
| --- | --- |
| Issue | [#33664](https://github.com/vllm-project/vllm/issues/33664) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization |
| 子分类 | race_cond |
| Operator 关键词 | cache;cuda;fp8;kernel;moe;operator;triton |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency;race_condition |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: DeepSeek-V3.1 with fp8 KV Cache causes illegal memory access at concurrency ≥ 5 in `serve_benchmark`

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Using **bench serve** to test the inference performance of DeepSeekV3.1 + fp8 KV cache, on vllm0.13.0 and 0.14.0, when the concurrency is set to 5 or higher, an illegal memory error occurs. No issues were observed in tests on vllm0.11.2 and vllm0.12.0. **vllm serve** ``` VLLM_USE_DEEP_GEMM=0 vllm serve DeepSeek-V3.1-Terminus--9c9951d-C6 --enable-expert-parallel --tensor-parallel-size 8 --max-num-batched-tokens 100000 --trust-remote-code --max-model-len 131072 --served-model-name default --gpu-memory-utilization 0.85 --host 0.0.0.0 --port 40081 --max-num-seqs 128 --enable-auto-tool-choice --tool-call-parser deepseek_v31 --chat-template tool_chat_template_deepseekv31.jinja --kv-cache-dtype fp8 ``` **benchmark test** ``` vllm bench serve --backend openai-chat --base-url http://0.0.0.0:40081/v1 --endpoint /chat/completions --model default --tokenizer /opt/ml/input/data/shared/DeepSeek-V3.1-Terminus--9c9951d-C6/LFS/ --num-prompts 100 --max-concurrency 5--num-warmups 0 --random-input-len 1024 --random-output-len 256 --request-rate 10 ``` **The error output of vllm 0.13.0** ``` (Worker_TP7_EP7 pid=181548) ERROR 02-03 15:01:15 [multiproc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ker_TP7_EP7 pid=181548) ERROR 02-03 15:01:15 [multiproc_executor.py:824] Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions. (Worker_TP6_EP6 pid=181547) ERROR 02-03 15:01:15 [multiproc_executor.py:824] r...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Bug]: DeepSeek-V3.1 with fp8 KV Cache causes illegal memory access at concurrency ≥ 5 in `serve_benchmark` bug ### Your current environment ### 🐛 Describe the bug Using **bench serve** to test the inference performance...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ERROR 02-03 15:01:15 [multiproc_executor.py:824] torch.AcceleratorError: CUDA error: an illegal memory access was encountered (Worker_TP6_EP6 pid=181547) ERROR 02-03 15:01:15 [multiproc_executor.py:824] File "/opt/ml/in...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: in tests on vllm0.11.2 and vllm0.12.0. **vllm serve** ``` VLLM_USE_DEEP_GEMM=0 vllm serve DeepSeek-V3.1-Terminus--9c9951d-C6 --enable-expert-parallel --tensor-parallel-size 8 --max-num-batched-tokens 100000 --trust-remo...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: inja --kv-cache-dtype fp8 ``` **benchmark test** ``` vllm bench serve --backend openai-chat --base-url http://0.0.0.0:40081/v1 --endpoint /chat/completions --model default --tokenizer /opt/ml/input/data/shared/DeepSeek-...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
