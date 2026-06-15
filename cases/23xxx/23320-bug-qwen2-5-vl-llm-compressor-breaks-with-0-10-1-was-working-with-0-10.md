# vllm-project/vllm#23320: [Bug]: Qwen2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer.

| 字段 | 值 |
| --- | --- |
| Issue | [#23320](https://github.com/vllm-project/vllm/issues/23320) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;moe;quantization;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;kernel;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ### 🛠️ Steps to reproduce Based on the llm-compressor GPTQ Qwen2.5-VL-7B example I found here: https://github.com/vllm-project/llm-compressor/blob/main/examples/multimodal_vision/qwen_2_5_vl_example.py , I created a Qwen2.5-VL-3B model which I uploaded here: https://huggingface.co/NM-dev/Qwen2.5-VL-3B-Instruct-W4A16-G128 . The only change from the script is changing the base model from the 7B to the 3B so that it was faster to quantize and easier to share and replicate. I reproduced the results with the 7B and the 32B. I created 2 images, "small.png" is 600*400 and "large.png" is 600*4000, To start the inference server with vLLM 0.10.0, I used the command: ```bash python3 -m vllm.entrypoints.openai.api_server --model NM-dev/Qwen2.5-VL-3B-Instruct-W4A16-G128 --generation-config vllm --max-model-len 32768 -tp 1 --limit_mm_per_prompt '{"images": 1, "videos": 0}' ``` (change the model with Qwen/Qwen2.5-VL-3B-Instruct to try with the base model) But with vLLM==0.10.1, started with the exact same command, I get the following error ```python INFO 08-21 07:50:08 [__init__.py:241] Automatically detected platform cuda. (APIServer pid=24129...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: rver pid=24129) INFO 08-21 07:50:10 [api_server.py:1805] vLLM API server version 0.10.1 (APIServer pid=24129) INFO 08-21 07:50:10 [utils.py:326] non-default args: {'model': 'NM-dev/Qwen2.5-VL-3B-Instruct-W4A16-G128', 'm...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 7: [Bug]: Qwen2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer. bug ### Your current environment ### 🐛 Describe...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 6: s changing the base model from the 7B to the 3B so that it was faster to quantize and easier to share and replicate. I reproduced the results with the 7B and the 32B. I created 2 images, "small.png" is 600*400 and "larg...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: n2.5-VL llm-compressor breaks with 0.10.1 (was working with 0.10.0) with A100 GPU. ValueError: Failed to find a kernel that can implement the WNA16 linear layer. bug ### Your current environment ### 🐛 Describe the bug #...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
