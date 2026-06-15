# vllm-project/vllm#41452: [Bug]: Gemma4-31B-it deployed on vLLM cannot process images in tool message

| 字段 | 值 |
| --- | --- |
| Issue | [#41452](https://github.com/vllm-project/vllm/issues/41452) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;scheduler_memory;speculative_decoding |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma4-31B-it deployed on vLLM cannot process images in tool message

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug An Internal Server Error (500) occurs in Gemma4-31B-it hosted on vLLM-0.20.0 when the tool-calling output includes image data. The specific error message is: `500 - {'error': {'message': "Failed to apply prompt replacement for mm_items['image'][0]", 'type': 'InternalServerError', 'param': None, 'code': 500}}` However, when the user input message contains image data, the server works without problem. #### Script to launch the vLLM server: ```bash nohup vllm serve ./$model_name \ --served-model-name "Gemma4-31B-it" \ --api-key \ --host 0.0.0.0 \ --port "${SERVICE_PORT}" \ --max-model-len 262144 \ --max-num-seqs 128 \ --tensor-parallel-size 8 \ --gpu-memory-utilization 0.90 \ --stream-interval 10 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --async-scheduling \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ > "$log_file" 2>&1 & ``` #### A minimal script to demonstrate the bug: ```python import os import sys from openai import OpenAI API_BASE = API_KEY = MODEL = "Gemma4-31B-it" # 1x1 transparent PNG — small but valid; exercises the multimodal pipeline # with no external file depend...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: Gemma4-31B-it deployed on vLLM cannot process images in tool message bug ### Your current environment ### 🐛 Describe the bug An Internal Server Error (500) occurs in Gemma4-31B-it hosted on vLLM-0.20.0 when the t...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 5: emory-utilization 0.90 \ --stream-interval 10 \ --enable-chunked-prefill \ --max-num-batched-tokens 8192 \ --async-scheduling \ --enable-auto-tool-choice \ --tool-call-parser gemma4 \ --reasoning-parser gemma4 \ > "$log...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: on vLLM-0.20.0 when the tool-calling output includes image data. The specific error message is: `500 - {'error': {'message': "Failed to apply prompt replacement for mm_items['image'][0]", 'type': 'InternalServerError',...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: AutoModelForImageTextToText.from_pretrained( MODEL_PATH, dtype=torch.bfloat16, device_map="auto", ) model.eval() run_case("Case A: image in USER message", processor, model, MESSAGES_CASE_A) print() run_case("Case B: ima...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ASE = API_KEY = MODEL = "Gemma4-31B-it" # 1x1 transparent PNG — small but valid; exercises the multimodal pipeline # with no external file dependency. TINY_PNG_B64 = ( "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
