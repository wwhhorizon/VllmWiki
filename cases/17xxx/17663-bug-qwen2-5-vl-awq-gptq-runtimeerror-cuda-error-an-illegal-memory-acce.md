# vllm-project/vllm#17663: [Bug]: Qwen2.5-VL AWQ/GPTQ RuntimeError: CUDA error: an illegal memory access was encountered 0.8.5+

| 字段 | 值 |
| --- | --- |
| Issue | [#17663](https://github.com/vllm-project/vllm/issues/17663) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 10; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;mismatch;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL AWQ/GPTQ RuntimeError: CUDA error: an illegal memory access was encountered 0.8.5+

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### Description The quantized Qwen2.5-VL (both the official and public AWQ models and private GPTQ models) fail to start on vllm 0.8.5 and 0.8.5.post1 but work on 0.8.3 and 0.8.4. I also tried on today's nightly build ```bash pip install vllm --pre --extra-index-url https://wheels.vllm.ai/nightly ``` but did not work either. The unquantized models do work as intended. ### Environment python 3.10 2 Nvidia H100 with CUDA 12.8 I tried using both --tensor-parallel-size 1 and --tensor-parallel-size 2 and it fails to start in both cases. ### Command python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-3B-Instruct-AWQ --tensor-parallel-size 1 --generation-config vllm --host 0.0.0.0 --max-model-len 32768 ### Models affected (not exhaustive) - Qwen/Qwen2.5-VL-3B-Instruct-AWQ - Qwen/Qwen2.5-VL-7B-Instruct-AWQ - Qwen/Qwen2.5-VL-32B-Instruct-AWQ - GPTQ versions (private) ### Reproduction ```bash python3 -m venv venv source venv/bin/activate pip install vllm==0.8.5.post1 ``` ```python python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-VL-3B-Instruct-AWQ --tensor-parallel-size 1 --generation-config vllm --host...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: Describe the bug ### Description The quantized Qwen2.5-VL (both the official and public AWQ models and private GPTQ models) fail to start on vllm 0.8.5 and 0.8.5.post1 but work on 0.8.3 and 0.8.4. I also tried on today'...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: Qwen2.5-VL AWQ/GPTQ RuntimeError: CUDA error: an illegal memory access was encountered 0.8.5+ bug;stale ### Your current environment ### 🐛 Describe the bug ### Description The quantized Qwen2.5-VL (both the offic...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 5: Your current environment ### 🐛 Describe the bug ### Description The quantized Qwen2.5-VL (both the official and public AWQ models and private GPTQ models) fail to start on vllm 0.8.5 and 0.8.5.post1 but work on 0.8.3 an...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: meError: CUDA error: an illegal memory access was encountered 0.8.5+ bug;stale ### Your current environment ### 🐛 Describe the bug ### Description The quantized Qwen2.5-VL (both the official and public AWQ models and pr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: rue, config_format= , dtype='auto', max_model_len=32768, guided_decoding_backend='auto', reasoning_parser=None, logits_processor_pattern=None, model_impl='auto', distributed_executor_backend=None, pipeline_parallel_size...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
