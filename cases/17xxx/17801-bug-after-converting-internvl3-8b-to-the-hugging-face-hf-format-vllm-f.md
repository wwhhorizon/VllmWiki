# vllm-project/vllm#17801: [Bug]: After converting InternVL3-8B to the Hugging Face (HF) format, vLLM fails to launch and throws the error: ValueError: 'limit_mm_per_prompt' is only supported for multimodal models.

| 字段 | 值 |
| --- | --- |
| Issue | [#17801](https://github.com/vllm-project/vllm/issues/17801) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;gemm;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: After converting InternVL3-8B to the Hugging Face (HF) format, vLLM fails to launch and throws the error: ValueError: 'limit_mm_per_prompt' is only supported for multimodal models.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I downloaded the model from [OpenGVLab/InternVL3-8B](https://huggingface.co/OpenGVLab/InternVL3-8B), which natively supports running OpenAI-style chat completions with vLLM. However, after converting it to the Hugging Face format using the script `transformers/src/transformers/models/internvl/convert_internvl_weights_to_hf.py`, launching vLLM resulted in the error: `ValueError: 'limit_mm_per_prompt' is only supported for multimodal models.` The command I used to launch vllm is as follows: ``` CUDA_VISIBLE_DEVICES=0,1 vllm serve $MODEL_PATH \ --tensor-parallel-size 2 \ --port $MODEL_PROT \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 65536 \ --limit-mm-per-prompt image=30,video=0\ --enable-prefix-caching \ --gpu-memory-utilization 0.6 \ --block-size 16 > "$VLLM_LOG" ``` The system runs correctly when I set MODEL_PATH to the original OpenGVLab/InternVL3-8B address. But throws an error when I change the path to the converted InternVL-3B-hf format : `ValueError: 'limit_mm_per_prompt' is only supported for multimodal models.` Could someone explain why this is happening and suggest solutions? Thank you very much! ### Before submi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: After converting InternVL3-8B to the Hugging Face (HF) format, vLLM fails to launch and throws the error: ValueError: 'limit_mm_per_prompt' is only supported for multimodal models. bug;stale ### Your current envi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. performance ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm;speculative_decoding cuda;gemm;operator;triton build_erro...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: or-parallel-size 2 \ --port $MODEL_PROT \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len 65536 \ --limit-mm-per-prompt image=30,video=0\ --enable-prefix-caching \ --gpu-memory-utilization 0.6 \ --block-size 16 > "$V...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ltimodal models.` The command I used to launch vllm is as follows: ``` CUDA_VISIBLE_DEVICES=0,1 vllm serve $MODEL_PATH \ --tensor-parallel-size 2 \ --port $MODEL_PROT \ --host 0.0.0.0 \ --dtype float16 \ --max-model-len...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: \ --enable-prefix-caching \ --gpu-memory-utilization 0.6 \ --block-size 16 > "$VLLM_LOG" ``` The system runs correctly when I set MODEL_PATH to the original OpenGVLab/InternVL3-8B address. But throws an error when I cha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
