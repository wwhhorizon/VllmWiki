# vllm-project/vllm#21266: [Bug]: GPTQ w4a16 Quantization slower than FP16 (Please Help)

| 字段 | 值 |
| --- | --- |
| Issue | [#21266](https://github.com/vllm-project/vllm/issues/21266) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;moe;quantization;sampling_logits |
| 子分类 | throughput |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling |
| 症状 | slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: GPTQ w4a16 Quantization slower than FP16 (Please Help)

### Issue 正文摘录

### 🐛 Describe the bug ## Problem I quantized the llama3-8b myself using gptq, also downloaded the quantized hf version and also used vllm llm compressor and despite it saying that it uses the gptq_marlin kernels for all those I don't see a speedup in neither the awq nor the gptq quantized versions... (running on SM90 H100GPU with Cuda-12.2 and vllm-0.9.2 installed - i pulled newest main version) I also tried different input and output-len, as well as many more prompts like 1000, but its always pretty much the same like the float16 unquantized version. ## my setup: (vllm) [gwb082@mlcbm002 vllm]$ python -c "import torch; print('Torch:', torch.__version__, '\nCUDA toolkit version:', torch.version.cuda, '\nCUDA available:', torch.cuda.is_available())" Torch: 2.7.1+cu126 CUDA toolkit version: 12.6 CUDA available: True (vllm) [gwb082@mlcbm002 vllm]$ vllm --version INFO 07-20 01:56:52 [__init__.py:235] Automatically detected platform cuda. 0.9.2rc2.dev368+g2b504eb77.precompiled ## I am testing like this: ``` (vllm) [gwb082@mlcbm012 Meta-Llama-3-8B-Instruct-quantized.w4a16]$ vllm bench throughput --model /home/geiger/gwb082/Jonathans_Thesis/compressed-models/quantized/Meta-Llama-3-8B-Ins...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ntized the llama3-8b myself using gptq, also downloaded the quantized hf version and also used vllm llm compressor and despite it saying that it uses the gptq_marlin kernels for all those I don't see a speedup in neithe...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 6: [Bug]: GPTQ w4a16 Quantization slower than FP16 (Please Help) bug;stale ### 🐛 Describe the bug ## Problem I quantized the llama3-8b myself using gptq, also downloaded the quantized hf version and also used vllm llm comp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ease Help) bug;stale ### 🐛 Describe the bug ## Problem I quantized the llama3-8b myself using gptq, also downloaded the quantized hf version and also used vllm llm compressor and despite it saying that it uses the gptq_...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ernel for GPTQMarlinLinearMethod INFO 07-20 01:26:42 [cuda.py:293] Using Flash Attention backend on V1 engine." ## Results get this as results for quantized: > Throughput: 1042.92 requests/s, 34382.06 total tokens/s, 10...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: GPTQ w4a16 Quantization slower than FP16 (Please Help) bug;stale ### 🐛 Describe the bug ## Problem I quantized the llama3-8b myself using gptq, also downloaded the quantized hf version and also used vllm llm comp...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
