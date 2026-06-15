# vllm-project/vllm#32068: [Bug]: Recompile in LLama model

| 字段 | 值 |
| --- | --- |
| Issue | [#32068](https://github.com/vllm-project/vllm/issues/32068) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Recompile in LLama model

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug When running multimodal llama4 (without compiling the encoder) and investigating the tlparse, I noticed that there was a recompile due to 0/1 specialization on `input_ids`. This can be fixed by marking `input_ids: 0` as dynamic ### Repro: ``` TORCH_TRACE=/tmp/llama_ex.txt with-proxy vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size=8 --gpu_memory_utilization=.8 --max_model_len=8192 --compilation-config='{"compile_mm_encoder":"false"}' ``` ``` TORCH_TRACE=/tmp/llama_ex_2.txt with-proxy vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size=8 --gpu_memory_utilization=.8 --max_model_len=8192 --compilation-config='{"compile_mm_encoder":"false"}' ``` ### Output Looking at the [tlparse](https://docs.vllm.ai/en/latest/design/debug_vllm_compile/#use-tlparse), we see a recompile reason: ``` 0/0: 2 = org_vocab_start_index) & (input_ < org_vocab_end_index) # vllm/vllm/model_executor/layers/vocab_parallel_embedding.py:167 in get_masked_input_and_mask (user code shown is first use of this value--the guard itself is not due user code but due to 0/1 specialization in the framework; to avoid special...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Recompile in LLama model bug;stale ### Your current environment ### 🐛 Describe the bug When running multimodal llama4 (without compiling the encoder) and investigating the tlparse, I noticed that there was a reco...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: [Bug]: Recompile in LLama model bug;stale ### Your current environment ### 🐛 Describe the bug When running multimodal llama4 (without compiling the encoder) and investigating the tlparse, I noticed that there was a reco...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nce ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ting;model_support;multimodal_vlm;sampling_logits cuda;operator;sampling;triton build_error;nan_inf env_dependency;shape Your current environment
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: n=.8 --max_model_len=8192 --compilation-config='{"compile_mm_encoder":"false"}' ``` ``` TORCH_TRACE=/tmp/llama_ex_2.txt with-proxy vllm serve meta-llama/Llama-4-Scout-17B-16E-Instruct --tensor-parallel-size=8 --gpu_memo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
