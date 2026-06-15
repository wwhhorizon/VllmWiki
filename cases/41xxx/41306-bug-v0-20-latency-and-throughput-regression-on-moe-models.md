# vllm-project/vllm#41306: [Bug]: v0.20 latency and throughput regression on MoE models

| 字段 | 值 |
| --- | --- |
| Issue | [#41306](https://github.com/vllm-project/vllm/issues/41306) |
| 状态 | open |
| 标签 | bug |
| 评论 | 12; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe |
| 子分类 | latency_reg |
| Operator 关键词 | attention;kernel;moe |
| 症状 | build_error;slowdown |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: v0.20 latency and throughput regression on MoE models

### Issue 正文摘录

### Your current environment ### Your current environment - vLLM v0.19.0 vs v0.20.0 (`vllm/vllm-openai:v0.19.0` and `vllm/vllm-openai:v0.20.0`) - 8× NVIDIA H200 (p5en.48xlarge) ### 🐛 Describe the bug v0.20.0 introduces a latency and throughput regression on MoE models compared to v0.19.0. Dense models are not affected. **300 prompts, max-concurrency=1, sonnet (input=4096, output=512):** | Model | Type | Params | v0.19 TPOT | v0.20 TPOT | Delta | v0.19 TTFT | v0.20 TTFT | Delta | v0.19 tput | v0.20 tput | Delta | |-------|------|--------|-----------|-----------|-------|-----------|-----------|-------|-----------|-----------|-------| | Llama-3.1-8B | Dense | 8B | 2.85ms | 2.87ms | +0.7% ✅ | 46.2ms | 47.3ms | +2.4% ✅ | 340 tok/s | 338 tok/s | -0.6% ✅ | | Llama-3.1-70B | Dense | 70B | 7.56ms | 7.59ms | +0.4% ✅ | 160.6ms | 162.6ms | +1.2% ✅ | 125 tok/s | 125 tok/s | 0% ✅ | | **Mixtral-8x7B** | **MoE** | **46B** | **2.66ms** | **3.22ms** | **+21%** ❌ | **55.2ms** | **87.7ms** | **+59%** ❌ | **306 tok/s** | **248 tok/s** | **-19%** ❌ | | **DeepSeek-V2-Chat** | **MoE+MLA** | **236B** | **8.73ms** | **9.14ms** | **+4.7%** ❌ | **135.4ms** | **167.0ms** | **+23%** ❌ | **111 tok/s** | **106 t...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 6: [Bug]: v0.20 latency and throughput regression on MoE models bug ### Your current environment ### Your current environment - vLLM v0.19.0 vs v0.20.0 (`vllm/vllm-openai:v0.19.0` and `vllm/vllm-openai:v0.20.0`) - 8× NVIDI...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: duction #### Mixtral-8x7B (clearest regression) ```bash # Start server docker run -d --name vllm_test --gpus all --network host --shm-size=16g \ vllm/vllm-openai:v0.19.0 \ --model mistralai/Mixtral-8x7B-Instruct-v0.1 \...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: or-parallel-size 8 \ --max-model-len 16384 \ --max-num-seqs 16 \ --dtype bfloat16 \ --compilation-config '{"compile_sizes":[1,2,4,8],"cudagraph_mode":"FULL_AND_PIECEWISE"}' # Run benchmark vllm bench serve \ --model mis...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: v0.20 latency and throughput regression on MoE models bug ### Your current environment ### Your current environment - vLLM v0.19.0 vs v0.20.0 (`vllm/vllm-openai:v0.19.0` and `vllm/vllm-openai:v0.20.0`) - 8× NVIDI...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: vllm bench serve \ --model mistralai/Mixtral-8x7B-Instruct-v0.1 \ --backend vllm \ --dataset-name sonnet \ --dataset-path sonnet.txt \ --sonnet-input-len 4096 \ --sonnet-output-len 512 \ --num-prompts 300 \ --max-concur...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
