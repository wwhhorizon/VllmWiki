# vllm-project/vllm#40165: [Bug]: HunyuanOCR crashes with "query and key must have the same dtype" during inference (vLLM 0.19.0, RTX 3050)

| 字段 | 值 |
| --- | --- |
| Issue | [#40165](https://github.com/vllm-project/vllm/issues/40165) |
| 状态 | open |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;multimodal_vlm;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;gemm;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: HunyuanOCR crashes with "query and key must have the same dtype" during inference (vLLM 0.19.0, RTX 3050)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ## 🐛 Bug Report ### Description When serving `tencent/HunyuanOCR` with vLLM, the server starts successfully but crashes during the first inference request. The error occurs inside the attention backend (`flash_attn_varlen_func`) with: ```text RuntimeError: query and key must have the same dtype ``` This happens even when forcing: - `--dtype half` - `--enforce-eager` So it does not appear related to CUDA graph or compilation. --- ### Reproduction #### Command ```bash vllm serve tencent/HunyuanOCR \ --dtype half \ --no-enable-prefix-caching \ --mm-processor-cache-gb 0 \ --gpu-memory-utilization 0.8 \ --host 0.0.0.0 \ --port 8082 \ --enforce-eager ``` ### Request (OpenAI API style) ```python from openai import OpenAI client = OpenAI( base_url="http://127.0.0.1:8082/v1", api_key="EMPTY", ) response = client.chat.completions.create( model="tencent/HunyuanOCR", messages=[ { "role": "user", "content": [ {"type": "text", "text": "Extract text from this image."}, { "type": "image_url", "image_url": { "url": "https://example.com/test.png" }, }, ], } ], temperature=0.0, max_tokens=256, ) print(response) ``` ### Expected behavior Model shoul...

## 现有链接修复摘要

#40180 [Bugfix] Fix dtype mismatch in XDRotaryEmbedding for HunyuanOCR

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: "query and key must have the same dtype" during inference (vLLM 0.19.0, RTX 3050) bug ### Your current environment ### 🐛 Describe the bug ## 🐛 Bug Report ### Description When serving `tencent/HunyuanOCR` with vLLM, the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: r: query and key must have the same dtype ``` This happens even when forcing: - `--dtype half` - `--enforce-eager` So it does not appear related to CUDA graph or compilation. --- ### Reproduction #### Command ```bash vl...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: , api_key="EMPTY", ) response = client.chat.completions.create( model="tencent/HunyuanOCR", messages=[ { "role": "user", "content": [ {"type": "text", "text": "Extract text from this image."}, { "
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ring the first inference request. The error occurs inside the attention backend (`flash_attn_varlen_func`) with: ```text RuntimeError: query and key must have the same dtype ``` This happens even when forcing: - `--dtyp...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: M, the server starts successfully but crashes during the first inference request. The error occurs inside the attention backend (`flash_attn_varlen_func`) with: ```text RuntimeError: query and key must have the same dty...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40180](https://github.com/vllm-project/vllm/pull/40180) | closes_keyword | 0.95 | [Bugfix] Fix dtype mismatch in XDRotaryEmbedding for HunyuanOCR | Fixes #40165 ## Purpose HunyuanOCR / HunyuanV1 crashes with a dtype mismatch during inference: ``` RuntimeError: query and key must have the same dtype ``` **Root cause:** `XDR |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
